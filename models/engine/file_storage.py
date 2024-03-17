#!/usr/bin/python3
"""Defines the FileStorage class"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Represents an abstracted storage engine.
    Attributes:
        __file_path: File name in which to save ojects.
        __objects: A dictionary of instantiated object.
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        obj_key = f'{obj.__class__.__name__}.{obj.id}'
        FileStorage.__objects[obj_key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        serialized_objs = {}
        for key, value in FileStorage.__objects.items():
            serialized_objs[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w') as save_file:
            json.dump(serialized_objs, save_file)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path, 'r') as reload_file:
                json_data = json.load(reload_file)
                for key, value in json_data.items():
                    class_name, obj_id = key.split('.')
                    obj = eval(class_name)(**value)
                    self.new(obj)
        except FileNotFoundError:
            pass
