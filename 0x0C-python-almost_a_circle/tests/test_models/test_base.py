#!/usr/bin/python3
"""This module contains a class that test
    all functionality of the Base model.
"""
import unittest
import pep8
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    """Base class tests.
    """
    def setUp(self):
        """sets nb_objects to 0.
        """
        Base._Base__nb_objects = 0

    def test_style_base(self):
        """test pep8
        """
        style = pep8.StyleGuide()
        m = style.check_files(["models/base.py"])
        self.assertEqual(m.total_errors, 0, "fix pep8")

    def test_docstring(self):
        """Test doc strings.
        """
        self.assertIsNotNone(Base.__doc__)
        self.assertIsNotNone(Base.__init__.__doc__)
        self.assertIsNotNone(Base.to_json_string.__doc__)
        self.assertIsNotNone(Base.save_to_file.__doc__)
        self.assertIsNotNone(Base.from_json_string.__doc__)
        self.assertIsNotNone(Base.create.__doc__)
        self.assertIsNotNone(Base.load_from_file.__doc__)

    def test_void_none(self):
        """Test with none value.
        """
        base = Base(None)
        self.assertEqual(base.id, 1)
        base = Base()
        self.assertEqual(base.id, 2)
        base = Base(3)
        self.assertEqual(base.id, 3)
        base = Base()
        self.assertEqual(base.id, 3)

    def test_int(self):
        """Test id attribute (int).
        """
        base = Base(-4)
        self.assertEqual(base.id, -4)
        base = Base()
        self.assertEqual(base.id, 1)

    def test_float(self):
        """Test id attribute (float).
        """
        base = Base(1.34)
        self.assertEqual(base.id, 1.34)

    def test_boolean(self):
        """Test id attribute (boolean).
        """
        base = Base(False)
        self.assertEqual(base.id, False)

    def test_string(self):
        """Test id attribute (str).
        """
        base = Base("a")
        self.assertEqual(base.id, "a")

    def test_tuple(self):
        """Test id attribute (tuple).
        """
        base = Base(())
        self.assertEqual(base.id, ())

    def test_list(self):
        """Test id attribute (list).
        """
        base = Base([])
        self.assertEqual(base.id, [])

    def test_dict(self):
        """Test id attribute (dict).
        """
        base = Base({})
        self.assertEqual(base.id, {})

    def test_set(self):
        """Test id attribute (set).
        """
        base = Base({1})
        self.assertEqual(base.id, {1})

    def test_toJson(self):
        """Tests transformation to a JSON
        """
        rec = Rectangle(10, 7, 2, 8)
        dictionary = rec.to_dictionary()
        json = Base.to_json_string([dictionary])
        self.assertEqual(type(json) is str and
                         "id" in json and
                         "width" in json and
                         "height" in json and
                         "x" in json and
                         "y" in json, True)
        sqa = Square(10, 7, 2)
        dictionary = sqa.to_dictionary()
        json = Base.to_json_string([dictionary])
        self.assertEqual(type(json) is str and
                         "id" in json and
                         "size" in json and
                         "x" in json and
                         "y" in json, True)

    def test_toFile(self):
        """Tests to test save
        """
        r = Rectangle(2, 4)
        Rectangle.save_to_file([r])
        a = 0
        with open("Rectangle.json", "r"):
            a = 1
        self.assertEqual(a == 1, True)

    def test_fromJson(self):
        """Test to test from JSON
        """
        st = '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]'
        dic = Base.from_json_string(st)
        self.assertEqual(dic,
                         [{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}])

    def test_create(self):
        """Tests to test create
        """
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r1) == str(r2), True)

    def test_loadFrom(self):
        """This tests loads
        """
        s = Square(7, 9, 1)
        list_squares_input = [s]
        Square.save_to_file(list_squares_input)
        li = Square.load_from_file()
        self.assertEqual(type(li) is list and
                         li[0].__class__.__name__ is "Square", True)


if __name__ == "__main__":
    unittest.main()
