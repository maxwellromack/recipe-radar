import os
from flask import Flask

def create_app(test_config = None):
    app = Flask(__name__, instance_relative_config = True)
    app.config.from_mapping(
        SECRET_KEY = 'dev', # change this before deploying
        DATABASE = os.path.join(app.instance_path, 'backend.sqlite'),
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent = True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass # TODO: exception handling
    
    @app.route('/example')  # remove once we get an actual landing page working
    def example():
        return "This is an example of a webpage!"

    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import user
    app.register_blueprint(user.bp)

    from . import reccomend
    app.register_blueprint(reccomend.bp)
    
    return app
