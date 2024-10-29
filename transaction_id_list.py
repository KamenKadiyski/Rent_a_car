from datetime import date
def id_generate(car_id, client_id) -> str:
    trans_list = [car_id, client_id]
    #car_id = input()
    #client_id = input()
    day_of_rent = str(date.today())
    trans_list.append(day_of_rent)
    trans_id = ':'.join(trans_list)
    return trans_id