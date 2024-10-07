def client_search(client_num):
    #missing = False
    for cl in client.keys():
        if client_num in client:
            missing = False
            #return_msg = f'Client with ID: {client_num}, {client[client_num]['name']} {client[client_num]['address']} is {client[client_num]['age']} old and status {client[client_num]['status']} driver'
            break
        else:
            #return_msg = f'Client not exist. Please enter the customer details:'
            missing = True
            break
    return missing #return_msg



def client_to_list(ids, name, address, age, status):
    client[ids] = {}
    client[ids]['name'] = name
    client[ids]['address'] = address
    client[ids]['age'] = age
    client[ids]['status'] = status


def client_exists(client_dict, key):
    if key in client_dict:
        return True
    for value in client_dict.values():
        if isinstance(value, dict):
            if client_exists(value, key):
                return True
    return False


client = {}


def add_client(client_id):
    record = False
    #client_id = ''
    while not record:
        client_found = True
        while client_found:
            #client_id = input(f'Insert client ID:')
            client_found = client_exists(client, client_id)
            if not client_found:
                break
            else:
                print(f'Client already exists! Try again!')
                break
        print(f'Client ID:{client_id}')
        client_name = input(f'Insert client name:')
        client_adderss = input(f'Insert client address:')
        while True:
            try:
                client_ages = input(f"Insert client's ages:")
                if int(client_ages) >= 18:
                    break

                else:
                    print("The customer is not old enough to rent a car!")
            except ValueError:
                print("Please enter valid choice!")
        client_status = 'Normal'
        while True:
            try:
                ans = input(f'Do You want to save the client\'s data? Y/N:').upper()
                if ans == 'Y' or ans == 'YES':
                    client_to_list(client_id, client_name, client_adderss, client_ages, client_status)
                    print(client)
                    break
                elif ans == 'N' or ans == 'NO':
                    client_id = client_name = client_adderss = client_ages = client_status = ''
                    print(client)
                    break
                else:
                    print("Please enter valid choice Y/N:")
            except ValueError:
                print("Please enter valid choice Y/N:")

        while True:
            try:
                ans1 = input(f'Next client? Y/N:').upper()
                if ans1 == 'Y' or ans1 == 'YES':
                    client_id = client_name = client_adderss = client_ages = client_status = ''
                    print(client)
                    break
                elif ans1 == 'N' or ans1 == 'NO':
                    record = True
                    print(client)
                    break
                else:
                    print("Please enter valid choice Y/N!")
            except ValueError:
                print("Please enter valid choice Y/N!")


# речник създаден само за целите на тестване на сорса
client = {'123': {'name': 'Kamen', 'address': 'Varna', 'age': '45', 'status': 'Normal'}, '234': {'name': 'Vili', 'address': 'Maidstone', 'age': '34', 'status': 'Normal'}, '345': {'name': 'Ralitsa', 'address': 'Sofia', 'age': '32', 'status': 'Normal'}}
#add_client()
#search_client = input(f'Insert client Id:')
#client_search(search_client)