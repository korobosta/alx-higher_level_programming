#!/usr/bin/python3
"""this module contains a class Base.
"""
import json
import turtle
import time
import csv


class Base:
    """Class Base that sets the instance id.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor that sets the instance id.

        Args:
            id (Int, None): id value. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries.

        Args:
            list_dictionaries (list): list of dictionaries

        Returns:
            json str: JSON string representation of list_dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) < 1:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): A list of instances who inherits of Base.
        """
        li = []
        filename = "{}.json".format(cls.__name__)
        if list_objs is not None:
            for obj in list_objs:
                li.append(obj.to_dictionary())
        with open(filename, mode="w", encoding="utf-8") as file:
            file.write(cls.to_json_string(li))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string.

        Args:
            json_string (str): a string representing a list of dictionaries.

        Returns:
            [type]: the list represented by json_string.
        """
        if json_string is None or len(json_string) < 1:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set.

        Returns:
            obj: instance with all new attributes.
        """
        if cls.__name__ == "Rectangle":
            new = cls(1, 1)
            new.update(**dictionary)
            return new
        elif cls.__name__ == "Square":
            new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances.

        Returns:
            list: list of instances.
        """
        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename, mode="r", encoding="utf-8") as file:
                pylist = cls.from_json_string(file.read())
        except Exception:
            return []
        return [cls.create(**i) for i in pylist]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Writes the csv string representation of list_objs to a file.

        Args:
            list_objs (list): A list of instances who inherits of Base.
        """
        li = []
        filename = "{}.csv".format(cls.__name__)
        if list_objs is not None:
            for obj in list_objs:
                li.append(obj.to_dictionary())
        with open(filename, mode="w", encoding="utf-8") as file:
            csvfile = csv.writer(file)
            for i in li:
                a = []
                if cls.__name__ == "Rectangle":
                    menu = ["id", "width", "height", "x", "y"]
                    for x in menu:
                        a.append(i[x])
                elif cls.__name__ == "Square":
                    menu = ["id", "size", "x", "y"]
                    for x in menu:
                        a.append(i[x])
                csvfile.writerow(a)

    @classmethod
    def load_from_file_csv(cls):
        """Returns a list of instances.

        Returns:
            list: list of instances.
        """
        filename = "{}.csv".format(cls.__name__)
        try:
            with open(filename, mode="r", encoding="utf-8") as file:
                reader = list(csv.reader(file, delimiter=','))
                if cls.__name__ == "Rectangle":
                    menu = ["id", "width", "height", "x", "y"]
                    lista = []
                    for i in reader:
                        newdict = {}
                        for idx, x in enumerate(menu):
                            newdict[x] = int(i[idx])
                        lista.append(newdict)
                    return [cls.create(**i) for i in lista]
                elif cls.__name__ == "Square":
                    menu = ["id", "size", "x", "y"]
                    lista = []
                    for i in reader:
                        newdict = {}
                        for idx, x in enumerate(menu):
                            newdict[x] = int(i[idx])
                        lista.append(newdict)
                    return [cls.create(**i) for i in lista]
        except Exception:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw all rectangles and squares

        Args:
            list_rectangles (list): list of rectangles.
            list_squares (list): list of squares.
        """
        t = turtle.Turtle()
        style = ("Arial", 15, 'normal', 'bold')
        s2 = ("Arial", 5, 'normal')
        t.speed(200)
        for i in list_rectangles:
            if "rectangle" in str(type(i)):
                t.shape("circle")
                t.shapesize(0.3, 0.01, 0.2)
                t.penup()
                t.setposition(0, 280)
                t.color('#4a661a')
                t.write("[Type] (Id) X/Y - Wi/He", font=style, align="center")
                t.setposition(0, 250)
                t.write(i, font=style, align="center")
                x = i.x
                y = i.y
                h = i.height
                w = i.width
                t.color('black')
                t.setposition(x, y)
                t.speed(3)
                t.pendown()
                t.fillcolor("#4a661a")
                t.begin_fill()
                for j in range(2):
                    t.forward(w)
                    t.left(90)
                    t.forward(h)
                    t.left(90)
                t.end_fill()
                t.penup()
                t.goto(0, 0)
                t.pendown()
                t.speed(200)
                for x in range(4):
                    c = 0
                    for j in range(10):
                        t.write(str(c), align="center", font=s2)
                        if x == 3 or x == 2:
                            c -= 20
                        else:
                            c += 20
                        t.stamp()
                        t.forward(20)
                    t.goto(0, 0)
                    t.left(90)
                time.sleep(3)
                turtle.resetscreen()
        for i in list_squares:
            if "square" in str(type(i)):
                t.shape("circle")
                t.shapesize(0.3, 0.01, 0.2)
                t.penup()
                t.setposition(0, 280)
                t.color('#c75038')
                t.write("[Type] (Id) X/Y - Wi/He", font=style, align="center")
                t.setposition(0, 250)
                t.write(i, font=style, align="center")
                t.penup()
                s = i.size
                x = i.x
                y = i.y
                t.color('black')
                t.setposition(x, y)
                t.speed(3)
                t.pendown()
                t.fillcolor("#c75038")
                t.begin_fill()
                for j in range(4):
                    t.forward(s)
                    t.left(90)
                t.end_fill()
                t.penup()
                t.goto(0, 0)
                t.pendown()
                t.speed(200)
                for x in range(4):
                    c = 0
                    for j in range(10):
                        t.write(str(c), align="center", font=s2)
                        if x == 3 or x == 2:
                            c -= 20
                        else:
                            c += 20
                        t.stamp()
                        t.forward(20)
                    t.goto(0, 0)
                    t.left(90)
                time.sleep(3)
                turtle.resetscreen()
