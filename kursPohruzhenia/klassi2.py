import csv
import os


class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)

    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[1]


class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = int(passenger_seats_count)
        self.car_type = 'car'


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        body_dimensions = body_whl.split('x')
        self.car_type = 'truck'
        try:
            if len(body_dimensions) != 3:
                raise ValueError

            for i in range(0, len(body_dimensions)):
                body_dimensions[i] = float(body_dimensions[i])

                if body_dimensions[i] <= 0.0:
                    raise ValueError

        except ValueError:
            body_dimensions = [float(0), float(0), float(0)]
        finally:
            self.body_length = float(body_dimensions[0])
            self.body_width = float(body_dimensions[1])
            self.body_height = float(body_dimensions[2])
            self.volume = float(body_dimensions[0]) * float(body_dimensions[1]) * float(body_dimensions[2])

    def get_body_volume(self):
        return self.volume


class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra
        self.car_type = 'spec_machine'


def get_car_list(csv_filename):
    car_list = []

    with open(csv_filename, encoding='utf-8') as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # пропускаем заголовок

        for row in reader:
            if len(row) != 7:
                continue

            t = row[0]
            brand = row[1]
            passenger_seat = row[2]
            photo_name = row[3]
            body_whl = row[4]
            carrying = row[5]
            extra = row[6]

            if not carrying or not brand or not photo_name:
                continue

            try:
                carrying = float(carrying)
                if carrying <= 0.0:
                    raise ValueError
            except ValueError:
                continue

            if t == 'car':
                try:
                    passenger_seat = int(passenger_seat)
                    if passenger_seat <= 0:
                        raise ValueError

                    car_list.append(Car(brand, photo_name, carrying, passenger_seat))
                except ValueError:
                    continue

            elif t == 'spec_machine':
                try:
                    if '.png' in photo_name or '.gif' in photo_name or '.jpeg' in photo_name or '.jpg' in photo_name:
                        if extra and not passenger_seat and not body_whl:
                            car_list.append(SpecMachine(brand, photo_name, carrying, extra))

                    else:
                        raise ValueError
                except ValueError:
                    continue
            elif t == 'truck':
                car_list.append(Truck(brand, photo_name, carrying, body_whl))
            else:
                continue

    return car_list


if __name__ == '__main__':

    csv_filename = r"C:\Users\rb693\Desktop\coursera_week3_cars.csv"
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # пропускаем заголовок
        for row in reader:
            print(row)

    for i in get_car_list(csv_filename):
        print(i)

    print(len(get_car_list(csv_filename)))
    print(bool(''))