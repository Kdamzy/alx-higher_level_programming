#!/usr/bin/python3
"""Defines unittests for base.py"""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """unit-test for Base model"""
    def no_arg(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)
        
    def two_args(self):
        with self.assertRaises(TypeError):
            Base(1, 2)

    def three_arg(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)

    def NO_id(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def unique_id(self):
        self.assertEqual(12, Base(12).id)

    def ids(self):
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 1)

    def instances(self):
        with self.assertRaises(AttributeError):
            print(Base(12).__nb_instances)

    def str_id(self):
        self.assertEqual("hello", Base("hello").id)

    def float_id(self):
        self.assertEqual(5.5, Base(5.5).id)

    def complex_id(self):
        self.assertEqual(complex(5), Base(complex(5)).id)

    def dict_id(self):
        self.assertEqual({"a": 1, "b": 2}, Base({"a": 1, "b": 2}).id)

    def bool_id(self):
        self.assertEqual(True, Base(True).id)

    def list_id(self):
        self.assertEqual([1, 2, 3], Base([1, 2, 3]).id)

    def tuple_id(self):
        self.assertEqual((1, 2), Base((1, 2)).id)

    def set_id(self):
        self.assertEqual({1, 2, 3}, Base({1, 2, 3}).id)

    def frozen_id(self):
        self.assertEqual(frozenset({1, 2, 3}), Base(frozenset({1, 2, 3})).id)

    def range_id(self):
        self.assertEqual(range(5), Base(range(5)).id)

    def bytes_id(self):
        self.assertEqual(b'Python', Base(b'Python').id)

    def bytearray_id(self):
        self.assertEqual(bytearray(b'abcefg'), Base(bytearray(b'abcefg')).id)

    def memorys_id(self):
        self.assertEqual(memoryview(b'abcefg'), Base(memoryview(b'abcefg')).id)

    def info_id(self):
        self.assertEqual(float('inf'), Base(float('inf')).id)

    def NaN_id(self):
        self.assertNotEqual(float('nan'), Base(float('nan')).id)
        
    def tearDown(self):
        """Delete any created file after each test."""
        pass

class Test_to_json_string(unittest.TestCase):
    """Unittests for Base class."""

    def json_string_rectangle_a(self):
        """Unittest for Rectangle Base class"""
        r = Rectangle(10, 7, 2, 8, 6)
        self.assertEqual(str, type(Base.to_json_string([r.to_dictionary()])))

    def json_string_rectangle_b(self):
        """Test for one dict"""
        r = Rectangle(10, 7, 2, 8, 6)
        self.assertTrue(len(Base.to_json_string([r.to_dictionary()])) == 53)

    def json_string_rectangle_c(self):
        """Test for two dict"""
        r1 = Rectangle(2, 4, 5, 6, 2)
        r2 = Rectangle(4, 2, 6, 1, 9)
        list_dicts = [r1.to_dictionary(), r2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 106)

    def json_string_square_a(self):
        """Unittest for square Base class """
        s = Square(8, 2, 6, 4)
        self.assertEqual(str, type(Base.to_json_string([s.to_dictionary()])))

    def json_string_square_b(self):
        """Test for one dict"""
        s = Square(8, 2, 6, 4)
        self.assertTrue(len(Base.to_json_string([s.to_dictionary()])) == 39)

    def json_string_square_c(self):
        """Test for two dict"""
        s1 = Square(10, 2, 3, 4)
        s2 = Square(4, 5, 2, 2)
        list_dicts = [s1.to_dictionary(), s2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 78)

    def json_string_list(self):
        """Empty string"""
        self.assertEqual("[]", Base.to_json_string([]))


    def json_string_no_args(self):
        """Test when no arggument is passed"""
        with self.assertRaises(TypeError):
            Base.to_json_string()


