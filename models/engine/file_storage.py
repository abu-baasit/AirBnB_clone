#!/usr/bin/python3
"""A storage for the class basemodel"""
import json
import os
from models.base_model import BaseModel


class FileStorage:
    """A class for virtual storage engine.
    Attributes:
        __file_path(str): name of object storage
        __objects(dict): a dictionary
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """method that returns dictionary of objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in objects the obj with key <obj class name>.id"""
        key = "{} {}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file file_path."""
        my_objects = {}
        for key, obj in Filestorage.__objects.items():
            my_objects[key] = obj.to_dict()

        with open(FileStorage.__file_path, 'w') as f:
            json.dump(my_objects, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        storage = FileStorage._objects
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as f:
                storage = json.loads(f)
                for key, value in storage.items():
                    name = value["__class__"]
                    self.new(eval(name)(**value))
