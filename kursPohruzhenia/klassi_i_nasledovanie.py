import csv
import os


class CarBase:

    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)

    def get_photo_file_ext(self):
        _, ext = os.path.splitext(self.photo_file_name)
        return ext


class Car(CarBase):
    car_type = 'car'

    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = int(passenger_seats_count)

    @classmethod
    def instance(cls, row):
        return cls(
            row[cls.csv_brand],
            row[cls.csv_photo_file_name],
            row[cls.csv_carrying],
            row[cls.csv_passenger_seats_count],
        )


class Truck(CarBase):
    car_type = 'truck'

    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        try:
            length, width, height = (float(c) for c in body_whl.split('x', 2))
        except ValueError:
            length, width, height = .0, .0, .0

        self.body_length = length
        self.body_width = width
        self.body_height = height

    def get_body_volume(self):
        return self.body_width * self.body_height * self.body_length

    @classmethod
    def instance(cls, row):
        return cls(
            row[cls.csv_brand],
            row[cls.csv_photo_file_name],
            row[cls.csv_carrying],
            row[cls.csv_body_whl],
        )


class SpecMachine(CarBase):
    car_type = 'spec_machine'

    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra

    @classmethod
    def instance(cls, row):
        return cls(
            row[cls.csv_brand],
            row[cls.csv_photo_file_name],
            row[cls.csv_carrying],
            row[cls.csv_extra],
        )

def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename, encoding='utf-8') as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';', )
        next(reader)
        for row in reader:
            if len(row) == 7:
                car_type, brand, passenger_seats_count, photo_file_name, body_whl, carrying, extra = row
                if row[0] == 'car' and all((brand, photo_file_name, passenger_seats_count)):
                    try:
                        car = Car(brand=row[1], photo_file_name=row[3], carrying=row[5], passenger_seats_count=row[2])
                        car_list.append(car)
                    except ValueError:
                        pass
                elif row[0] == 'truck' and all((brand, photo_file_name)):
                    try:
                        car = Truck(brand=row[1], photo_file_name=row[3], body_whl=row[4], carrying=row[5])
                        car_list.append(car)
                    except ValueError:
                        pass
                elif row[0] == 'spec_machine' and all((brand, photo_file_name, extra)):
                    try:
                        if '.png' in photo_file_name or '.gif' in photo_file_name or '.jpeg' in photo_file_name or '.jpg' in photo_file_name:
                            car = SpecMachine(brand=row[1], photo_file_name=row[3], carrying=row[5], extra=row[6])
                            car_list.append(car)
                        else:
                            raise ValueError
                    except ValueError:
                        continue
    return car_list
