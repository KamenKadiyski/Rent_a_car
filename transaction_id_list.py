from datetime import date
def id_generate(car_id, client_id) -> str:
    trans_list = [car_id, client_id]
    #car_id = input()
    #client_id = input()
    day_of_rent = str(date.today())
    trans_list.append(day_of_rent)
    trans_id = ':'.join(trans_list)
    return trans_id
def info_from_id(trans_id):
    trans_list = trans_id.split(':')
    car_id = trans_list[0]
    client_id = trans_list[1]
    day_of_rent = trans_list[2]
    return car_id, client_id, day_of_rent
