import sqlite3 as sql
import click
from flask import current_app, g

def get_db():
    if 'db' not in g:
        g.db = sql.connect(
            current_app.config['DATABASE'],
            detect_types = sql.PARSE_DECLTYPES
        )
