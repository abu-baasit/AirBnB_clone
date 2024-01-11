#!/usr/bin/python3
"""__init__ method contained in model directory"""
from models.engine.file_ import FileStorage


storage = FileStorage()
storage.reload()
