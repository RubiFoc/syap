# Задание 2:
# Требуется написать программу, которая вычисляет общую площадь стены
# комнаты, которую необходимо оклеить обоями. При этом окна, двери, пол и
# потолок оклеивать не нужно. – 3 балла
class SquareOfWalls:
    def __init__(self, windows_square, door_square, room_length, room_height, room_width):
        self.windows_square = windows_square
        self.door_square = door_square
        self.room_length = room_length
        self.room_height = room_height
        self.room_width = room_width
        self.walls_square = 2 * self.room_height * (self.room_length + self.room_width)

    def get_walls_square(self):
        return self.walls_square

    def calculate_wallpaper(self):
        return self.walls_square - self.windows_square - self.door_square


wall = SquareOfWalls(5, 2, 7, 3, 4)
print(str(wall.get_walls_square()) + ' м^2')
print(str(wall.calculate_wallpaper()) + ' м^2')
