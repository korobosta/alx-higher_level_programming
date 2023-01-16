#!/usr/bin/python3
"""This module constains a class that test square class.
"""
import io
import pep8
import unittest
from models.base import Base
from models.square import Square
from contextlib import redirect_stdout as out


class TestSquare(unittest.TestCase):
    """Tester class.
    """

    def setUp(self):
        """Sets nb_objects to 0 for each test.
        """
        Base._Base__nb_objects = 0

    def test_style_base(self):
        """test pep8
        """
        style = pep8.StyleGuide()
        m = style.check_files(["models/square.py"])
        self.assertEqual(m.total_errors, 0, "fix pep8")

    def test_docstring(self):
        """Test doc strings.
        """
        self.assertIsNotNone(Square.__doc__)
        self.assertIsNotNone(Square.__init__.__doc__)
        self.assertIsNotNone(Square.size.__doc__)
        self.assertIsNotNone(Square.__str__.__doc__)
        self.assertIsNotNone(Square.update.__doc__)
        self.assertIsNotNone(Square.to_dictionary.__doc__)

    def test_attributes(self):
        """Test the Square basic attributes.
        """
        sqa = Square(1, 2, 3, 4)
        self.assertEqual(sqa.size, 1)
        self.assertEqual(sqa.x, 2)
        self.assertEqual(sqa.y, 3)
        self.assertEqual(sqa.id, 4)
        sqa2 = Square(2, 2, 3, 6)
        self.assertEqual(sqa2.size, 2)
        self.assertEqual(sqa2.x, 2)
        self.assertEqual(sqa2.y, 3)
        self.assertEqual(sqa2.id, 6)

    def test_id(self):
        """Test id attribute.
        """
        Square(1, 1)
        sqa3 = Square(1, 1)
        sqa4 = Square(1, 1, 1, 4)
        self.assertEqual(sqa3.id, 2)
        self.assertEqual(sqa4.id, 4)

    def test_size_int(self):
        """Test size with negative integer.
        """
        with self.assertRaises(ValueError) as error:
            Square(-2, 1)
        self.assertEqual("width must be > 0", str(error.exception))

    def test_size_none(self):
        """Test size with none value.
        """
        with self.assertRaises(TypeError) as error:
            Square(None, 1)
        self.assertEqual("width must be an integer", str(error.exception))

    def test_size_float(self):
        """Test size with float value.
        """
        with self.assertRaises(TypeError) as error:
            Square(3.1416, 1)
        self.assertEqual("width must be an integer", str(error.exception))

    def test_size_boolean(self):
        """Test size with boolean value.
        """
        with self.assertRaises(TypeError) as error:
            Square(True, 1)
        self.assertEqual("width must be an integer", str(error.exception))

    def test_size_str(self):
        """Test size with string value.
        """
        with self.assertRaises(TypeError) as error:
            Square("i'm a error >:O", 1)
        self.assertEqual("width must be an integer", str(error.exception))

    def test_size_list(self):
        """Test size with list value.
        """
        with self.assertRaises(TypeError) as error:
            Square(["i", "m", "a", "bad", "guy", "duh"], 1)
        self.assertEqual("width must be an integer", str(error.exception))

    def test_size_tuple(self):
        """Test size with tuple value.
        """
        with self.assertRaises(TypeError) as error:
            Square((1, 0, 0, 1, 1), 1)
        self.assertEqual("width must be an integer", str(error.exception))

    def test_size_dict(self):
        """Test size with dictionary value.
        """
        with self.assertRaises(TypeError) as error:
            Square({"Tyler": "The creator", "A$AP": "Rocky"}, 1)
        self.assertEqual("width must be an integer", str(error.exception))

    def test_size_set(self):
        """Test size with set value.
        """
        with self.assertRaises(TypeError) as error:
            Square({"i'm", "a", "set"}, 1)
        self.assertEqual("width must be an integer", str(error.exception))

    def test_x_int(self):
        """Test x with negative integer.
        """
        with self.assertRaises(ValueError) as error:
            Square(1, -2)
        self.assertEqual("x must be >= 0", str(error.exception))

    def test_x_none(self):
        """Test x with none value.
        """
        with self.assertRaises(TypeError) as error:
            Square(1, None)
        self.assertEqual("x must be an integer", str(error.exception))

    def test_x_float(self):
        """Test x with float value.
        """
        with self.assertRaises(TypeError) as error:
            Square(1, 3.1416)
        self.assertEqual("x must be an integer", str(error.exception))

    def test_x_boolean(self):
        """Test x with boolean value.
        """
        with self.assertRaises(TypeError) as error:
            Square(1, True)
        self.assertEqual("x must be an integer", str(error.exception))

    def test_x_str(self):
        """Test x with string value.
        """
        with self.assertRaises(TypeError) as error:
            Square(1, "i'm a error >:O")
        self.assertEqual("x must be an integer", str(error.exception))

    def test_x_list(self):
        """Test x with list value.
        """
        with self.assertRaises(TypeError) as error:
            Square(1, ["i", "m", "a", "bad", "guy", "duh"])
        self.assertEqual("x must be an integer", str(error.exception))

    def test_x_tuple(self):
        """Test x with tuple value.
        """
        with self.assertRaises(TypeError) as error:
            Square(1, (1, 0, 0, 1, 1))
        self.assertEqual("x must be an integer", str(error.exception))

    def test_x_dict(self):
        """Test x with dictionay value.
        """
        with self.assertRaises(TypeError) as error:
            Square(1, {"Tyler": "The creator", "A$AP": "Rocky"})
        self.assertEqual("x must be an integer", str(error.exception))

    def test_x_set(self):
        """Test x with set value.
        """
        with self.assertRaises(TypeError) as error:
            Square(1, {"i'm", "a", "set"})
        self.assertEqual("x must be an integer", str(error.exception))

    def test_y_int(self):
        """Test y with negative integer.
        """
        with self.assertRaises(ValueError) as error:
            Square(1, 1, -2)
        self.assertEqual("y must be >= 0", str(error.exception))

    def test_y_none(self):
        """Test y with none value.
        """
        with self.assertRaises(TypeError) as error:
            Square(1, 1, None)
        self.assertEqual("y must be an integer", str(error.exception))

    def test_y_float(self):
        """Test y with float value.
        """
        with self.assertRaises(TypeError) as error:
            Square(1, 1, 3.1416)
        self.assertEqual("y must be an integer", str(error.exception))

    def test_y_boolean(self):
        """Test y with boolean value.
        """
        with self.assertRaises(TypeError) as error:
            Square(1, 1, True)
        self.assertEqual("y must be an integer", str(error.exception))

    def test_y_str(self):
        """Test y with string value.
        """
        with self.assertRaises(TypeError) as error:
            Square(1, 1, "i'm a error >:O")
        self.assertEqual("y must be an integer", str(error.exception))

    def test_y_list(self):
        """Test y with list value.
        """
        with self.assertRaises(TypeError) as error:
            Square(1, 1, ["i", "m", "a", "bad", "guy", "duh"])
        self.assertEqual("y must be an integer", str(error.exception))

    def test_y_tuple(self):
        """Test y with tuple value.
        """
        with self.assertRaises(TypeError) as error:
            Square(1, 1, (1, 0, 0, 1, 1))
        self.assertEqual("y must be an integer", str(error.exception))

    def test_y_dict(self):
        """Test y with dictionay value.
        """
        with self.assertRaises(TypeError) as error:
            Square(1, 1, {"Tyler": "The creator", "A$AP": "Rocky"})
        self.assertEqual("y must be an integer", str(error.exception))

    def test_y_set(self):
        """Test y with set value.
        """
        with self.assertRaises(TypeError) as error:
            Square(1, 1, {"i'm", "a", "set"})
        self.assertEqual("y must be an integer", str(error.exception))

    def test_display(self):
        """Test Square display.
        """
        with io.StringIO() as buff, out(buff):
            sqa5 = Square(6)
            sqa5.display()
            expected_display = "######\n" * 6
            self.assertEqual(buff.getvalue(), expected_display)
        with io.StringIO() as buff, out(buff):
            sqa5 = Square(1)
            sqa5.display()
            expected_display = "#\n"
            self.assertEqual(buff.getvalue(), expected_display)
        with io.StringIO() as buff, out(buff):
            sqa6 = Square(3, 1, 3, 3)
            sqa6.display()
            expected_display = "\n"*3 + " ###\n"*3
            self.assertEqual(buff.getvalue(), expected_display)

    def test_str(self):
        """Test Square str.
        """
        sqa7 = Square(32, 2, 2, 1)
        self.assertEqual(str(sqa7), "[Square] (1) 2/2 - 32")
        sqa8 = Square(1, 1)
        self.assertEqual(str(sqa8), "[Square] (1) 1/0 - 1")
        sqa9 = Square(3, 1, 3, 3)
        self.assertEqual(str(sqa9), "[Square] (3) 1/3 - 3")

    def test_update_args(self):
        """Test Square update (args).
        """
        sqa10 = Square(1, 2, 3, 4)
        sqa10.update(100, 20, 23)
        self.assertEqual(sqa10.id, 100)
        self.assertEqual(sqa10.size, 20)
        self.assertEqual(sqa10.x, 23)
        self.assertEqual(sqa10.y, 3)

    def test_update_kwargs(self):
        """Test Square update (kwargs).
        """
        sqa11 = Square(1, 2, 3, 4)
        sqa11.update(id=34, x=0, size=23)
        self.assertEqual(sqa11.id, 34)
        self.assertEqual(sqa11.size, 23)
        self.assertEqual(sqa11.x, 0)
        self.assertEqual(sqa11.y, 3)

    def test_update_args_kwargs(self):
        """Test Square update (args/kwargs).
        """
        sqa12 = Square(1, 2, 3, 4)
        sqa12.update(100, 20, size=69)
        self.assertEqual(sqa12.id, 100)
        self.assertEqual(sqa12.size, 20)
        self.assertEqual(sqa12.x, 2)
        self.assertEqual(sqa12.y, 3)

    def test_to_dictionay(self):
        """Test Square to_dictionary method.
        """
        sqa13 = Square(1, 1, 1, 1)
        dictionary = sqa13.to_dictionary()
        self.assertEqual(type(dictionary), type({}))
        self.assertEqual("id" in dictionary, True)
        self.assertEqual("size" in dictionary, True)
        self.assertEqual("x" in dictionary, True)
        self.assertEqual("y" in dictionary, True)


if __name__ == "__main__":
    unittest.main()
