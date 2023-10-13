import unittest
from unittest.mock import Mock, patch
from src.drawing_module import DrawingModule

class TestDrawingModule(unittest.TestCase):

    def setUp(self):
        self.canvas = Mock()
        self.drawing_module = DrawingModule(self.canvas)

    def test_rotate_triangle(self):
        with patch('math.radians') as mock_radians:
            mock_radians.return_value = 45.0
            self.drawing_module.rotate_triangle((0, 0, 100, 0, 50, 100), (50, 50), 45.0)

        self.canvas.create_polygon.assert_called()

    def test_rotate_triangle_no_rotation(self):
        original_triangle = (0, 0, 100, 0, 50, 100)
        center = (50, 50)
        angular_speed = 0.0
        self.drawing_module.rotate_triangle(original_triangle, center, angular_speed)
        rotated_segment = self.canvas.create_polygon.call_args[0]
        self.assertEqual(rotated_segment, original_triangle)

if __name__ == '__main__':
    unittest.main()
