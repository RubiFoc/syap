# Задание 3:
# 1. Реализуйте базовый класс Car.
# 2. У класса должны быть следующие атрибуты: speed, color, name, is_police
# (булево). А также методы: go, stop, turn(direction), которые должны сообщать,
# что машина поехала, остановилась, повернула (куда);
# 3. Опишите несколько дочерних классов: TownCar, SportCar, WorkCar,
# PoliceCar;
# 4. Добавьте в базовый класс метод show_speed, который должен показывать
# текущую скорость автомобиля;
# 5. Для классов TownCar и WorkCar переопределите метод show_speed. При
# значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться
# сообщение о превышении скорости. – 3 балла

class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction: int):
        if direction == 0:
            print('Машина повернула вправо')
        elif direction == 1:
            print('Машина повернула влево')
        else:
            print('Машина развернулась')

    def show_speed(self):
        print(self.speed)


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f"Превышение скорости {self.speed}")
        else:
            print(self.speed)


class SportCar(Car):
    ...


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f"Превышение скорости {self.speed}")
        else:
            print(self.speed)


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, is_police=True)


sport_car = SportCar(100, "красный", "спортивная тачанка")
sport_car.show_speed()
town_car = TownCar(61, 'синий', "обычная тачанка")
town_car.show_speed()
work_car = WorkCar(41, 'грязный', "убитая тачанка")
work_car.show_speed()
police_car = PoliceCar(100, "чёрная", "полицейская тачанка")
police_car.show_speed()
