#!/usr/bin/python3
"""Database storage class for hbnb"""
import os
import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import models
from models.base_model import BaseModel, Base
from models.city import City
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    """Database storage class"""

    __engine = None
    __session = None

    classes = {
        'State': State,
        'City': City,
        'User': User,
        'Place': Place,
        'Review': Review
    }

    def __init__(self):
        """Setup for Dbstorage instances"""
        user = os.getenv("HBNB_MYSQL_USER")
        pwd = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST")
        db = os.getenv("HBNB_MYSQL_DB")
        env = os.getenv("HBNB_ENV")

        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                user,
                pwd,
                host,
                db
            ), pool_pre_ping=True
        )

        if env == "test":
            Base.metadata.dropall(self.__engine)

    def all(self, cls=None):
        """returns a new dictionary like filestorage"""

        ret_dict = {}

        for item in self.classes.keys():
            if cls == item or cls is None:
                objs = self.__session.query(self.classes[item]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    ret_dict[key] = obj
        return (ret_dict)

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reload data into database"""
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker()
        Session.configure(bind=self.__engine, expire_on_commit=False)
        DBStorage.__session = scoped_session(Session)
    
    def close(self):
        """ release connection owned by session """
        self.__session.remove()
