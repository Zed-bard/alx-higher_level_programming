#!/usr/bin/python3

import json
import os
import csv
import turtle


class Base:
    """Represents the base class
    
    Attributes:
        __nb_objects (int): The count of Base objects created
    
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes a Base instance
        
        Args:
            id (int, optional): The id of the instance
        
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Converts a list of dictionaries to a JSON string representation
        
        Args:
            list_dictionaries (list): List of dictionaries
        
        Returns:
            str: JSON string representation of the list of dictionaries
        
        """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file
        
        Args:
            list_objs (list): List of instances
        
        """
        if list_objs is None:
            with open(cls.__name__ + ".json", "w") as file:
                file.write("[]")
        else:
            list_instance = [i.to_dictionary() for i in list_objs]
            with open(cls.__name__ + ".json", "w") as file:
                file.write(cls.to_json_string(list_instance))

    @staticmethod
    def from_json_string(json_string):
        """Converts a JSON string representation to a list of dictionaries
        
        Args:
            json_string (str): JSON string
        
        Returns:
            list: List of dictionaries
        
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Creates an instance with attributes already set
        
        Args:
            **dictionary (dict): Dictionary of attribute values
        
        Returns:
            Base: Instance with attributes set
        
        """
        if cls.__name__ == "Rectangle":
            result = cls(32, 3)
        elif cls.__name__ == "Square":
            result = cls(32)
        result.update(**dictionary)
        return result

    @classmethod
    def load_from_file(cls):
        """Loads instances from a file
        
        Returns:
            list: List of instances
        
        """
        list_instance = []
        file_name = cls.__name__ + ".json"
        if os.path.isfile(file_name):
            with open(file_name, "r") as file:
                json_data = file.read()
            dict_data = cls.from_json_string(json_data)
            for i in dict_data:
                list_instance.append(cls.create(**i))
        return list_instance

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes and deserializes instances to/from a CSV file
        
        Args:
            list_objs (list): List of instances
        
        """
        if (list_objs is None or not isinstance(list_objs, list)
                or not all(isinstance(j, Base) for j in list_objs)):
            with open(cls.__name__ + ".csv", "w") as file:
                file.write("[]")
        elif any(isinstance(j, Base) for j in list_objs):
            dict_data = [i.to_dictionary() for i in list_objs]
            if cls.__name__ == "Rectangle":
                csv_columns = ["id", "width", "height", "x", "y"]
            else:
                csv_columns = ["id", "size", "x", "y"]
            with open(cls.__name__ + ".csv", "w") as file:
                writer = csv.DictWriter(file, fieldnames=csv_columns)
                writer.writeheader()
                writer.writerows(dict_data)

    @classmethod
    def load_from_file_csv(cls):
        """Loads instances from a CSV file
        
        Returns:
            list: List of instances
        
        """
        list_instance = []
        file_name = cls.__name__ + ".csv"
        if os.path.isfile(file_name):
            with open(file_name, "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    d = {key: int(value) for key, value in row.items()}
                    list_instance.append(cls.create(**d))
        return list_instance

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draws squares and rectangles using Turtle graphics
        
        Args:
            list_rectangles (list): List of Rectangle instances
            list_squares (list): List of Square instances
        
        """
        turtle.bgcolor("black")
        for i in list_rectangles + list_squares:
            tt = turtle.Turtle()
            tt.shape("turtle")
            tt.fillcolor("white")
            tt.pen(fillcolor="white", pencolor="red", pensize=2)
            tt.begin_fill()
            for _ in range(2):
                tt.forward(i.width)
                tt.right(90)
                tt.forward(i.height)
                tt.right(90)
            tt.end_fill()
        turtle.done()
