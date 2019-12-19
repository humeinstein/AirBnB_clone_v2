#!/usr/bin/python3
"""create a unique FileStorage instance for your application"""
import os
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

classes = {
    'Place': Place,
    'State': State,
    'User': User,
    'City': City,
    'BaseModel': BaseModel,
    'Review': Review,
    'Amenity': Amenity
}

if os.getenv("HBNB_TYPE_STORAGE") == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()
