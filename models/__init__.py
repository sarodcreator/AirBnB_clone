#!/usr/bin/python3
"""Initializer that passes storage function from engine"""

from models.engine.file_storage import FileStorage
#import models.engine.file_storage

storage = FileStorage()
storage.reload()
