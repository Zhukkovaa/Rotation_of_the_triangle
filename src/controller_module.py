import tkinter as tk
class ControllerModule:
    """
       Класс для управления вращением треугольника.

       Ключевые атрибуты:
           root (tk.Tk): Основное окно приложения.
           input_module (InputModule): Модуль для ввода данных.
           drawing_module (DrawingModule): Модуль для рисования и вращения треугольника.
           tkinter_module (TkinterModule): Модуль для создания пользовательского интерфейса.

       Методы:

           point_in_triangle_cross_product(self, x1, y1, x2, y2, x3, y3, x, y):
               Проверяет, принадлежит ли точка треугольнику, используя векторное произведение.

           input_value(self):
               Получает входные значения от пользовательского интерфейса.

           start_rotation(self):
               Начинает вращение треугольника.

    """

    def __init__(self, input_module, drawing_module, tkinter_module):
        self.input_module = input_module
        self.drawing_module = drawing_module
        self.input_module.error_label = self.input_module.error_label
        self.input_module.get_input_values=self.input_module.get_input_values
        self.tkinter_module = tkinter_module
        self.tkinter_module.create_button = tkinter_module.create_button("Начать вращение",self.start_rotation)

    def point_in_triangle_cross_product(self, x1, y1, x2, y2, x3, y3, x, y):
        """
            Проверяет, принадлежит ли точка треугольнику, используя векторное произведение.

            Ключевые аргументы:
                x1, y1, x2, y2, x3, y3: Координаты вершин треугольника.
                x, y: Координаты точки вращения.

            Возвращаемое значение:
                bool: True, если точка принадлежит треугольнику, иначе False.

            Описание:
            Эта функция использует метод векторного произведения для определения, принадлежит ли заданная
            точка треугольнику. Она вычисляет векторные произведения для трех пар вершин треугольника
            и точки и проверяет их знаки. Если все векторные произведения имеют одинаковые знаки
            (положительные или отрицательные), то точка принадлежит треугольнику.

        """
        cross_product1 = (x - x1) * (y2 - y1) - (y - y1) * (x2 - x1)
        cross_product2 = (x - x2) * (y3 - y2) - (y - y2) * (x3 - x2)
        cross_product3 = (x - x3) * (y1 - y3) - (y - y3) * (x1 - x3)
        return (cross_product1 >= 0 and cross_product2 >= 0 and cross_product3 >= 0) or (cross_product1 <= 0 and cross_product2 <= 0 and cross_product3 <= 0)

    def input_value(self):
        """
           Используется для получения входных данных от пользовательского интерфейса.

           Возвращаемое значение:
               tuple: Кортеж с входными значениями координат треугольника, угловой скорости, точки вращения
               (x1, y1, x2, y2, x3, y3, speed, center_x, center_y).

           Описание:
                Этот метод извлекает значения, введенные пользователем, из пользовательского интерфейса
                с помощью объекта tkinter_module. Затем он возвращает эти значения в виде кортежа,
                содержащего координаты вершин треугольника (x1, y1, x2, y2, x3, y3), скорость (speed),
                а также координаты центра вращения (center_x, center_y).

        """
        x1, y1,x2, y2, x3, y3, speed_entry, center_x_entry,center_y_entry=self.tkinter_module.get_entry()
        return self.input_module.get_input_values(x1, y1,x2, y2, x3, y3, speed_entry, center_x_entry,center_y_entry)

    def start_rotation(self):
        """
         Начинает вращение треугольника.

         Описание:
            Данный метод вызывается при нажатии кнопки "Начать вращение" и начинает вращение треугольника.
            Сначала метод проверяет, принадлежит ли заданная точка треугольнику. Если точка
            не принадлежит треугольнику, то устанавливает текст ошибки и завершает выполнение. В противном
            случае, сбрасывает текст ошибки. Затем вызывается метод для вращения треугольника с учетом
            введенных данных.

        """
        x1, y1, x2, y2, x3, y3, speed, center_x, center_y = self.input_value()
        if not self.point_in_triangle_cross_product(x1, y1, x2, y2, x3, y3, center_x, center_y):
            self.input_module.error_label.config(text="Точка лежит вне треугольника")
            return
        self.input_module.error_label.config(text="")
        triangle = (x1, y1, x2, y2, x3, y3)
        self.drawing_module.rotate_triangle(triangle, (center_x, center_y), speed)
