#!/usr/bin/python3
"""Console Module"""
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """Contains the functionality for the console"""

    prompt = "(hbnb) "

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


if __name__ == "__main__":
    HBNBCommand().cmdloop()
