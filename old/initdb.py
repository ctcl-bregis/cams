from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

basedir = os.path.abspath(os.path.dirname(__file__))

dbengine = create_engine('sqlite:///' + os.path.join(basedir, dbfile), echo = True)
dbbase = declarative_base()

# Memory Module Device Type
class memd(dbbase):
    __tablename__ = "memd"

    id = Column(Integer, primary_key=True)
    
    note = Column(String)
