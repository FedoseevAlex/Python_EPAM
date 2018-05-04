import unittest

from Triangle import Point, Triangle


class TestPoint(unittest.TestCase):
    """Test case for class Point in Triangle.py."""

    def test_point_positive_init_no_arguments(self):
        """Positive test of __init__ function without arguments."""
        p = Point()
        self.assertEqual(p.x, 0.0, 'Test of Point().x failed. Returned value != 0.0')
        self.assertEqual(p.y, 0.0, 'Test of Point().y failed. Returned value != 0.0')

    def test_point_positive_init_one_argument(self):
        """Positive test of __init__ function with one given argument."""
        p = Point(3)
        self.assertEqual(p.x, 3.0, 'Test of Point(3).x failed. Returned value != 3.0')
        self.assertEqual(p.y, 0.0, 'Test of Point(3).y failed. Returned value != 0.0')

    def test_point_positive_init_x_keyword_argument(self):
        """Positive test of __init__ function with one given argument x as keyword argument."""
        p = Point(x=4)
        self.assertEqual(p.x, 4.0, 'Test of Point(x=4).x failed. Returned value != 4.0')
        self.assertEqual(p.y, 0.0, 'Test of Point(x=4).y failed. Returned value != 0.0')

    def test_point_positive_init_y_keyword_argument(self):
        """Positive test of __init__ function with one given argument y as keyword argument."""
        p = Point(y=5)
        self.assertEqual(p.x, 0.0, 'Test of Point(y=5).x failed. Returned value != 0.0')
        self.assertEqual(p.y, 5.0, 'Test of Point(y=5).y failed. Returned value != 5.0')

    def test_point_positive_init_correct_arguments(self):
        """Positive test of __init__ function with both correct arguments."""
        p = Point(2, 23.52)
        self.assertEqual(p.x, 2.0, 'Test of Point(2, 23.52).x failed. Returned value != 2.0')
        self.assertEqual(p.y, 23.52, 'Test of Point(2, 23.52).y failed. Returned value != 23.52')

        p = Point(x=2, y=23.52)
        self.assertEqual(p.x, 2.0, 'Test of Point(x=2, y=23.52).x failed. Returned value != 2.0')
        self.assertEqual(p.y, 23.52, 'Test of Point(x=2, y=23.52).y failed. Returned value != 23.52')

        p = Point(y=2, x=23.52)
        self.assertEqual(p.y, 2.0, 'Test of Point(y=2, x=23.52).x failed. Returned value != 23.52')
        self.assertEqual(p.x, 23.52, 'Test of Point(y=2, x=23.52).y failed. Returned value != 2.0')

    def test_point_negative_init_wrong_type_argument(self):
        """
        Negative test of __init__ function with one given argument of wrong types.
        Checked argument types -> str, list, tuple, dict, set
        """
        with self.assertRaises(ValueError) as err:
            Point('five', 'three')
            self.assertEqual(err.args[0], 'Wrong value to define point. Both x and y must be int or float.',
                             "Test of Point('five', 'three') failed.")

        with self.assertRaises(ValueError) as err:
            Point(['five', 'two'])
            self.assertEqual(err.args[0], 'Wrong value to define point. Both x and y must be int or float.',
                             "Test of Point(['five', 'two']) failed.")

        with self.assertRaises(ValueError) as err:
            Point([5, 2])
            self.assertEqual(err.args[0], 'Wrong value to define point. Both x and y must be int or float.',
                             "Test of Point([5, 2]) failed.")

        with self.assertRaises(ValueError) as err:
            Point((1, 3))
            self.assertEqual(err.args[0], 'Wrong value to define point. Both x and y must be int or float.',
                             "Test of Point((1, 3)) failed.")

        with self.assertRaises(ValueError) as err:
            Point({'x': 3, 'y': 0.1})
            self.assertEqual(err.args[0], 'Wrong value to define point. Both x and y must be int or float.',
                             "Test of Point({'x': 3, 'y': 0.1}) failed.")

        with self.assertRaises(ValueError) as err:
            Point({3, 0.1})
            self.assertEqual(err.args[0], 'Wrong value to define point. Both x and y must be int or float.',
                             "Test of Point({3, 0.1}) failed.")

    def test_point_positive_repr(self):
        """Positive test of __repr__ method."""
        p = Point(x=3, y=5)
        self.assertTupleEqual(p.__repr__(), (3.0, 5.0),
                         'Test of Point(x=3, y=5).__repr__() failed. Returned value != (3.0, 5.0)')

    def test_point_positive_str(self):
        """Positive test of __repr__ method."""
        p = Point(x=3, y=5)
        self.assertEqual(p.__str__(), '(3.0, 5.0)',
                              'Test of Point(x=3, y=5).__repr__() failed. Returned value != (3.0, 5.0)')

    def test_point_positive_add(self):
        """Positive test of __add__ method."""
        p1 = Point(x=3, y=5)
        p2 = Point(5, 3)
        p = p1 + p2
        self.assertEqual(str(p), '(8.0, 8.0)',
                         'Test of Point(x=3, y=5) + Point(5, 3) failed. Returned value != (8.0, 8.0)')

    def test_point_negative_x_and_y_setting_deleting(self):
        """Negative test of attribute setting and deleting method."""
        p = Point(x=6.67, y=5.34)

        with self.assertRaises(AttributeError) as err:
            p.x = 9
            self.assertEqual(err.args[0], "Can't set attribute.",
                             "Test of Point(x=6.67, y=5.34).x = 9 failed, no AttributeError was raised.")

        with self.assertRaises(AttributeError) as err:
            p.y = 10
            self.assertEqual(err.args[0], "Can't set attribute.",
                             "Test of Point(x=6.67, y=5.34).y = 10 failed, no AttributeError was raised.")

        with self.assertRaises(AttributeError) as err:
            del p.x
            self.assertEqual(err.args[0], "Can't delete attribute.",
                             "Test of del Point(x=6.67, y=5.34).x failed, no AttributeError was raised.")

        with self.assertRaises(AttributeError) as err:
            del p.y
            self.assertEqual(err.args[0], "Can't delete attribute.",
                             "Test of del Point(x=6.67, y=5.34).y failed, no AttributeError was raised.")

    def test_point_positive_x_and_y_getting(self):
        """Positive test of attribute getting."""
        p = Point(x=6.67, y=5.34)
        self.assertEqual(p.x, 6.67, "Test of Point(x=6.67, y=5.34).x failed, returned value != 6.67.")
        self.assertEqual(p.y, 5.34, "Test of Point(x=6.67, y=5.34).y failed, returned value != 5.34.")

    def test_point_positive_distance(self):
        """Positive test of Point.distance method."""
        p1 = Point(1, 7)
        p2 = Point(4, 23)
        self.assertEqual(p1.distance(p2), 265 ** 0.5,
                         "Test of Point(1, 7).distance(Point(4, 23)) failed, returned value != 16.278820596099706.")
        self.assertEqual(p1.distance(), 5 * 2 ** 0.5,
                         "Test of Point(x=6.67, y=5.34).distance() failed, returned value != 7.0710678118654755.")

    def test_point_negative_distance(self):
        """Negative test of Point.distance method."""

        with self.assertRaises(ValueError) as err:
            Point(1, 7).distance('foo')
            self.assertEqual(err.args[0], "Wrong type of argument. Distance is calculated between two Point objects.",
                             "Test of Point(1, 7).distance('foo') failed, no ValueError was raised.")

    def test_point_positive_on_one_line(self):
        """Negative test of Point.on_one_line method."""
        a = Point(1, 0)
        b = Point(34, 0)
        c = Point(42, 0)

        self.assertTrue(Point.on_one_line(a, b, c),
                        "Test of Point.on_one_line(a, b, c) failed, returned value != True.")
        d = Point(1, 2)
        e = Point(34, 43)
        f = Point(42, 54)

        self.assertFalse(Point.on_one_line(d, e, f),
                         "Test of Point.on_one_line(d, e, f) failed, returned value != False.")

        self.assertTrue(Point.on_one_line(a), "Test of Point.on_one_line(a) failed, returned value != True.")

    def test_point_negative_on_one_line(self):
        """Negative test of Point.on_one_line method."""
        a = Point(1, 0)
        b = Point(34, 0)
        c = Point(42, 0)

        with self.assertRaises(ValueError) as err:
            Point.on_one_line('foo', a, b, c)
            self.assertEqual(err.args[0], "Some of given arguments is not points.",
                             "Test of Point.on_one_line('foo', a, b, c) failed, no ValueError was raised.")