class Test_save_to_file(unittest.TestCase):
    """Unittests for save_to_file function of Base class."""


    def test_save_to_file_rectangle_a(self):
        """Test for one rectangle dict"""
        r = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 53)

    def test_save_to_file_rectangles_b(self):
        """Test for two rectangle dict"""
        r1 = Rectangle(10, 7, 2, 8, 5)
        r2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 105)

    def test_save_to_file_square_a(self):
        """test for one square dict"""
        s = Square(10, 7, 2, 8)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

    def test_save_to_file_squares_b(self):
        """test for two square dict"""
        s1 = Square(10, 7, 2, 8)
        s2 = Square(8, 1, 2, 3)
        Square.save_to_file([s1, s2])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 77)


    def test_save_to_file_empty_list(self):
        """when there is an empty list"""
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_no_args(self):
        """No argument is passes"""
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()



class Test_from_json_string(unittest.TestCase):
    """Unittests for from_json_string method of Base class."""


    def test_from_json_string_rectangle_a(self):
        """Test for one rectangle dict"""
        list_input = [{"id": 89, "width": 10, "height": 4, "x": 7}]
        json_list_input = Rectangle.to_json_string(list_input)
        output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, output)

    def test_from_json_string_rectangles_b(self):
        """test for two rectangle dict"""
        list_input = [
            {"id": 89, "width": 10, "height": 4, "x": 7, "y": 8},
            {"id": 98, "width": 5, "height": 2, "x": 1, "y": 3},
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, output)

    def test_from_json_string_square_a(self):
        """test for one square dict"""
        list_input = [{"id": 89, "size": 10, "height": 4}]
        json_list_input = Square.to_json_string(list_input)
        output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, output)

    def test_from_json_string_two_squares(self):
        list_input = [
            {"id": 89, "size": 10, "height": 4},
            {"id": 7, "size": 1, "height": 7}
        ]
        json_list_input = Square.to_json_string(list_input)
        output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, output)

    def test_from_json_string_empty_list(self):
        """when there ia an empth list"""
        self.assertEqual([], Base.from_json_string("[]"))

    def test_from_json_string_no_args(self):
        """No argument passed"""
        with self.assertRaises(TypeError):
            Base.from_json_string()


