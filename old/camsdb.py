# CAMS by CrazyblocksTechnologies Computer Laboratories
# Created - Last Updated: October 19, 2022 - November 3, 2022
# Purpose: Database access code to simplify the main script (app.py)

from app import cams
import os


dbfile = "data/data.db"

basedir = os.path.abspath(os.path.dirname(__file__))

cams.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, dbfile)
cams.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(cams)
