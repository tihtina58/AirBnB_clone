#!/usr/bin/python3
"""Python module for FileStorage class."""
import json


class FileStorage:
    """This class serialize instances to a JSON file and deserialize
    JSON file to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns objects dictionary."""
        return type(self).__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = type(obj).__name__ + "." + obj.id
        ((type(self)).__objects)[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        path = type(self).__file_path
        objects = type(self).__objects
        obj_to_dict = {}
        for key, value in objects.items():
            obj_to_dict[key] = value.to_dict()
        with open(path, 'w', encoding='utf-8') as my_file:
            json.dump(obj_to_dict, my_file)

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON
        file (__file_path) exists; otherwise, do nothing."""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        path = type(self).__file_path
        try:
            with open(path, mode='r', encoding='utf-8') as my_file:
                objs_dicts = json.load(my_file)
            for key, value in objs_dicts.items():
                obj = eval(value['__class__'] + '(**value)')
                type(self).__objects[key] = obj
        except:
            pass
