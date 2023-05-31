import sqlite3
import click
import os
from flask import current_app, g

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

def add_recipes():  # Adds new recipes to the database
    db = get_db()
    num_recipes = 0
    recipes_added = 0
    path = 'backend/recipes/'
    dir = os.listdir(path)

    for f in dir:
        if os.path.isfile(os.path.join(path,f)):
            num_recipes +=1

    max_id = (db.execute(
        'SELECT MAX(id) FROM recipe'
    )).fetchone()[0]
    if not max_id:  # No values in table
        for id in range(num_recipes):
            with open(path + str(id) + '.txt', 'r') as file:
                line = file.readline()
                while 'METADATA:' not in line:
                    line = file.readline()

                ingredients = line[10:]
                db.execute(
                    'INSERT INTO recipe (ingredients) VALUES (?)',
                    (ingredients,)
                )
                db.commit()
                recipes_added += 1
    else:
        for id in range(int(max_id) + 1, num_recipes):
            with open(path + str(id) + '.txt', 'r') as file:
                line = file.readline()
                while 'METADATA:' not in line:
                    line = file.readline()

                ingredients = line[10:]
                db.execute(
                    'INSERT INTO recipe (ingredients) VALUES (?)',
                    (ingredients,)
                )
                db.commit()
                recipes_added += 1
    return recipes_added

@click.command('init-db')
def init_db_command():
    """"Clear the existing data and create new tables."""
    init_db()
    click.echo("Initialized the database.")

@click.command('add-recipes')
def add_recipes_command():
    """Add new recipes to the database."""
    recipes_added = add_recipes()
    click.echo(str(recipes_added) + " recipe(s) added to the database.")

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
    app.cli.add_command(add_recipes_command)
