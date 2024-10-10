import json
from datetime import date

with open("rented_cars.json", "r") as file:
    transactions = json.load(file)
from backend_clients import client_search, add_client, client
from backend_cars import cars, add_car, car_search


def transaction_to_list(ids, customer, dnes, days, deposit, paid, status):
    transactions[ids] = {}
    transactions[ids]['client'] = customer
    transactions[ids]['date'] = dnes
    transactions[ids]['days'] = days
    transactions[ids]['deposit'] = deposit
    transactions[ids]['paid'] = paid
    transactions[ids]['status'] = status



car_deposit = 800
car_to_rent = ''
customer_who_rent = ''
#transactions = {}


#if len(cars) == 0:
   # add_car()


def list_cars ():
    while True:
        try:
            ans = input(f'Please enter car ID or A to view all cars:').upper()
            if ans == 'A' or ans == 'ALL':
                for key, value in cars.items():

                    if isinstance(value, dict):
                        print(
                            f'car with ID: {key}, {cars[key]["brand"]} {cars[key]["model"]} for {cars[key]["price"]}lv. per day is {cars[key]["status"]}')
                    else:
                        print(f'  {value}')
                break
            else:
                car_search(ans)
                if cars[ans]['status'] == 'Rented':
                    print(f'The car already rented.')
                    while True:
                        try:
                            ans1 = input(f'Do you want to rent other car? Y/N:').upper()
                            if ans1 == 'Y' or ans1 == 'YES':

                                #print(cars) #-да се активира ако има грешка за тестови данни
                                break
                            elif ans1 == 'N' or ans1 == 'NO':
                                record = True
                                print(f'Bye!')
                                break
                            else:
                                print("Please enter valid choice Y/N!")
                        except ValueError:
                            print("Please enter valid choice Y/N!")

                break
        except ValueError:
            print(f"Please enter valid choice Y/N!")


def rent_a_car ():
    global car_deposit
    while True:
        try:
            while True:
                car_to_rent = input(f'Please enter the ID of the car you want to rent:')
                if cars[car_to_rent]['status'] == 'Rented':
                    print(f'The car is already rented! Try another car!')
                    continue
                else:
                    car_search(car_to_rent)
                    break


            customer_who_rent = input(f'Please enter the ID of the customer who wants to rent the car:')
            #print(client_search(customer_who_rent))
            if client_search(customer_who_rent):
                print(f'Customer not exist. Please enter the customer details:')
                add_client(customer_who_rent)
                break
            else:
                print(f'Client with ID: {customer_who_rent}, {client[customer_who_rent]["name"]} {client[customer_who_rent]["address"]} is {client[customer_who_rent]["age"]} old and status {client[customer_who_rent]["status"]} driver')
                break
        except ValueError:
            print(f"Please enter valid ID!")

    day_price = float(cars[car_to_rent]['price'])

    while True:
        try:
            days_to_rent = int(input(f'Please enter how many days you want to rent the car:'))
            break
        except ValueError:
            print(f"Please enter integer number!")
    rent_to_pay = days_to_rent * day_price
    if client[customer_who_rent]['status'] != 'Normal':
        car_deposit += car_deposit * 0.3
    while True:
        try:
            ins_confirm = input(f'Would you like insurance covering damages incurred during the rental:Y/N?').upper()
            if ins_confirm == 'Y' or ins_confirm == 'N':
                break
            else:
                print(f'Please enter valid choice Y/N!')
        except ValueError:
            print(f'Please enter valid choice Y/N!')
    if ins_confirm == 'Y':
        car_deposit = car_deposit  / 2
    while True:
        try:
            out_confirm = input(
                f'Do you plan to drive the rental car outside the country during the rental period? Y/N:').upper()
            if out_confirm == 'Y':
                rent_to_pay += 160
                break
            elif out_confirm == 'N':
                print(f'If you leave the country with the rented car, illegally, you owe a fine of BGN 600!')
                break
            else:
                print(f'Please enter valid choice Y/N!')
        except ValueError:
            print(f'Please enter valid choice Y/N!')
    trans_id = car_to_rent
    while True:
        try:
            outside_eu = input(f'Is your driving license issued by a non-EU country? Y/N').upper()
            if outside_eu == 'Y' or outside_eu == 'YES':
                print(
                    f'You have a permit to drive for up to 90 days on the territory of the country,\nstarting from the date of your entry into the country.')
                break
            elif outside_eu == 'N' or outside_eu == 'NO':
                break
            else:
                print(f'Please enter valid choice Y/N!')
        except ValueError:
            print(f'Please enter valid choice Y/N!')
    while True:
        try:
            prepayment = float(input(f'Please enter the amount of advance payment. Enter 0 (zero) if none:'))
            rent_to_pay -= prepayment
            break
        except ValueError:
            print(f"Please enter integer number!")

    print(
        f'Rent Amount:BGN {rent_to_pay:.2f} Deposit:BGN {car_deposit:.2f} Total Amount to Pay:BGN {(rent_to_pay + car_deposit):.2f}')
    while True:
        try:
            ans = input(f'Do You want to save the transaction\'s data? Y/N:').upper()
            if ans == 'Y' or ans == 'YES':
                transaction_status = 'Active'
                day_of_rent = str(date.today())
                transaction_to_list(trans_id, customer_who_rent,day_of_rent, days_to_rent, car_deposit, rent_to_pay, transaction_status)
                cars[car_to_rent]['status'] = 'Rented'
                trans_id = days_to_rent = car_deposit = rent_to_pay = transaction_status = ''
                customer_who_rent = car_to_rent = day_of_rent = ''
                #print(transactions) #-да се активира ако има грешка за тестови данни
                #print((cars[car_to_rent])) #-да се активира ако има грешка за тестови данни
                break
            elif ans == 'N' or ans == 'NO':
                trans_id = days_to_rent = car_deposit = rent_to_pay = transaction_status = ''
                customer_who_rent = car_to_rent = day_of_rent = ''
                #print(transactions) #-да се активира ако има грешка за тестови данни
                break
            else:
                print(f'Please enter valid choice Y/N!')
        except ValueError:
            print(f'Please enter valid choice Y/N!')



