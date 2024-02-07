#!/usr/bin/python3
''' Defines unittest for console.py'''
import os
import sys
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand

class TestAirBnB_CloneConsole(unittest.TestCase):
    ''' Tests the AirBnB_clone console'''
    def test_prompt_present(self):
        '''Test if the prompt is displayed'''
        self.assertEqual("(hbnb)", HBNBCommand.prompt)

    def test_empty_line(self):
        '''Tests if line is empty'''
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", output.getvalue().strip())
    
    ''' Testing help messages of HBNB'''
    def test_help(self):
        ''' Tests if help prints available commands and how to use it'''
        help_message = ("Documented commands (type help <topic>):\n"
                        "========================================\n"
                        "EOF  help  quit")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help"))
            self.assertEqual(help_message, output.getvalue().strip())

    def test_help_EOF(self):
        '''Test if help EOF print correct help message'''
        help_message = "exit the program, if end of file"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help EOF"))
            self.assertEqual(help_message, output.getvalue().strip())

    def test_help_quit(self):
        '''Test if help quit prints correct help message'''
        help_message = "quit the program"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help quit"))
            self.assertEqual(help_message, output.getvalue().strip())
    
    '''Testing commands'''
    def test_quit(self):
        '''Test if quit is typed in console'''
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("quit"))
    
    def test_EOF(self):
        '''Test if EOF is typed in console'''
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("EOF"))
        
    
if __name__ == "__main__":
    unittest.main()