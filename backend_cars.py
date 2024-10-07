


def car_search(car_num):
    for car in cars.keys():
        if car_num in cars:
            print(f'car with ID: {car_num}, {cars[car_num]['brand']} {cars[car_num]['model']} for BGN{cars[car_num]['price']} per day is {cars[car_num]['status']}')
            break
        else:
            print(f'Car with {car_num} not exists!')
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
            if not car_found:
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
                    # print(cars) #-да се активира ако има грешка за тестови данни
                    break
                elif ans == 'N' or ans == 'NO':
                    car_id = car_brand = car_model = rent_price = car_status = ''
                    # print(cars) #-да се активира ако има грешка за тестови данни
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
                    # print(cars) #-да се активира ако има грешка за тестови данни
                    break
                elif ans1 == 'N' or ans1 == 'NO':
                    record = True
                    # print(cars) #-да се активира ако има грешка за тестови данни
                    break
                else:
                    print("Please enter valid choice Y/N!")
            except ValueError:
                print("Please enter valid choice Y/N!")

def car_del (car_id):
    #car_search(car_id)
    if cars[car_id]["status"] == "Rented":
        print(f"The car with ID {car_id} is rented out! You cannot delete the car from the database!")
    else:
        while True:
            try:
                ans1 = input(f'Are you sure you want to delete this car? Y/N:').upper()
                if ans1 == 'Y' or ans1 == 'YES':
                    del cars[car_id]
                    #print(cars) #-да се активира ако има грешка за тестови данни
                    break
                elif ans1 == 'N' or ans1 == 'NO':
                    # print(cars) #-да се активира ако има грешка за тестови данни
                    break
                else:
                    print("Please enter valid choice Y/N!")
            except ValueError:
                print("Please enter valid choice Y/N!")

def car_detail_change(car_changes,car_id):
    if car_changes == '1':
        while True:
            try:
                new_price = float(input(f'Please enter the new rental price of the car:'))
                break
            except ValueError:
                print("Please enter valid choice Y/N!")
        while True:
            try:
                ans1 = input(f'Are you sure you want to change the rental price? Y/N:').upper()
                if ans1 == 'Y' or ans1 == 'YES':
                    cars[car_id]['price'] = str(new_price)
                    # print(cars[car_id]) - #-да се активира ако има грешка за тестови данни
                    break
                elif ans1 == 'N' or ans1 == 'NO':
                    # print(cars[car_id]) #-да се активира ако има грешка за тестови данни
                    break
                else:
                    print("Please enter valid choice Y/N!")
            except ValueError:
                print("Please enter valid choice Y/N!")



    elif car_changes == '2':
        if cars[car_id]["status"] == "Rented":
            print(f"The car with ID {car_id} is rented out! You cannot scrap the car!")
        else:
            while True:
                try:
                    ans1 = input(f'Are you sure you want to scrap this car? Y/N:').upper()
                    if ans1 == 'Y' or ans1 == 'YES':
                        cars[car_id]['status'] = 'Scrapped'
                        #print(cars[car_id]) #-да се активира ако има грешка за тестови данни
                        break
                    elif ans1 == 'N' or ans1 == 'NO':
                        #print(cars[car_id]) #- да се активира ако има грешка за тестови данни
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
