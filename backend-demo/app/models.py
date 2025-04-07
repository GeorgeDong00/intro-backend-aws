from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db):
    """
        Sample User Table
    -------------------------------
    id | netid  | name
    -------------------------------
     1 | cw566  | Who's That Pokémon?
     2 | yw2645 | Who's That Pokémon?
        ...
     42| gd289  | George Dong
    """

    __tablename__ = "Users"

    # Characteristics of an user
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    netid = db.Column(db.Text, nullable=False)
    name = db.Column(db.Text, nullable=False)

    # Each AguaClara member has multiple weekly hour entries.
    entries = db.relationship(
        "WeeklyEntries", backref="Users", lazy=True, cascade="all, delete-orphan"
    )


class WeeklyEntry(db):
    """
        Sample Weekly Entries Table
    -----------------------------------------------
    entry id | week number | hours spent | user id
    -----------------------------------------------
        1    |      0      |      7      |   1       # a weekly entry submitted by (cw566)
        2    |      1      |      3      |   2       # a weekly entry submitted by (yw2645)
        3    |      2      |      5      |   1       # a weekly entry submitted by (cw566)
            ...
        9    |      5      |      5      |   42      # a weekly entry submitted by (gd289)
    """

    __tablename__ = "WeeklyEntries"

    # Characteristics of a weekly entry
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    week_number = db.Column(db.Text, nullable=False)
    worked_hours = db.Column(db.Integer)

    # Each weekly entry have a corresponding user id number, identifying who submitted entry.
    user_id = db.Column(db.Integer, db.ForeignKey("Users.id"), nullable=False)
