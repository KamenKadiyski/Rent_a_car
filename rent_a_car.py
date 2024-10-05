from backend_clients import client_search, add_client, client
from backend_cars import cars, add_car, car_search
def transaction_to_list(ids, days, deposit, paid, status):
    transactions[ids] = {}
    transactions[ids]['days'] = days
    transactions[ids]['deposit'] = deposit
    transactions[ids]['paid'] = paid
    transactions[ids]['status'] = status
car_deposit = 800
car_to_rent = ''
customer_who_rent = ''
transactions = {}
if len(cars) == 0:
    add_car()
while True:
    try:
        ans = input(f'Please enter car ID or A to view all cars:').upper()
        if ans == 'A' or ans == 'ALL':
            for key, value in cars.items():

                if isinstance(value, dict):
                    print(
                        f'car with ID: {key}, {cars[key]['brand']} {cars[key]['model']} for {cars[key]['price']}lv. per day is {cars[key]['status']}')
                else:
                    print(f'  {value}')
                #break
        else:
            car_search(ans)
            if cars[ans]['status'] == 'Rented':
                print(f'The car already rented.')
                while True:
                    try:
                        ans1 = input(f'Do you want to rent other car? Y/N:').upper()
                        if ans1 == 'Y' or ans1 == 'YES':

                            print(cars)
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
while True:
    try:
        car_to_rent = input(f'Please enter the ID of the car you want to rent:')
        car_search(car_to_rent)
        customer_who_rent = input(f'Please enter the ID of the customer who wants to rent the car:')
        client_search(customer_who_rent)
        if client_search(customer_who_rent):
            add_client()
        break
    except ValueError:
        print(f"Please enter valid ID!")


day_price = int(cars[car_to_rent]['price'])

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
    car_deposit -= car_deposit * 0.5
while True:
    try:
        out_confirm = input(f'Do you plan to drive the rental car outside the country during the rental period? Y/N:').upper()
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
trans_id = car_to_rent + ':' + customer_who_rent
while True:
    try:
        outside_eu = input(f'Is your driving license issued by a non-EU country? Y/N').upper()
        if outside_eu == 'Y' or outside_eu == 'YES':
            print(f'You have a permit to drive for up to 90 days on the territory of the country,\nstarting from the date of your entry into the country.')
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

print(f'Rent Amount:BGN {rent_to_pay:.2f} Deposit:BGN {car_deposit:.2f} Total Amount to Pay:BGN {(rent_to_pay+car_deposit):.2f}')
while True:
    try:
        ans = input(f'Do You want to save the transaction\'s data? Y/N:').upper()
        if ans == 'Y' or ans == 'YES':
            transaction_status = 'Active'
            transaction_to_list(trans_id, days_to_rent, car_deposit, rent_to_pay,transaction_status)
            print(transactions)
            break
        elif ans == 'N' or ans == 'NO':
            trans_id = days_to_rent = car_deposit = rent_to_pay = transaction_status = ''
            print(transactions)
            break
        else:
            print(f'Please enter valid choice Y/N!')
    except ValueError:
        print(f'Please enter valid choice Y/N!')
