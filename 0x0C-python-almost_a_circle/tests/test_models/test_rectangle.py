#!/usr/bin/python3
"""This module constains a class that test rectangle class.
"""
import io
import pep8
import unittest
from models.base import Base
from models.rectangle import Rectangle
from contextlib import redirect_stdout as out


class TestRectangle(unittest.TestCase):
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
        m = style.check_files(["models/rectangle.py"])
        self.assertEqual(m.total_errors, 0, "fix pep8")

    def test_docstring(self):
        """Test doc strings.
        """
        self.assertIsNotNone(Rectangle.__doc__)
        self.assertIsNotNone(Rectangle.__init__.__doc__)
        self.assertIsNotNone(Rectangle.width.__doc__)
        self.assertIsNotNone(Rectangle.height.__doc__)
        self.assertIsNotNone(Rectangle.x.__doc__)
        self.assertIsNotNone(Rectangle.y.__doc__)
        self.assertIsNotNone(Rectangle.area.__doc__)
        self.assertIsNotNone(Rectangle.display.__doc__)
        self.assertIsNotNone(Rectangle.update.__doc__)
        self.assertIsNotNone(Rectangle.to_dictionary.__doc__)
        self.assertIsNotNone(Rectangle.__str__.__doc__)

    def test_attributes(self):
        """Test the rectangle basic attributes.
        """
        rec = Rectangle(1, 1)
        self.assertEqual(rec.width, 1)
        self.assertEqual(rec.height, 1)
        self.assertEqual(rec.x, 0)
        self.assertEqual(rec.y, 0)
        self.assertEqual(rec.id, 1)
        rec = Rectangle(1, 8, 0, 3, 3)
        self.assertEqual(rec.width, 1)
        self.assertEqual(rec.height, 8)
        self.assertEqual(rec.x, 0)
        self.assertEqual(rec.y, 3)
        self.assertEqual(rec.id, 3)

    def test_id(self):
        """Test id attribute.
        """
        Rectangle(1, 1)
        rec2 = Rectangle(1, 1)
        rec3 = Rectangle(1, 1, 1, 1, 4)
        self.assertEqual(rec2.id, 2)
        self.assertEqual(rec3.id, 4)

    def test_width_int(self):
        """Test width with negative integer.
        """
        with self.assertRaises(ValueError) as error:
            Rectangle(-2, 1)
        self.assertEqual("width must be > 0", str(error.exception))

    def test_width_none(self):
        """Test width with none value.
        """
        with self.assertRaises(TypeError) as error:
            Rectangle(None, 1)
        self.assertEqual("width must be an integer", str(error.exception))

    def test_width_float(self):
        """Test width with float value.
        """
        with self.assertRaises(TypeError) as error:
            Rectangle(3.1416, 1)
        self.assertEqual("width must be an integer", str(error.exception))

    def test_width_boolean(self):
        """Test width with boolean value.
        """
        with self.assertRaises(TypeError) as error:
            Rectangle(True, 1)
        self.assertEqual("width must be an integer", str(error.exception))

    def test_width_str(self):
        """Test width with string value.
        """
        with self.assertRaises(TypeError) as error:
            Rectangle("i'm a error >:O", 1)
        self.assertEqual("width must be an integer", str(error.exception))

    def test_width_list(self):
        """Test width with list value.
        """
        with self.assertRaises(TypeError) as error:
            Rectangle(["i", "m", "a", "bad", "guy", "duh"], 1)
        self.assertEqual("width must be an integer", str(error.exception))

    def test_width_tuple(self):
        """Test width with tuple value.
        """
        with self.assertRaises(TypeError) as error:
            Rectangle((1, 0, 0, 1, 1), 1)
        self.assertEqual("width must be an integer", str(error.exception))

    def test_width_dict(self):
        """Test width with dictionary value.
        """
        with self.assertRaises(TypeError) as error:
            Rectangle({"Tyler": "The creator", "A$AP": "Rocky"}, 1)
        self.assertEqual("width must be an integer", str(error.exception))

    def test_width_set(self):
        """Test width with set value.
        """
        with self.assertRaises(TypeError) as error:
            Rectangle({"i'm", "a", "set"}, 1)
        self.assertEqual("width must be an integer", str(error.exception))

    def test_height_int(self):
        """Test height with negative integer.
        """
        with self.assertRaises(ValueError) as error:
            Rectangle(1, -2)
        self.assertEqual("height must be > 0", str(error.exception))

    def test_height_none(self):
        """Test height with none value.
        """
        with self.assertRaises(TypeError) as error:
            Rectangle(1, None)
        self.assertEqual("height must be an integer", str(error.exception))

    def test_height_float(self):
        """Test height with float value.
        """
        with self.assertRaises(TypeError) as error:
            Rectangle(1, 3.1416)
        self.assertEqual("height must be an integer", str(error.exception))

    def test_height_boolean(self):
        """Test height with boolean value.
        """
        with self.assertRaises(TypeError) as error:
            Rectangle(1, True)
        self.assertEqual("height must be an integer", str(error.exception))

    def test_height_str(self):
        """Test height with string value.
        """
        with self.assertRaises(TypeError) as error:
            Rectangle(1, "i'm a error >:O")
        self.assertEqual("height must be an integer", str(error.exception))

    def test_height_list(self):
        """Test height with list value.
        """
        with self.assertRaises(TypeError) as error:
            Rectangle(1, ["i", "m", "a", "bad", "guy", "duh"])
        self.assertEqual("height must be an integer", str(error.exception))

    def test_height_tuple(self):
        """Test height with tuple value.
        """
        with self.assertRaises(TypeError) as error:
            Rectangle(1, (1, 0, 0, 1, 1))
        self.assertEqual("height must be an integer", str(error.exception))

    def test_height_dict(self):
        """Test height with dictionary value.
        """
        with self.assertRaises(TypeError) as error:
            Rectangle(1, {"Tyler": "The creator", "A$AP": "Rocky"})
        self.assertEqual("height must be an integer", str(error.exception))

    def test_height_set(self):
        """Test height with set value.
        """
        with self.assertRaises(TypeError) as error:
            Rectangle(1, {"i'm", "a", "set"})
        self.assertEqual("height must be an integer", str(error.exception))

    def test_x_int(self):
        """Test x with negative integer.
        """
        with self.assertRaises(ValueError) as error:
            Rectangle(1, 1, -2)
        self.assertEqual("x must be >= 0", str(error.exception))

    def test_x_none(self):
        """Test x with none value.
        """
        with self.assertRaises(TypeError) as error:
            Rectangle(1, 1, None)
        self.assertEqual("x must be an integer", str(error.exception))

    def test_x_float(self):
        """Test x with float value.
        """
        with self.assertRaises(TypeError) as error:
            Rectangle(1, 1, 3.1416)
        self.assertEqual("x must be an integer", str(error.exception))

    def test_x_boolean(self):
        """Test x with boolean value.
        """
        with self.assertRaises(TypeError) as error:
            Rectangle(1, 1, True)
        self.assertEqual("x must be an integer", str(error.exception))

    def test_x_str(self):
        """Test x with string value.
        """
        with self.assertRaises(TypeError) as error:
            Rectangle(1, 1, "i'm a error >:O")
        self.assertEqual("x must be an integer", str(error.exception))

    def test_x_list(self):
        """Test x with list value.
        """
        with self.assertRaises(TypeError) as error:
            Rectangle(1, 1, ["i", "m", "a", "bad", "guy", "duh"])
        self.assertEqual("x must be an integer", str(error.exception))

    def test_x_tuple(self):
        """Test x with tuple value.
        """
        with self.assertRaises(TypeError) as error:
            Rectangle(1, 1, (1, 0, 0, 1, 1))
        self.assertEqual("x must be an integer", str(error.exception))

    def test_x_dict(self):
        """Test x with dictionay value.
        """
        with self.assertRaises(TypeError) as error:
            Rectangle(1, 1, {"Tyler": "The creator", "A$AP": "Rocky"})
        self.assertEqual("x must be an integer", str(error.exception))

    def test_x_set(self):
        """Test x with set value.
        """
        with self.assertRaises(TypeError) as error:
            Rectangle(1, 1, {"i'm", "a", "set"})
        self.assertEqual("x must be an integer", str(error.exception))

    def test_y_int(self):
        """Test y with negative integer.
        """
        with self.assertRaises(ValueError) as error:
            Rectangle(1, 1, 1, -2)
        self.assertEqual("y must be >= 0", str(error.exception))

    def test_y_none(self):
        """Test y with none value.
        """
        with self.assertRaises(TypeError) as error:
            Rectangle(1, 1, 1, None)
        self.assertEqual("y must be an integer", str(error.exception))

    def test_y_float(self):
        """Test y with float value.
        """
        with self.assertRaises(TypeError) as error:
            Rectangle(1, 1, 1, 3.1416)
        self.assertEqual("y must be an integer", str(error.exception))

    def test_y_boolean(self):
        """Test y with boolean value.
        """
        with self.assertRaises(TypeError) as error:
            Rectangle(1, 1, 1, True)
        self.assertEqual("y must be an integer", str(error.exception))

    def test_y_str(self):
        """Test y with string value.
        """
        with self.assertRaises(TypeError) as error:
            Rectangle(1, 1, 1, "i'm a error >:O")
        self.assertEqual("y must be an integer", str(error.exception))

    def test_y_list(self):
        """Test y with list value.
        """
        with self.assertRaises(TypeError) as error:
            Rectangle(1, 1, 1, ["i", "m", "a", "bad", "guy", "duh"])
        self.assertEqual("y must be an integer", str(error.exception))

    def test_y_tuple(self):
        """Test y with tuple value.
        """
        with self.assertRaises(TypeError) as error:
            Rectangle(1, 1, 1, (1, 0, 0, 1, 1))
        self.assertEqual("y must be an integer", str(error.exception))

    def test_y_dict(self):
        """Test y with dictionay value.
        """
        with self.assertRaises(TypeError) as error:
            Rectangle(1, 1, 1, {"Tyler": "The creator", "A$AP": "Rocky"})
        self.assertEqual("y must be an integer", str(error.exception))

    def test_y_set(self):
        """Test y with set value.
        """
        with self.assertRaises(TypeError) as error:
            Rectangle(1, 1, 1, {"i'm", "a", "set"})
        self.assertEqual("y must be an integer", str(error.exception))

    def test_area(self):
        """Test rectangle area.
        """
        rect4 = Rectangle(34623, 12312)
        self.assertEqual(rect4.area(), 426278376)

    def test_display(self):
        """Test rectangle display.
        """
        with io.StringIO() as buff, out(buff):
            rect5 = Rectangle(4, 6)
            rect5.display()
            expected_display = "####\n" * 6
            self.assertEqual(buff.getvalue(), expected_display)
        with io.StringIO() as buff, out(buff):
            rect5 = Rectangle(1, 1)
            rect5.display()
            expected_display = "#\n"
            self.assertEqual(buff.getvalue(), expected_display)

    def test_str(self):
        """Test rectangle str.
        """
        rect6 = Rectangle(32, 2, 2, 1, 53)
        self.assertEqual(str(rect6), "[Rectangle] (53) 2/1 - 32/2")
        rect7 = Rectangle(1, 1)
        self.assertEqual(str(rect7), "[Rectangle] (1) 0/0 - 1/1")

    def test_display1(self):
        """Test rectangle display1.
        """
        with io.StringIO() as buff, out(buff):
            rect7 = Rectangle(2, 2, 1, 4)
            rect7.display()
            expected_display = "\n\n\n\n"+" ##\n" * 2
            self.assertEqual(buff.getvalue(), expected_display)
        with io.StringIO() as buff, out(buff):
            rect8 = Rectangle(1, 1, 0, 0)
            rect8.display()
            expected_display = "#\n"
            self.assertEqual(buff.getvalue(), expected_display)

    def test_update_args(self):
        """Test rectangle update (args).
        """
        rect9 = Rectangle(1, 2, 3, 4, 5)
        rect9.update(100, 20, 23)
        self.assertEqual(rect9.id, 100)
        self.assertEqual(rect9.width, 20)
        self.assertEqual(rect9.height, 23)
        self.assertEqual(rect9.x, 3)
        self.assertEqual(rect9.y, 4)

    def test_update_kwargs(self):
        """Test rectangle update (kwargs).
        """
        rect10 = Rectangle(1, 2, 3, 4, 5)
        rect10.update(id=34, x=0, height=23)
        self.assertEqual(rect10.id, 34)
        self.assertEqual(rect10.width, 1)
        self.assertEqual(rect10.height, 23)
        self.assertEqual(rect10.x, 0)
        self.assertEqual(rect10.y, 4)

    def test_update_args_kwargs(self):
        """Test rectangle update (args/kwargs).
        """
        rect11 = Rectangle(1, 2, 3, 4, 5)
        rect11.update(100, 20, width=69)
        self.assertEqual(rect11.id, 100)
        self.assertEqual(rect11.width, 20)
        self.assertEqual(rect11.height, 2)
        self.assertEqual(rect11.x, 3)
        self.assertEqual(rect11.y, 4)

    def test_to_dictionay(self):
        """Test Rectangle to_dictionary method.
        """
        rect12 = Rectangle(1, 1, 1, 1, 1)
        dictionary = rect12.to_dictionary()
        self.assertEqual(type(dictionary), type({}))
        self.assertEqual("id" in dictionary, True)
        self.assertEqual("width" in dictionary, True)
        self.assertEqual("height" in dictionary, True)
        self.assertEqual("x" in dictionary, True)
        self.assertEqual("y" in dictionary, True)


if __name__ == "__main__":
    unittest.main()
