#!/usr/bin/python3
""" Provide a Base class for all others classes """


import json

class Base():
    """ Base class for all others classes """
    HEADERS = ('id',)

    __nb_objects = 0

    def __init__(self, id=None):
        """ Instantiate a base class """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return a JSON representation a list of dictionaries
        """
        if list_dictionaries is None:
            return '[]'
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Return the list defined by a JSON string
        """
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def load_from_file(cls):
        """Load the objects defined in the JSON file <class-name>.json
        """
        try:
            with open("{}.json".format(cls.__name__), 'r') as ifile:
                return [cls.create(**obj)
                        for obj in cls.from_json_string(ifile.read())]
        except FileNotFoundError:
            return []

    @classmethod
    def load_from_file_csv(cls):
        """Save a CSV representation of list_objs to <class_name>.json
        """
        try:
            with open("{}.csv".format(cls.__name__), 'r') as ifile:
                return [cls.create(
                    **{k: int(v) for k, v in zip(cls.HEADERS, line.split(','))}
                ) for line in ifile.readlines()]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file(cls, list_objs):
        """Save a JSON representation of list_objs to <class-name>.json
        """
        with open("{}.json".format(cls.__name__), 'w') as ofile:
            if list_objs:
                ofile.write(cls.to_json_string(
                    [obj.to_dictionary() for obj in list_objs]
                ))
            else:
                ofile.write("[]")

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Save a CSV representation of list_objs to <class-name>.json
        """
        with open("{}.csv".format(cls.__name__), 'w') as ofile:
            if list_objs:
                for obj in list_objs:
                    obj = obj.to_dictionary()
                    ofile.write(
                        ','.join(str(obj[key]) for key in cls.HEADERS) + '\n'
                    )

    @classmethod
    def create(cls, **dictionary):
        """Return a new instance of cls with its attributes set
        """
        args = []
        while True:
            try:
                obj = cls(*args)
            except TypeError:
                args.append(1)
            else:
                break
        obj.update(**dictionary)
        return obj

    def update(self, *args, **kwargs):
        """Update the attributes of a base object
        """
        if args:
            for pair in zip(self.HEADERS, args):
                setattr(self, *pair)
        else:
            for key in kwargs:
                if key in self.HEADERS:
                    setattr(self, key, kwargs[key])
