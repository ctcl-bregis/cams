# db_setup.py
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

# Location of the database file
dbfile = "data/data.db"

basedir = os.path.abspath(os.path.dirname(__file__))
engine = create_engine('sqlite:///' + os.path.join(basedir, dbfile), convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit = False, autoflush = False, bind = engine))
Base = declarative_base()
Base.query = db_session.query_property()

def initdb():
    import models
    Base.metadata.create_all(bind = engine)

def checkdb(db):
    if not os.path.isfile(db): 
        return False
    
    size = os.path.getsize(db)

    # file is empty, give benefit of the doubt that its sqlite
    # New sqlite3 files created in recent libraries are empty!
    if size == 0: 
        return True

    # SQLite database file header is 100 bytes
    if size < 100: 
        return False
    
    # Validate file header
    with open(db, 'rb') as fd: 
        header = fd.read(100)    

    return (header[:16] == b'SQLite format 3\x00')

