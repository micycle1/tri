import unittest

from tri.delaunay import triangulate


class TestTriSmoke(unittest.TestCase):
    def test_triangulate_minimum_triangle(self):
        dt = triangulate([(0.0, 0.0), (1.0, 0.0), (0.0, 1.0)])
        self.assertEqual(len(dt.vertices), 3)

