#!/usr/bin/python3
"""
Module: 6-model_state

Contains the definition of the State class and creates the corresponding table in the database.
"""

import sys
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

class State(Base):
    """
    State class inherits from Base.

    Attributes:
        __tablename__: Name of the table in the database.
        id: Integer column representing the primary key.
        name: String column representing the state name.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

if __name__ == "__main__":
    """
    Main entry point of the script.
    Connects to the MySQL server and creates the necessary table.
    """
    # Connect to MySQL server running on localhost at port 3306
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
