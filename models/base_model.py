#!/usr/bin/python3
"""
python module for BaseModel class.
"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """Base class for hbnb project."""
    def __init__(self, *args, **kwargs):
        """Initialize method with id, and created_at, updated_at."""
        if kwargs:
            kwargs["created_at"] = datetime.strptime(kwargs["created_at"],
                                                     "%Y-%m-%dT%H:%M:%S.%f")
            kwargs["updated_at"] = datetime.strptime(kwargs["updated_at"],
                                                     "%Y-%m-%dT%H:%M:%S.%f")
            for key in kwargs.keys():
                if key != "__class__":
                    (self.__dict__)[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """print format: [<class name>] (<self.id>) <self.__dict__>"""
        return "[{}] ({}) {}".format(type(self).__name__,
                                     self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute updated_at with the current
        datetime."""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__
        of the instance."""
        dict = (self.__dict__).copy()
        dict["__class__"] = type(self).__name__
        dict["created_at"] = (dict["created_at"]).isoformat()
        dict["updated_at"] = (dict["updated_at"]).isoformat()
        return dict
