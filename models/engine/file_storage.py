# models/engine/file_storage.py
import json
from models.base_model import BaseModel
from models.user import User

class FileStorage:
    """Serializes instances to a JSON file & deserializes back to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects (only if the JSON file (__file_path) exists)"""
        try:
            with open(self.__file_path, 'r') as f:
                obj_dict = json.load(f)
            for key, value in obj_dict.items():
                class_name = value["__class__"]
                if class_name == "BaseModel":
                    self.__objects[key] = BaseModel(**value)
                elif class_name == "User":
                    self.__objects[key] = User(**value)
        except FileNotFoundError:
            pass
