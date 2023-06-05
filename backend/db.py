import sqlite3
import click
import os, time
from flask import current_app, g
import numpy as np

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

    db.execute(
        'CREATE TABLE recipe (id INTEGER PRIMARY KEY AUTOINCREMENT, ingredients BLOB)'
    )
    db.commit()

    size = 0
    with open('backend/ingredients_list.txt') as file:
        for size, _ in enumerate(file):
            pass

    updated = 0
    with os.scandir('backend/recipes/') as dir:
        for entry in dir:
            arr = np.zeros(size, dtype = 'int')
            index = 0
            with open('backend/ingredients_list.txt', 'r') as list:
                while ingredient := list.readline():
                    with open(entry.path, 'r') as recipe:
                        if ingredient in recipe.read():
                            arr[index] = 1
                        index += 1
            bin_str = np.array2string(arr)
            bin_str = bin_str.replace(' ','')
            bin_str = bin_str.replace(']','')
            data = bin_str.replace('[','')
            db.execute(
                'INSERT INTO recipe (ingredients) VALUES (?)',
                (data,)
            )
            db.commit()
            print("Added " + str(entry.name) + " to the database.")
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
