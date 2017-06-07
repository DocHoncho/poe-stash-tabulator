import click
import flask

from . import initdb

def install_commands(app):
	#import pdb; pdb.set_trace()
	app.cli.add_command(initdb.initdb, 'initdb')