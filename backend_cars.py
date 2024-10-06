


def car_search(car_num):
    for car in cars.keys():
        if car_num in cars:
            print(f'car with ID: {car_num}, {cars[car_num]['brand']} {cars[car_num]['model']} for {cars[car_num]['price']}lv. per day is {cars[car_num]['status']}')
            break
        else:
            print(f'car not exist')
            break


def add_to_list(ids, brand, model, price, status):
    cars[ids] = {}
    cars[ids]['brand'] = brand
    cars[ids]['model'] = model
    cars[ids]['price'] = price
    cars[ids]['status'] = status


def car_exists(cars_dict, key):
    if key in cars_dict:
        return True
    for value in cars_dict.values():
        if isinstance(value, dict):
            if car_exists(value, key):
                return True
    return False


cars = {}


def add_car():
    record = False
    car_id = ''
    while not record:
        car_found = True
        while car_found:
            car_id = input(f'Insert car ID:')
            car_found = car_exists(cars, car_id)
            if car_found == False:
                break
            else:
                print(f'Car already exists! Try again!')

        car_brand = input(f'Insert brand:')
        car_model = input(f'Insert model:')
        rent_price = input(f'Insert rent price per day:')
        car_status = 'Available'
        while True:
            try:
                ans = input(f'Do You want to save the car\'s data? Y/N:').upper()
                if ans == 'Y' or ans == 'YES':
                    add_to_list(car_id, car_brand, car_model, rent_price, car_status)
                    print(cars)
                    break
                elif ans == 'N' or ans == 'NO':
                    car_id = car_brand = car_model = rent_price = car_status = ''
                    print(cars)
                    break
                else:
                    print("Please enter valid choice Y/N!")
            except ValueError:
                print("Please enter valid choice Y/N!")
        while True:
            try:
                ans1 = input(f'Next car? Y/N:').upper()
                if ans1 == 'Y' or ans1 == 'YES':
                    car_id = car_brand = car_model = rent_price = car_status = ''
                    print(cars)
                    break
                elif ans1 == 'N' or ans1 == 'NO':
                    record = True
                    print(cars)
                    break
                else:
                    print("Please enter valid choice Y/N!")
            except ValueError:
                print("Please enter valid choice Y/N!")



#add_car()
# речник създаден само за целите на тестване на сорса
cars = {'123': {'brand': 'ALfa', 'model': 'Mito', 'price': '10', 'status': 'Available'}, '234': {'brand': 'Citroen', 'model': 'C5', 'price': '20', 'status': 'Available'}, '345': {'brand': 'Honda', 'model': 'Civic', 'price': '15', 'status': 'Rented'}, '654': {'brand': 'Toyota', 'model': 'Rav4', 'price': '30', 'status': 'Available'}}
#search_car = input(f'Insert car Id:')
#car_search(search_car)
