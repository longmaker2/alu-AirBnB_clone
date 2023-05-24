#!/usr/bin/python3
"""
Parent class to all classes in the AirBnB clone project
"""


from datetime import datetime
from uuid import uuid4
import models


class BaseModel:
    """Custom BaseModel class for the AirBnB clone project
    Attributes:
        id (str): unique id for each instance
        created_at (datetime): time object was created
        updated_at (datetime): time object was updated

    Methods:
        __init__: initializes class instance
        __str__: returns string representation of class instance
        save: updates attribute updated_at with current datetime
        to_dict: returns dictionary representation of class instance
    """

    def __init__(self, *args, **kwargs):
        """initializes class instance
        Args:
            *args: unused
            **kwargs: dictionary of attributes
        """
        DATE_TIME_FORMAT = "%Y-%m-%dT%H:%M:%S.%f"
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)
        else:
            for key, v in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    self.__dict__[key] = datetime.strptime(v, DATE_TIME_FORMAT)
                elif key[0] == "id":
                    self.__dict__[key] = str(v)
                else:
                    self.__dict__[key] = v

    def __str__(self):
        """returns string representation of class instance
        Returns:
            str: string representation of class instance
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """updates attribute updated_at with current datetime"""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """returns dictionary representation of class instance
        Returns:
            dict: dictionary representation of class instance
        """
        new_objects = {}
        for key, value in self.__dict__.items():
            if key in ["created_at", "updated_at"]:
                new_objects[key] = value.isoformat()
            else:
                new_objects[key] = value
        new_objects["__class__"] = self.__class__.__name__
        return new_objects