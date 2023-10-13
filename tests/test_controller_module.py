import unittest
from unittest.mock import Mock
from src.controller_module import ControllerModule

class TestControllerModule(unittest.TestCase):

    def setUp(self):
        self.input_module = Mock()
        self.drawing_module = Mock()
        self.storage_module = Mock()
        self.tkinter_module = Mock()
        self.controller = ControllerModule(
            self.input_module, self.drawing_module, self.tkinter_module
        )

    def test_point_in_triangle_cross_product_in_triangle(self):
        result = self.controller.point_in_triangle_cross_product(0, 0, 200, 0, 100, 100, 100, 0)
        self.assertTrue(result)

    def test_point_in_triangle_cross_product_outside_triangle(self):
        result = self.controller.point_in_triangle_cross_product(0, 0, 200, 0, 100, 100, 500, 500)
        self.assertFalse(result)

    def test_start_rotation_valid_input(self):
        self.tkinter_module.get_entry.return_value = (0, 0, 200, 0, 100, 100, 200, 100, 100)
        self.input_module.get_input_values.return_value = (0, 0, 200, 0, 100, 100, 200, 100, 100)
        self.controller.start_rotation()
        self.input_module.error_label.config.assert_called_with(text="")
        self.drawing_module.rotate_triangle.assert_called_with((0, 0, 200, 0, 100, 100), (100, 100), 200)

    def test_start_rotation_invalid_input(self):
        self.tkinter_module.get_entry.return_value = (0, 0, 200, 0, 100, 100, 200, 300, 300)
        self.input_module.get_input_values.return_value = (0, 0, 200, 0, 100, 100, 200, 300, 300)

        self.controller.start_rotation()

        self.input_module.error_label.config.assert_called_with(text="Точка не принадлежит отрезку")
        self.storage_module.set_input_values.assert_not_called()
        self.drawing_module.rotate_segment.assert_not_called()

if __name__ == '__main__':
    unittest.main()
