#!/usr/bin/python3
""" This module includes defines a class BaseModel"""
import uuid
import datetime


class BaseModel:
    """ defines all common attributes/methods for other classes"""

    def __init__(self):
        """initializes attributes"""
        self.id = str(uuid.uuid4())
        current_time = datetime.datetime.now()
        self.created_at = current_time
        self.updated_at = current_time

    def save(self):
        """updates 'updated_at' with the current datetime"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """ returns a dictionary containing all keys/values of the instance"""
        dict_instance = self.__dict__.copy()
        dict_instance.update({
            '__class__': self.__class__.__name__,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
            })
        return dict_instance

    def __str__(self):
        """prints [<class name>] (<self.id>) <self.__dict__>"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