def return_car():
    while True:
        try:
            car_to_return = input("Please enter the ID of the car you are returning: ")
            if cars[car_to_return]['status'] != 'Rented' and transactions[car_to_return]['status'] != "Active":
                print(f'The car is not rented! Try another car! ')
                continue
            else:
                car_search(car_to_return)
                break
        except ValueError:
            print(f"Please enter valid ID!")

    return_price = 0

    while True:
        try:
            same_point = input(f"Is the car returned to the same location from which it was rented? Y/N: ").upper()
            if same_point == 'Y' or same_point == 'YES':
                break
            elif same_point == 'N' or same_point == 'NO':
                print(f"A fee of BGN 100 will be charged for a one-way rental. ")
                return_price += 100
                break
            else:
                print(f'Please enter valid choice Y/N! ')
        except ValueError:
            print(f'Please enter valid choice Y/N! ')

    while True:
        try:
            full_tank = input(f"Is the vehicle returned with a full tank/battery? Y/N: ").upper()
            if full_tank == 'Y' or full_tank == 'YES':
                break
            elif full_tank == 'N' or full_tank == 'NO':
                while True:
                    try:
                        electric_car = input(f"Is the car electric? Y/N: ").upper()
                        if electric_car == 'Y' or electric_car == 'YES':
                            print(
                                f"You will be charged an administrative fee of BGN 30 plus\nBGN 1 for each kWh required to fully charge the battery. ")
                            kwh_needed = int(input(f"Please enter how many kWh are needed to charge the battery: "))
                            return_price += kwh_needed
                            break
                        elif electric_car == 'N' or electric_car == 'NO':
                            print(
                                f"You will be charged an administrative fee of BGN 30 plus\nBGN 2,90 for each liter of fuel required to fill the tank. ")
                            fuel_needed = int(input(f"Please enter how many liters of fuel are required: "))
                            return_price += fuel_needed * 2.9
                            return_price += 30
                            break
                        else:
                            print(f'Please enter valid choice Y/N!')
                    except ValueError:
                        print(f'Please enter valid choice Y/N!')
                break
            else:
                print(f'Please enter valid choice Y/N!')
        except ValueError:
            print(f'Please enter valid choice Y/N!')

    while True:
        try:
            damages = input(f"Is there damage to the vehicle, due to the customer's fault? Y/N: ").upper()
            if damages == 'Y' or damages == 'YES':
                print(f"Since there is damage to the car through your fault, the deposit will not be refunded!")
                cust_id = transactions[car_to_return]["client"]
                customer_stat = 'Risky'
                break
            elif damages == 'N' or damages == 'NO':
                break
            else:
                print(f'Please enter valid choice Y/N!')
        except ValueError:
            print(f'Please enter valid choice Y/N!')

    if return_price != 0:
        print(
            f'You owe BGN {return_price:.2f} for non-compliance with the terms of the contract and/or damage to the car')

    while True:
        try:
            ans = input(f'Do You want to save the transaction\'s data? Y/N: ').upper()
            if ans == 'Y' or ans == 'YES':
                cars[car_to_return]['status'] = 'Available'
                if damages == 'Y' or damages == 'YES':
                    client[cust_id]["status"] = customer_stat
                transactions[car_to_return]["status"] = 'Closed'
                print(transactions[car_to_return])  # -да се активира ако има грешка за тестови данни
                print((cars[car_to_return]))# -да се активира ако има грешка за тестови данни
                print(client[cust_id])
                break
            elif ans == 'N' or ans == 'NO':

                break
            else:
                print(f'Please enter valid choice Y/N!')
        except ValueError:
            print(f'Please enter valid choice Y/N!')
