#!/usr/bin/python3
""" A program that contains the entry point of the command interpreter"""
import cmd


class HBNBCommand(cmd.Cmd):
    """A base class for the console"""
    prompt = '(hbnb)'

    def do_quit(self, arg):
        """Method to quit the program"""
        return True

    def do_eof(self, arg):
        """Method to exit the program"""
        print()
        return True

    def emptyline(self):
        """execute nothingupon empty input"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
