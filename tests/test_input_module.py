import unittest
from unittest.mock import Mock
from src.input_module import InputModule

class TestInputModule(unittest.TestCase):

    def test_validate_input_valid(self):
        error_label = Mock()
        input_module = InputModule(error_label)

        widget_mock = Mock()
        widget_mock.get.return_value = "1"
        event_mock = Mock(widget=widget_mock)

        input_module.validate_input(event_mock)
        error_label.config.assert_called_with(text="")

    def test_validate_input_invalid(self):
        error_label = Mock()
        input_module = InputModule(error_label)

        widget_mock = Mock()
        widget_mock.get.return_value = "abc"
        event_mock = Mock(widget=widget_mock)

        input_module.validate_input(event_mock)
        error_label.config.assert_called_with(text="Введите числовое значение!")

    def test_validate_input_invalid2(self):
        error_label = Mock()
        input_module = InputModule(error_label)

        widget_mock = Mock()
        widget_mock.get.return_value = "*/."
        event_mock = Mock(widget=widget_mock)

        input_module.validate_input(event_mock)
        error_label.config.assert_called_with(text="Введите числовое значение!")

    def test_get_input_values(self):
        x1, y1, x2, y2, x3, y3 = "100", "200", "300", "400", "500", "600"
        speed_entry, center_x_entry, center_y_entry = "700", "800", "900"

        error_label = Mock()
        input_module = InputModule(error_label)

        result = input_module.get_input_values(x1, y1, x2, y2, x3, y3, speed_entry, center_x_entry, center_y_entry)
        expected_result = (100, 200, 300, 400, 500, 600, 700, 800, 900)

        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
