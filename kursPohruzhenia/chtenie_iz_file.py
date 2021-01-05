from kursPohruzhenia.klassi_i_nasledovanie import *
cars = get_car_list('car.csv')
print(len(cars))
for c in cars:
    print(c.__dict__)
    print(c.get_photo_file_ext())







#print(cars[0].brand, cars[0].photo_file_name, cars[0].carrying, cars[0].passenger_seats_count)
#print(cars[1].brand, cars[1].photo_file_name, cars[1].carrying, cars[1].body_whl)
#print(cars[2].brand, cars[2].photo_file_name, cars[2].carrying, cars[2].body_whl)
#print(cars[3].brand, cars[3].photo_file_name, cars[3].carrying, cars[3].passenger_seats_count)
#print(cars[4].brand, cars[4].photo_file_name, cars[4].carrying, cars[4].extra)
