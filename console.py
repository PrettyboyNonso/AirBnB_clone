#!/usr/bin/python3
"""Console Module"""
import cmd
import sys
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Contains the functionality for the console"""

    prompt = "(hbnb) "

    classes = {'BaseModel': BaseModel}

    def preloop(self):
        """Print if isatty is false"""
        if not sys.__stdin__.isatty():
            print('(hbnb)')

    def do_quit(self, command):
        """Method to exit the HBNB console"""
        exit()

    def help_quit(self):
        """Print the help documentation for the quit command"""
        print("Exits the program with formatting\n")

    def do_EOF(self, arg):
        """Handles EOF to exit the console"""
        print()
        exit()

    def help_EOF(self):
        """Prints the help documentation for the EOF"""
        print("Exit the program without formatting\n")

    def emptyline(self):
        """Override the emmptyline method of cmd"""
        pass

    def do_create(self, args):
        """Create an object of given parameter"""
        if not args:
            print("** class name missing **")
        elif args not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        new_instance = HBNBCommand.classes[args]()
        storage.save()
        print(new_instance.id)
        storage.save()

    def help_create(self):
        """Help info for the create method"""
        print("Create a class of any type")
        print("[usage]: create <className>\n")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
