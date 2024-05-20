#!/usr/bin/python3
import uuid
from datetime import datetime
import models

format_date_time = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """This is a basemodel"""

    def __init__(self, *args, **kwargs):
        """This initializes the class instances on creation"""
        if args is not None and len(args) > 0:
            pass
        if kwargs:
            for key, value, in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    value = datetime.strptime(value, format_date_time)
                if key not in ["__class__"]:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        """This prints the string representation of the instance"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """This saves changes to the instance"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """This method returns a dictionary containing all"""
        dict_ionary = self.__dict__.copy()
        dict_ionary['__class__'] = self.__class__.__name__
        dict_ionary['created_at'] = self.created_at.isoformat()
        dict_ionary['updated_at'] = self.updated_at.isoformat()
        return dict_ionary
