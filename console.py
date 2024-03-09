#!/usr/bin/python3
""" Module containing the HBNBCommand class, a command interpreter."""
import cmd


class HBNBCommand(cmd.Cmd):
    """ Command interpreter for HBNB project."""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """ Quit command to exit the program."""
        return True

    def help_quit(self):
        """ Displays help message for quit command."""
        print("Quit command to exit the program")

    def do_EOF(self, arg):
        """ EOF command to exit the program."""
        print()
        return True

    def emptyline(self):
        """ Executes nothing."""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
