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

    def do_show(self, args):
        """Method to show the individual object based on id"""
        new_args = args.split(" ")
        c_name = new_args[0]
        c_id = new_args[2]

        if c_id and " " in c_id:
            c_id = c_id.partition(' ')[0]

        if not c_name:
            print("** class name missing **")
            return

        if c_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if not c_id:
            print('** instance id missing **')
            return

        key = c_name + "." + c_id
        try:
            print(storage._FileStorage__objects[key])
        except KeyError:
            print("** no instance found **")

    def help_show(self):
        """Help for the show command"""
        print("Show an individual instance of a class")
        print("[usage]: show <className> <objectId>\n")

    def do_destroy(self, args):
        """Destroy a specific object"""
        new_args = args.split(" ")
        c_name = new_args[0]
        c_id = new_args[2]

        if c_id and " " in c_id:
            c_id = c_id.partition(' ')[0]

        if not c_name:
            print("** class name missing **")
            return

        if c_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if not c_id:
            print('** instance id missing **')
            return

        key = c_name + "." + c_id
        try:
            del(storage.all()[key])
            storage.save()
        except KeyError:
            print("** no instance found **")

    def help_destroy(self):
        """Help for the destroy command"""
        print("Destroys an individual instance of a class")
        print("[usage]: destroy <className> <objectId>\n")

    def do_all


if __name__ == "__main__":
    HBNBCommand().cmdloop()
