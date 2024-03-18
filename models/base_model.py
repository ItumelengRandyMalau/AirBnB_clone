#!/usr/bin/python3
"""BaseModel that defines all common attributes
    and methods for other classes"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """BaseModel class"""
    def __init__(self, *args, **kwargs):
        """Initializes class"""
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key in ['created_at', 'updated_at']:
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        """Saves the class"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Dictionary representation of object"""
        dict_instance = self.__dict__.copy()
        dict_instance.update({
            '__class__': self.__class__.__name__,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
            })
        return dict_instance

    def __str__(self):
        """Returns string representation of object"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
