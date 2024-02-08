#!/usr/bin/python3
"""Defines the HBnB console."""

import shlex
import models
from models import *
import cmd

class HBNBCommand(cmd.Cmd):
    """Class that entry point of the command interpreter
    """

    prompt = '(hbnb)'
    cmd = ["create", "show", "all", "destroy", "update", "count"]
    class_list = ["BaseModel", "User", "State", "City", "Amenity",
                    "Place", "Review"]

    def do_EOF(self, args):
        """exit the program, if end of file
        """
        return True

    def do_quit(self, args):
        """quit the program
        """
        return True

    def empty_line(self):
        """an empty line + ENTER shouldn’t execute anything
        """
        pass

    def parse(line):
        """Parses a given string, and returns a list
        """
        return shlex.split(line)

    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it 
        (to the JSON file) and prints the id
        """

        arg = parse(line)
        if not arg:
            print("** class name missing **")
        if arg[0] not in self.class_list:
            print("** class doesn't exist **")
        else:
            obj = self.class_list[arg[0]]()
            print(obj.id)
            models.storage.save()

    def do_show(self, line):
        """Prints the string representation of an instance based 
        on the class name and id
        """

        arg = parse(line)
        if not arg:
            print("** class name missing **")
        elif arg[0] not in self.class_list:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        else:
            obj = models.storage.all()
            key = args[0] + '.' + args[1]
            try:
                new_key = obj[key]
                print(new_key)
            except KeyError:
                print('** no instance found **')

    def do_destroy(self, line):
        """ Deletes an instance based on the class name and id 
        (save the change into the JSON file)
        """

        arg = parse(line)
        if not arg:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            obj = models.storage.all()
            key = args[0] + '.' + args[1]
            try:
                new_key = obj[key]
                obj.pop(key)
                del new_key
                models.storage.save()
            except KeyError:
                print("** no instance found **")


