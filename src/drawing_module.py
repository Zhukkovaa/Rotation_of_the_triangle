import math
class DrawingModule:
    """
       Класс для рисования и вращения треугольника на холсте.

       Ключевые атрибуты:
           canvas (tk.Canvas): Виджет холста, на котором будет производиться рисование и вращение треугольника.
           triangle (tuple): Кортеж, содержащий координаты вершин текущего треугольника.

       Методы:

           rotate_triangle(self, triangle, center, angular_speed):
               Вращает треугольник вокруг центра вращения с указанной угловой скоростью.

     """

    def __init__(self, canvas):
        self.canvas = canvas
        self.triangle = None

    def rotate_triangle(self, triangle, center, angular_speed):
        """
            Вращает треугольник вокруг центра вращения с указанной угловой скоростью.

            Ключевые атрибуты:
                triangle (tuple): Кортеж, содержащий координаты вершин треугольника (x1, y1, x2, y2, x3, y3).
                center (tuple): Кортеж с координатами центра вращения (center_x, center_y).
                angular_speed (float): Угловая скорость вращения в градусах в секунду.

            Описание:
                Этот метод вращает треугольник, заданный координатами его вершин, вокруг указанного
                центра вращения с заданной угловой скоростью. При каждой итерации метода, треугольник
                поворачивается на угол, равный `angular_speed`, вокруг точки `center`. Затем, новые
                координаты вершин треугольника используются для отображения его нового положения на
                холсте. Метод выполняет рекурсивные вызовы с задержкой 20 миллисекунд для плавного
                вращения треугольника.

        """
        x1, y1, x2, y2, x3, y3 = triangle
        center_x, center_y = center
        angle = angular_speed
        radian_angle = math.radians(angle)
        rotated_x1 = center_x + (x1 - center_x) * math.cos(radian_angle) - (y1 - center_y) * math.sin(radian_angle)
        rotated_y1 = center_y + (x1 - center_x) * math.sin(radian_angle) + (y1 - center_y) * math.cos(radian_angle)
        rotated_x2 = center_x + (x2 - center_x) * math.cos(radian_angle) - (y2 - center_y) * math.sin(radian_angle)
        rotated_y2 = center_y + (x2 - center_x) * math.sin(radian_angle) + (y2 - center_y) * math.cos(radian_angle)
        rotated_x3 = center_x + (x3 - center_x) * math.cos(radian_angle) - (y3 - center_y) * math.sin(radian_angle)
        rotated_y3 = center_y + (x3 - center_x) * math.sin(radian_angle) + (y3 - center_y) * math.cos(radian_angle)
        self.canvas.delete('triangle')
        self.canvas.create_polygon(rotated_x1, rotated_y1, rotated_x2, rotated_y2, rotated_x3, rotated_y3, tags='triangle', fill='pink')
        self.canvas.after(20, self.rotate_triangle, (rotated_x1, rotated_y1, rotated_x2, rotated_y2, rotated_x3, rotated_y3), (center_x, center_y), angular_speed)
