#!/usr/bin/python3
""" Module containing the HBNBCommand class, a command interpreter."""
import cmd
import shlex
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    """ Command interpreter for HBNB project."""
    prompt = "(hbnb) "
    valid_instances = ["BaseModel"]

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
    def do_create(self, arg):
        """ Creates a new instance of BaseModel,
            saves it (to the JSON file) and prints the id.
        """
        command_args = shlex.split(arg)
        if len(command_args) == 0:
            print("**class name missing**")
        elif command_args[0] not in self.valid_instances:
            print("** class doesn't exist **")
        else:
            new_inst = BaseModel()
            new_inst.save()
            print(new_inst.id)

    def do_show(self, arg):
        """ Prints the string representation of an instance based             class name and id.
        """
        command_args = shlex.split(arg)
        if len(command_args) == 0:
            print("** class name missing **")
        elif command_args[0] not in valid_instances:
            print("** class doesn't exist **")
        elif len(command_args) < 2:
            print("** instance id missing **")
        else:
            obj = storage.all()
            key = "{}.{}".format(command_args[0], command_args[1])
            if key in obj:
                print(obj[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
