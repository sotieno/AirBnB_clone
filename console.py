#!/usr/bin/python3
"""Entry point of the command interpreter"""
import cmd
from models import storage

"""
global CLASSES list
"""
ClASSES = ["BaseModel", "User", "City", "Place", "State", "Amenity", "Review"]


class HBNBCommand(cmd.Cmd):
    """
    Defines the HBNB Command interpreter

    Attr:
        prompt(str): the command prompt
    """
    prompt = "(hbnb)"

    def default(self, arg):
        """
        default method for the following commands
        do_all = self.all()
        do_create = self.create()
        do_show = self.show()
        do_destroy = self.destroy()
        do_update = self.update()
        do_count = self.count()
        """
        if "." not in arg or "(" not in arg or len(arg) < 10:
            print("** command not found **")
            return

        args = arg.split(".")
        brace_idx = args[1].index('(')
        cmds = args[1][:brace_idx]
        arg = args[1].split("(")
        arg = arg[1][:-1]
        arg_line = arg.split(", ")
        argv = ""

        if len(arg_line) != 0:
            for a in arg_line:
                if not a.isdigit():
                    a = a[1:-1]
                argv += a + " "

        if cmds == "count":
            self.count(args[0] + " " + argv)
            return

        eval("self.do_" + cmds)(args[0] + " " + argv)

    def do_all(self, arg):
        """
        Prints all string representation of all
        instances based or not on the class name
        Eg: $ all BaseModel or $ all
        """
        instances = storage.all().copy()
        str_all = []
        args = list(arg.split())

        if len(args) == 0:
            for a_class, info in instances.items():
                inst = eval(info['__class__'])(**info)
                str_all.append(inst.__str__())
        else:
            if args[0] not in ClASSES:
                print("** class doesn't exist **")
                return
            else:
                for a_class, info in instances.items():
                    if info['__class__'] == args[0]:
                        inst = eval(args[0])(**info)
                        str_all.append(inst.__str__())
        print(str_all)

    def do_quit(self, arg):
        """
        command  executed to exit the console
        """
        return True

    def do_EOF(self, arg):
        """
        EOF signal to exit the program
        """
        print("")
        return True

    def emptyline(self):
        """
        command to be executed when empty line + <ENTER> key passed
        """
        pass

    def check_id(id):
        """
        Checks for id
        """
        current_inst = storage.all()

        for keys, values in current_inst.items():
            if values['id'] == id:
                return False
        return True

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves (to JSON file)
        and prints the id
        Eg: $ create BaseModel
        """
        args = list(arg.split())

        if len(args) == 0:
            print("** class name missing **")
            return
        elif args[0] not in ClASSES:
            print("** class doesn't exist **")
            return
        inst = eval(args[0])()
        inst.save()
        print(inst.id)

    def do_show(self, arg):
        """
        Prints the string representaion of an instance based on the
        class name and id.
        Eg: $ show BaseModel 1234-1234-1234.
        """
        args = list(arg.split())
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in ClASSES:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
            return
        key = args[0] + '.' + args[1]
        if key not in storage.all():
            print("** no instance found **")
        elif HBNBCommand.check_id(args[1]):
            print("** no instance found **")
        else:
            key = args[0] + '.' + args[1]
            instances = storage.all().copy()
            inst = eval(args[0])(**instances[key])
            print(inst)

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file).
        eg: $ destroy BaseModel 1234-1234-1234.
        """
        args = list(arg.split())
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in ClASSES:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif HBNBCommand.check_id(args[1]):
            print("** no instance found **")
        else:
            key = args[0] + '.' + args[1]
            del storage.all()[key]
            storage.save()

    def do_update(self, arg):
        """
        Update a class instance of a given id by addn or updatn a attr dict[]
        (save the change into the JSON file).
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com".
        """
        args = list(arg.split())
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in ClASSES:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif HBNBCommand.check_id(args[1]):
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            key = args[0] + '.' + args[1]
            value = args[3]
            if value[0] == '"' and value[-1] == '"':
                value = value[1:-1]
            if value.isdigit():
                value = int(value)
            storage.all()[key][args[2]] = value
            instance = storage.all()[key]
            inst = eval(args[0])(**instance)
            inst.save()
            storage.all()[key]['updated_at'] = inst.updated_at.isoformat()
            storage.save()

    def count(self, arg):
        """
        counts and the number of instances of a class.
        """
        instances = storage.all().copy()
        num_inst = 0
        args = list(arg.split())
        if len(args) == 0:
            print("** class name missing **")
        else:
            if args[0] not in ClASSES:
                print("** class doesn't exist **")
                return
            else:
                for a_class, info in instances.items():
                    if info['__class__'] == args[0]:
                        num_inst += 1
        print(num_inst)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
