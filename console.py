#!/usr/bin/python3
"""Python module for console class."""
import cmd
from models import storage


class HBNBCommand(cmd.Cmd):
    """"
    command line interpreter class.
    """
    prompt = '(hbnb) '

    def do_quit(self, line):
        """
        Quit command to exit the program.
        """
        return True

    def do_EOF(self, line):
        """
        EOF command to exit the programm.
        """
        return True

    def emptyline(self):
        """
        empty line.
        """
        return

    def do_create(self, line):
        """
        Creates a new instance of BaseModel, saves it
        (to the JSON file) and prints the id.
        Ex: $ create BaseModel
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        str_classes = ['BaseModel', 'User', 'State', 'City',
                       'Amenity', 'Place', 'Review']
        classes = [BaseModel, User, State, City, Amenity,
                   Place, Review]
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        else:
            if args[0] in str_classes:
                class_idx = str_classes.index(args[0])
                obj = classes[class_idx]()
                obj.save()
                print(obj.id)
            else:
                print("** class doesn't exist **")

    def do_show(self, line):
        """
        Prints the string representation of an
        instance based on the class name and id.
        Ex: $ show BaseModel 1234-1234-1234
        """
        classes = ['BaseModel', 'User', 'State', 'City',
                   'Amenity', 'Place', 'Review']
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif len(args) == 1:
            if args[0] not in classes:
                print("** class doesn't exist **")
            else:
                print("** instance id missing **")
        elif len(args) > 1:
            if args[0] not in classes:
                print("** class doesn't exist **")
            else:
                objects = storage.all()
                key = args[0] + '.' + args[1]
                if key not in objects.keys():
                    print("** no instance found **")
                else:
                    print(objects[key])

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name
        and id (save the change into the JSON file).
        Ex: $ destroy BaseModel 1234-1234-1234.
        """
        classes = ['BaseModel', 'User', 'State', 'City',
                   'Amenity', 'Place', 'Review']
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif len(args) == 1:
            if args[0] not in classes:
                print("** class doesn't exist **")
            else:
                print("** instance id missing **")
        elif len(args) > 1:
            if args[0] not in classes:
                print("** class doesn't exist **")
            else:
                objects = storage.all()
                key = args[0] + '.' + args[1]
                if key not in objects.keys():
                    print("** no instance found **")
                else:
                    del objects[key]
                    storage.save()

    def do_all(self, line):
        """
        Prints all string representation of all
        instances based or not on the class name.
        Ex: $ all BaseModel or $ all.
        """
        classes = ['BaseModel', 'User', 'State', 'City',
                   'Amenity', 'Place', 'Review']
        args = line.split()
        objects = storage.all()
        list = []
        if len(args) == 0:
            for key in objects.keys():
                list.append(objects[key].__str__())
        else:
            if args[0] not in classes:
                print("** class doesn't exist **")
                return
            for key in objects.keys():
                obj_class = key.split('.')[0]
                if args[0] == obj_class:
                    list.append(objects[key].__str__())
        print(list)

    def do_update(self, line):
        """
        Updates an instance based on the class name and
        id by adding or updating attribute (save the change
        into the JSON file).
        Ex: $ update BaseModel 1234-1234-1234
        email "aibnb@holbertonschool.com".
        """
        classes = ['BaseModel', 'User', 'State', 'City',
                   'Amenity', 'Place', 'Review']
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif len(args) == 1:
            if args[0] not in classes:
                print("** class doesn't exist **")
            else:
                print("** instance id missing **")
        elif len(args) == 2:
            if args[0] not in classes:
                print("** class doesn't exist **")
            else:
                objects = storage.all()
                key = args[0] + '.' + args[1]
                if key not in objects.keys():
                    print("** no instance found **")
                else:
                    print("** attribute name missing **")
        elif len(args) == 3:
            if args[0] not in classes:
                print("** class doesn't exist **")
            else:
                objects = storage.all()
                key = args[0] + '.' + args[1]
                if key not in objects.keys():
                    print("** no instance found **")
                else:
                    print("** value missing **")
        else:
            if args[0] not in classes:
                print("** class doesn't exist **")
            else:
                objects = storage.all()
                key = args[0] + '.' + args[1]
                if key not in objects.keys():
                    print("** no instance found **")
                else:
                    i = 0
                    while line[i] != '"':
                        i += 1
                    str_val = line[i + 1:].split('"')[0]
                    if str_val == '"':
                        str_val = ""
                    value = HBNBCommand.cast_value(str_val)
                    setattr(objects[key], args[2], value)
                    objects[key].save()

    @staticmethod
    def cast_value(val):
        """Cast string to integer or float if possible."""
        if '.' in val:
            try:
                val = float(val)
            except:
                pass
        else:
            try:
                val = int(val)
            except:
                pass

        return val

if __name__ == '__main__':
    HBNBCommand().cmdloop()
