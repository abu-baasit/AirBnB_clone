#!/usr/bin/python3
'''
This is a BaseModel class that defines all common attributes/methods
for other classes
'''
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    '''
    BaseModel class
    '''

    def __init__(self, *args, **kwargs):
        '''
        Constructor method
        '''
        if not kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        value = datetime.strptime(value,
                                                  '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            self.save()
            models.storage.new(self)

    def save(self):
        '''
        Update public instance with current datetime
        '''
        self.updated_at = datetime.now()
        models.storage.save()

    def __str__(self):
        '''
        String representation
        '''
        return '[{}] ({}) {}'.format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def to_dict(self):
        '''
        Dictionary containing all
        keys/values of __dict__
        '''
        my_dict = self.__dict__.copy()
        my_dict['__class__'] = self.__class__.__name__
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        return my_dict
