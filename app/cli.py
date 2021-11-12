import click
from flask import Blueprint

from models.Names import Names

from db import conn

bp = Blueprint('commands', __name__)

@bp.cli.command("say_my_name")
@click.option('-name', default="Noname")
def say_my_name(name):
    print("say_my_name %s " % name)

@bp.cli.command("create_db")
@click.option('-name', default="Noname")
def create_db(name):
    print("creating db %s " % name)
    conn.drop_all()
    conn.create_all()
    conn.session.commit()