class TestBase_create(unittest.TestCase):
    """Unittests for create method of Base class."""

    def test_create_rectangle(self):
        r1 = Rectangle(1, 5, 1, 3, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(r1))

    def test_create_rectangle_b(self):
        r1 = Rectangle(1, 5, 1, 3, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertNotEqual(r1, r2)

    def test_create_square(self):
        s1 = Square(1, 5, 1, 3, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual("[Square] (7) 5/1 - 3", str(s1))

    def test_create_square_b(self):
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertNotEqual(s1, s2)


class TestBase_load_from_file(unittest.TestCase):
    """Unittests for load_from_file_method of Base class."""
    
    
    def test_load_from_file_rectangle(self):
        """test case for Rectangle"""
        r1 = Rectangle(8, 5, 2, 9, 1)
        r2 = Rectangle(6, 2, 5, 7, 2)
        Rectangle.save_to_file([r1, r2])
        output = Rectangle.load_from_file()
        self.assertTrue(all(type(obj) == Rectangle for obj in output))
        
    def test_load_from_file_rectangle_a(self):
        """test for the first rectangle dict"""
        r1 = Rectangle(18, 5, 2, 9, 1)
        r2 = Rectangle(6, 2, 5, 7, 2)
        Rectangle.save_to_file([r1, r2])
        rectangle_output = Rectangle.load_from_file()
        self.assertEqual(str(r1), str(rectangle_output[0]))

    def test_load_from_file_rectangle_b(self):
        """tet for the second ectangle dict"""
        r1 = Rectangle(8, 5, 2, 9, 1)
        r2 = Rectangle(6, 2, 5, 7, 2)
        Rectangle.save_to_file([r1, r2])
        rectangle_output = Rectangle.load_from_file()
        self.assertEqual(str(r2), str(rectangle_output[1]))

    def test_load_from_file_square(self):
        """test case for square"""
        s1 = Square(7, 1, 6, 4)
        s2 = Square(5, 8, 2, 3)
        Square.save_to_file([s1, s2])
        output = Square.load_from_file()
        self.assertTrue(all(type(obj) == Square for obj in output))
        
    def test_load_from_file_square_a(self):
        """test for the first square dict"""
        s1 = Square(7, 1, 6, 4)
        s2 = Square(5, 8, 2, 3)
        Square.save_to_file([s1, s2])
        square_output = Square.load_from_file()
        self.assertEqual(str(s1), str(square_output[0]))

    def test_load_from_file_square_b(self):
        """Test for the second dict"""
        s1 = Square(7, 1, 6, 4)
        s2 = Square(5, 8, 2, 3)
        Square.save_to_file([s1, s2])
        square_output = Square.load_from_file()
        self.assertEqual(str(s2), str(square_output[1]))

    def test_load_from_file_none(self):
        """when the file is not present"""
        output = Square.load_from_file()
        self.assertEqual([], output)


class TestBase_save_to_file_csv(unittest.TestCase):
    """Unittests for save_to_file_csv method of Base class."""


    def test_save_to_file_csv_rectangle_a(self):
        r = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file_csv([r])
        with open("Rectangle.csv", "r") as f:
            self.assertTrue("5,10,7,2,8", f.read())

    def test_save_to_file_csv_rectangles_b(self):
        r1 = Rectangle(1, 7, 2, 8, 5)
        r2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file_csv([r1, r2])
        with open("Rectangle.csv", "r") as f:
            self.assertTrue("5,10,7,2,8\n2,4,1,2,3", f.read())

    def test_save_to_file_csv_square_a(self):
        """test case when one argumnet is passed"""
        s = Square(10, 7, 2, 8)
        Square.save_to_file_csv([s])
        with open("Square.csv", "r") as f:
            self.assertTrue("8,10,7,2", f.read())

    def test_save_to_file_csv_squares_b(self):
        """test case when two argument is passed"""
        s1 = Square(10, 7, 2, 8)
        s2 = Square(8, 1, 2, 3)
        Square.save_to_file_csv([s1, s2])
        with open("Square.csv", "r") as f:
            self.assertTrue("8,10,7,2\n3,8,1,2", f.read())

    def test_save_to_file__csv_cls_file(self):
        s = Square(10, 7, 2, 8)
        Base.save_to_file_csv([s])
        with open("Base.csv", "r") as f:
            self.assertTrue("8,10,7,2", f.read())


    def test_save_to_file_csv_empty_list(self):
        """When there is an empty list"""
        Square.save_to_file_csv([])
        with open("Square.csv", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_csv_no_args(self):
        """when no argument is passed"""
        with self.assertRaises(TypeError):
            Rectangle.save_to_file_csv()


class TestBase_load_from_file_csv(unittest.TestCase):
    """Unittests for testing load_from_file_csv method of Base class."""


    def test_load_from_file_csv_rectangle_a(self):
        """test case for the first rectangle dict"""
        r1 = Rectangle(13, 7, 3, 10, 1)
        r2 = Rectangle(4, 5, 3, 9, 2)
        Rectangle.save_to_file_csv([r1, r2])
        rectangle_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(r1), str(rectangle_output[0]))

    def test_load_from_file_csv_second_rectangle(self):
        """test case for the second rectangle dict"""
        r1 = Rectangle(13, 7, 3, 10, 1)
        r2 = Rectangle(4, 5, 3, 9, 2)
        Rectangle.save_to_file_csv([r1, r2])
        rectangle_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(r2), str(rectangle_output[1]))


    def test_load_from_file_csv_square_a(self):
        """test case for the first square dict"""
        s1 = Square(4, 1, 2, 3)
        s2 = Square(7, 4, 2, 5)
        Square.save_to_file_csv([s1, s2])
        square_output = Square.load_from_file_csv()
        self.assertEqual(str(s1), str(square_output[0]))

    def test_load_from_file_csv_square_b(self):
        """Test for the second square dict"""
        s1 = Square(4, 1, 2, 3)
        s2 = Square(7, 4, 2, 5)
        Square.save_to_file_csv([s1, s2])
        squares_output = Square.load_from_file_csv()
        self.assertEqual(str(s2), str(squares_output[1]))


    def test_load_from_file_csv_no_file(self):
        """the file is not present"""
        output = Square.load_from_file_csv()
        self.assertEqual([], output)


if __name__ == "__main__":
    unittest.main()