import click

from db import Base
from db import DB

@click.command()
def initdb():

	click.echo('Suck it')