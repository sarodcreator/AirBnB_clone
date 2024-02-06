#!/usr/bin/python3
"""Defines the HBnB console."""

import shlex
import models
from models.base_model import BaseModel
from models.__init__ import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
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

