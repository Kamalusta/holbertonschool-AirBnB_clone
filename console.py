#!/usr/bin/python3
'''doc'''
import cmd, sys


class HBNBCommand(cmd.Cmd):
    '''doc'''
    prompt = '(hbnb)'
    
    def do_quit(self, arg):
        'Quit command to exit the program'
        return True

    def do_EOF(self, arg):
        'Quit command to exit the program'
        return True

    def emptyline(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
