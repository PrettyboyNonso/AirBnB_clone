#!/usr/bin/python3
""" Class FileStorage """

from json import load, dump
from os.path import exists

class FileStorage:
    """Handles storage of all class instances."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Sets the obj with key in __objects"""
        class_name = obj.__class__.__name__
        obj_id = obj.id
        FileStorage.__objects[f"{class_name}.{obj_id}"] = obj

    def save(self):
        """Saves __objects to JSON file"""
        dict_to_json = {key: obj.to_dict() for key, obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, "w", encoding='utf-8') as file:
            dump(dict_to_json, file)

    def reload(self):
        """Loads storage dictionary from file"""
        if exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding='utf-8') as file:
                obj_dict = load(file)
                for key, value in obj_dict.items():
                    class_name = key.split('.')[0]
                    module_path = f"models.{class_name.lower()}"
                    module = __import__(module_path, fromlist=[class_name])
                    class_ = getattr(module, class_name)
                    FileStorage.__objects[key] = class_(**value)
