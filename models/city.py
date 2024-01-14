#!/usr/bin/python3
'''
Creating a City class
'''
from models.base_model import BaseModel


class City(BaseModel):
    '''
    State class inherits from BaseModel with the listed attributes
    '''
    state_id = ''
    name = ''
