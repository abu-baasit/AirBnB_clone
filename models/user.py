#!/usr/bin/python3
'''
Creating a User class that inherits from the basemodel
'''
from models.base_model import BaseModel


class User(BaseModel):
    '''
    Class User inherits from BaseModel the attributes below
    '''
    email = ''
    password = ''
    first_name = ''
    last_name = ''
