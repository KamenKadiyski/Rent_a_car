def client_search(client_num):
    for cl in client.keys():
        if client_num in client:
            print(f'Client with ID: {client_num}, {client[client_num]['name']} {client[client_num]['address']} is {client[client_num]['age']} old and status {client[client_num]['status']} driver')
            break
        else:
            print(f'Client not exist')
            break

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

def add_client():
    record = False
    client_id = ''
    while not record:
        client_found = True
        while client_found:
            client_id = input(f'Insert client ID:')
            client_found = client_exists(client, client_id)
            if not client_found:
                break
            else:
                print(f'Client already exists! Try again!')

        client_name = input(f'Insert client name:')
        client_adderss = input(f'Insert client address:')
        client_ages = input(f"Insert client's ages:")
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


add_client()
search_client = input(f'Insert client Id:')
client_search(search_client)

# test test