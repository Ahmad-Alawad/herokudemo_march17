from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Melon(db.Model):
    """Melon we offer for sale."""

    id = db.Column(db.Integer,
                   nullable=False,
                   primary_key=True)

    name = db.Column(db.String(50),
                     nullable=False,
                     unique=True)


def connect_to_db(app, db_uri=None):
    """Connect our application to our database."""

    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri or 'postgres:///hackbright'
    db.app = app
    db.init_app(app)
    print "Connected to DB."
