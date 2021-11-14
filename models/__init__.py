#!/usr/bin/python3
"""Init module for models package"""
from models.engine import file_storage


FileStorage = file_storage.FileStorage
storage = FileStorage()
storage.reload()