class TestTriangle(unittest.TestCase):
    """Test case for class Triangle in Triangle.py."""

    def test_triangle_positive_init(self):
        """Positive test of Triangle.__init__ method."""
        t = Triangle(Point(1, 1), Point(2, 3), Point(4, 5))
        self.assertEqual(str(t), '((1.0, 1.0), (2.0, 3.0), (4.0, 5.0))',
                         "Test of Triangle(Point(0, 0), Point(8, 0), Point(4, 5)) failed,\
                          returned value != ((1.0, 1.0), (2.0, 3.0), (4.0, 5.0)).")

    def test_triangle_negative_init_points_on_line(self):
        """Negative test of Triangle.__init__ method. Points belong to one line."""
        with self.assertRaises(ValueError) as err:
            Triangle(Point(1, 1), Point(1, 3), Point(1, 5))
            self.assertEqual(err.args[0], "Given points belong to one line and can not define triangle.",
                             "Triangle(Point(1, 1), Point(1, 3), Point(1, 5)) failed, no ValueError was raised.")

    def test_triangle_negative_init_wrong_argument_type(self):
        """Negative test of Triangle.__init__ method. Wrong type of arguments."""
        with self.assertRaises(ValueError) as err:
            Triangle('foo', Point(1, 3), 'bar')
            self.assertEqual(err.args[0], "Given points belong to one line and can not define triangle.",
                             "Triangle('foo', Point(1, 3), 'bar') failed, no ValueError was raised.")

        with self.assertRaises(ValueError) as err:
            Triangle(42, Point(1, 3), 21)
            self.assertEqual(err.args[0], "Given points belong to one line and can not define triangle.",
                             "Triangle(42, Point(1, 3), 21) failed, no ValueError was raised.")

    def test_triangle_positive_area(self):
        """Positive test of Triangle.area method."""
        t = Triangle(Point(0, 3.1415), Point(2.7, 3), Point(3 ** 0.5, 6.023))
        self.assertEqual(t.area(1), 4.0,
                         "Test of Triangle(Point(0, 3.1415), Point(2.7, 3), Point(3 ** 0.5, 6.023)).area(1),\
                          returned value != 4.0.")
        self.assertEqual(t.area(), 4.013,
                         "Test of Triangle(Point(0, 3.1415), Point(2.7, 3), Point(3 ** 0.5, 6.023)).area(1) failed,\
                          returned value != 4.013.")
        self.assertEqual(t.area(6), 4.012568,
                         "Test of Triangle(Point(0, 3.1415), Point(2.7, 3), Point(3 ** 0.5, 6.023)).area(6) failed,\
                          returned value != 4.012568.")

    def test_triangle_negative_area_negative_mantissa(self):
        """Negative test of Triangle.area method. Give -1 as mantissa value."""
        t = Triangle(Point(0, 3.1415), Point(2.7, 3), Point(3 ** 0.5, 6.023))

        with self.assertRaises(ValueError) as err:
            t.area(-1)
            self.assertEqual(err.args[0], "Negative number for mantissa is not allowed.",
                             "Triangle(Point(0, 3.1415), Point(2.7, 3), Point(3 ** 0.5, 6.023)).area(-1) failed,\
                              no ValueError was raised.")

    def test_triangle_positive_is_isosceles_property(self):
        """Positive test of Triangle.is_isosceles property."""
        a = Point(-2, 0)
        b = Point(2, 0)
        c = Point(0, 4)
        t = Triangle(a, b, c)
        self.assertTrue(t.is_isosceles,
                         "Test of Triangle(Point(-2, 0), Point(2, 0), Point(0, 4)) failed, returned value != True.")
        d = Point(-2, 45)
        e = Point(2, 0)
        f = Point(0, 4)
        g = Triangle(d, e, f)
        self.assertFalse(g.is_isosceles,
                         "Test of Triangle(Point(-2, 45), Point(2, 0), Point(0, 4)) failed, returned value != False.")

    def test_triangle_positive_is_equilateral_property(self):
        """Positive test of Triangle.is_equilateral property."""
        a = Point(-9, 10)
        b = Point(-1, 4)
        c = Point(3 * 3 ** 0.5 - 5, 4 * 3 ** 0.5 + 7)
        t = Triangle(a, b, c)
        self.assertTrue(t.is_equilateral,
                         "Test of Triangle(Point(-9, 10), Point(-1, 4), Point(3 * 3 ** 0.5 - 5, 4 * 3 ** 0.5 + 7))\
                          failed, returned value != True.")
        a = Point(-9, 21)
        b = Point(-1, 4)
        c = Point(3 * 3 ** 0.5 - 5, 4 * 3 ** 0.5 + 7)
        t = Triangle(a, b, c)
        self.assertFalse(t.is_equilateral,
                         "Test of Triangle(Point(-9, 21), Point(-1, 4), Point(3 * 3 ** 0.5 - 5, 4 * 3 ** 0.5 + 7))\
                          failed, returned value != False.")


if __name__ == '__main__':
    unittest.main()
