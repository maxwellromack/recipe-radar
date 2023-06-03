import sqlite3
import click
import os, time
from flask import current_app, g
import backend.ingredients as ing

def get_db():
    if 'db' not in g:
        # connect to the database
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types = sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row  # returns rows that act like dicts so we can
    return g.db                         # access columns by name

def close_db(e = None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))

def update_recipes():
    db = get_db()

    db.execute('DROP TABLE IF EXISTS recipe')
    db.commit()

    updated = 0
    with os.scandir('recipes/') as dir:
        for entry in dir:
            data = ing.encode(entry.path)
            try:
                db.execute(
                    'INSERT INTO recipe ingredients VALUES ?',
                    data,
                )
                db.commit()
            except:
                print("Something went wrong adding " + str(entry.name))
            else:
                updated += 1
    
    return updated
    
@click.command('update-recipes')
def update_recipes_command():
    """""Updates all the recipes in the database. WARNING: HIGH COMPUTATION COST!"""
    updated = update_recipes()
    click.echo("Updated " + str(updated) + " recipes.")

@click.command('init-db')
def init_db_command():
    """"Clear the existing data and create new tables."""
    init_db()
    click.echo("Initialized the database.")

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
    app.cli.add_command(update_recipes_command)
