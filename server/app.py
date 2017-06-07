import json
import os

import flask
from flask import Flask, flash, session, request, redirect, url_for
from jinja2 import Environment, FileSystemLoader, select_autoescape

import logging
import logging.config

import db

DEFAULT_LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'loggers': {
        '': {
            'level': 'INFO', 
        },
        'another.module': {
            'level': 'DEBUG',
        },
    }
}
logging.config.dictConfig(DEFAULT_LOGGING)

THIS_DIR = os.path.dirname(os.path.abspath(__file__))

env = Environment(
    loader=FileSystemLoader(os.path.join(THIS_DIR, 'templates')),
    autoescape=select_autoescape(['html', 'xml'])
    )


app = Flask(__name__)
app.secret_key = 'ballsacks'
app.state = {}
app.settings = {
    'data_directory': 'data' 
}

db_path = app.settings['data_directory'] + '/app.db'
app.db = db.DB(db_path)

db.create_database(app.db)

from commands import install_commands
install_commands(app)

@app.context_processor
def inject_globals():
    return {
        'APP' : {
            'app_title': 'Path of Exile Stash Tabulator',
            'app_version': '0.0.1'
            }
        }

@app.route('/import', methods=['POST'])
def do_import():
    try:
        app.state['_raw_data'] = json.loads(request.form['importData'])
    except json.JSONDecodeError as e:

        logging.error(str(e))
        flash(str(e), 'danger')

    return redirect(url_for('index'))

@app.route('/', methods=['GET'])
def index():
    
    return flask.render_template('app.html', state=app.state)
    

if __name__ == '__main__':
    app.run(debug=True)
