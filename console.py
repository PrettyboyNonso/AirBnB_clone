#!/usr/bin/python3
"""
console.py

This module provides a command-line interface (CLI) for the AirBnB clone project.
It allows users to interact with the application through various commands to
create, update, delete, and display instances of different classes.
"""

import cmd
import json
import shlex
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

classes = {
    'BaseModel': BaseModel, 'User': User, 'Place': Place,
    'State': State, 'City': City, 'Amenity': Amenity, 'Review': Review
}


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class implements the command interpreter for the AirBnB clone project.

    This class inherits from cmd.Cmd and provides various commands to manage
    instances of different models such as BaseModel, User, Place, State, City,
    Amenity, and Review.
    """

    prompt = '(hbnb) '

    def do_EOF(self, arg):
        """Handle EOF to exit the program."""
        return True

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def emptyline(self):
        """Do nothing on empty input line."""
        pass

    def do_create(self, args):
        """
        Create a new instance of BaseModel, saves it (to the JSON file),
        and prints the id. Ex: $ create BaseModel
        """
        if not args:
            print("** class name missing **")
            return
        if args not in classes:
            print("** class doesn't exist **")
            return
        instance = classes[args]()
        instance.save()
        print(instance.id)

    def do_show(self, args):
        """
        Prints the string representation of an instance based on the class
        name and id. Ex: $ show BaseModel 1234-1234-1234
        """
        args = shlex.split(args)
        if not args:
            print("** class name missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        try:
            print(storage.all()[key])
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, args):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file). Ex: $ destroy BaseModel 1234-1234-1234
        """
        args = shlex.split(args)
        if not args:
            print("** class name missing **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        key = f"{args[0]}.{args[1]}"
        if key in storage.all():
            del storage.all()[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, args):
        """
        Prints all string representation of all instances based or not on the class name.
        Ex: $ all BaseModel or $ all
        """
        args = shlex.split(args)
        obj_list = []
        if args:
            if args[0] not in classes:
                print("** class doesn't exist **")
                return
            obj_list = [str(obj) for obj in storage.all().values() if isinstance(obj, classes[args[0]])]
        else:
            obj_list = [str(obj) for obj in storage.all().values()]
        print(obj_list)
    
    def do_update(self, args):
    """
    Updates an instance based on the class name and id by adding or
    updating attribute (save the change into the JSON file).
    Ex: $ update BaseModel 1234-1234-1234 email "aibnb@holbertonschool.com"
    """
    args = shlex.split(args)
    if len(args) == 0:
        print("** class name missing **")
        return
    if args[0] not in classes:
        print("** class doesn't exist **")
        return
    if len(args) < 2:
        print("** instance id missing **")
        return
    key = f"{args[0]}.{args[1]}"
    if key not in storage.all():
        print("** no instance found **")
        return
    if len(args) < 3:
        print("** attribute name missing **")
        return
    if len(args) < 4:
        print("** value missing **")
        return
    instance = storage.all()[key]
    setattr(instance, args[2], args[3])
    instance.save()
        

    def default(self, line):
        """
        Handle default behavior when an invalid command is entered.
        Check if the command follows the format "<class name>.all()", "<class name>.count()",
        "<class name>.show(<id>)", "<class name>.destroy(<id>)", or "<class name>.update(<id>, <attribute name>, <attribute value>)"
        and call the corresponding class method if it matches.
        """
        parts = line.split('.')
        if len(parts) == 2:
            class_name, method_call = parts[0], parts[1]
            if class_name in classes:
                if method_call == "all()":
                    self.do_all(class_name)
                    return
                elif method_call == "count()":
                    count = sum(1 for obj in storage.all().values() if obj.__class__.__name__ == class_name)
                    print(count)
                    return
                elif method_call.startswith("show(") and method_call.endswith(")"):
                    instance_id = method_call[5:-1]
                    self.do_show(f"{class_name} {instance_id}")
                    return
                elif method_call.startswith("destroy(") and method_call.endswith(")"):
                    instance_id = method_call[8:-1]
                    self.do_destroy(f"{class_name} {instance_id}")
                    return
                elif method_call.startswith("update(") and method_call.endswith(")"):
                    args_str = method_call[7:-1]
                    args = shlex.split(args_str)
                    if len(args) == 3:
                        self.do_update(f"{class_name} {args[0]} {args[1]} {args[2]}")
                    return
        print("*** Unknown syntax: {}".format(line))

if __name__ == '__main__':
    HBNBCommand().cmdloop()
