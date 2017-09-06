from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager


from trouble.config import Configuration	# Import our configuration data

app = Flask(__name__)
app.config.from_object(Configuration)

# --- Flask-SQLAlchemy ---
db = SQLAlchemy(app)

# --- Flask-Migrate ---
migrate = Migrate(app, db)

# --- Flask-Script ---
manager = Manager(app)
manager.add_command('db', MigrateCommand)