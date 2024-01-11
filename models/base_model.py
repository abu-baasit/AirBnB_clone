#!/usr/bin/python3
"""Defines a BaseModel for parent class"""
import models
import uuid
from datetime import datetime


class BaseModel:
    """ defines base model that defines all common
    attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """initialize/construct a basemodel
        Args:
            - *args: list of arguments
            - **kwargs: dict of key/value pair argument
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        value = datetime.strptime(value,
                                                  '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, value)
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """Returns the string that represents the
        instance of the base model"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """updates attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save(self)

    def to_dict(self):
        """returns a dictionary containing all keys/values pairs of __dict__"""
        result_dict = self.__dict__.copy()
        result_dict['__class__'] = self.__class__.__name__
        result_dict['created_at'] = self.created_at.isoformat()
        result_dict['updated_at'] = self.updated_at.isoformat()
        return result_dict
