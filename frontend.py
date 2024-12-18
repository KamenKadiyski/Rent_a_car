import json

from backend_clients import client
from backend_cars import add_car, car_del, car_detail_change, cars, car_search
from rent_a_car import (list_cars, rent_a_car, transactions, return_car)


#admin_panel option 2 and 3 : тук съм добавила опции за премахване и промяна, да се свържат с backend

def main_menu():
    try:
        print("Welcome to RentACar Turtle Team!")
        print("Which menu do you want to enter?")
        print("1. Admin panel")
        print("2. Client panel")
        print("3. Exit")
        return input("Please choose an option (1-3): ")
    except ValueError:
        print("Invalid option, please try again.")


def main_menu_client():
    print("\nClient Menu: ")
    print("1. View Cars")
    print("2. Rent a Car")
    print("3. Return a Car")
    print("4. Exit")
    return input("Please choose an option (1-4): ")


def main_menu_admin():
    print("\nAdmin Menu: ")
    print("1. Enter new car")
    print("2. Change data for already existing car")
    print("3. Remove a car from the menu")
    print("4. Exit")
    return input("Please choose an option (1-4): ")


def exit_menu():
    print("Thank you for using RentACar Turtle Team! \nHave a great day!")
    try:
        with open("clients_data.json", "w", encoding="utf-8") as f1:
            json.dump(client, f1, ensure_ascii=False, indent=4)
        with open("cars_data.json", "w", encoding="utf-8") as f2:
            json.dump(cars, f2, ensure_ascii=False, indent=4)
        with open("transactions.json", "w", encoding="utf-8") as f3:
            json.dump(transactions, f3, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Error: {e}")


    return None


def display_cars():
    print("\nAvailable Cars:")
    list_cars()


def client_panel():
    while True:
        try:
            option = main_menu_client()
            if option == "1":
                display_cars()
            elif option == "2":
                print("Renting a car functionality.")
                #while not car_search:
                car_for_rent  = input(f'Please enter the ID of the car you want to rent:')
                if not car_search(car_for_rent):
                    #print(f'The car does not exist in the database!')
                    continue
                else:
                    rent_a_car(car_for_rent)
            elif option == "3":
                print("Returning a car functionality.")
                return_car_id = input("Please enter car ID: ")
                if not car_search(return_car_id):
                    continue
                else:
                    return_car(return_car_id)
                # to add functionality here
            elif option == "4":
                break
            else:
                print("Invalid option, please try again.")
        except ValueError:
            print("Invalid option, please try again.")


def admin_panel():
    while True:
        try:
            option = main_menu_admin()
            if option == "1":
                print("Enter new car functionality.")
                add_car() # to review it

            elif option == "2":
                print("Changing data for existing car functionality.")
                car_id_to_be_changed = input("Please select for which car ID you want to make changes: ")
                if car_search(car_id_to_be_changed):
                    print("What do you want to change?")
                    print("1. Price")
                    print("2. Scrap car")

                    car_changes = input("Please select option from the list above (1-2)")
                    try:
                        if car_changes == "1":
                            car_detail_change(car_changes,car_id_to_be_changed)
                        elif car_changes == "2":
                            car_detail_change(car_changes,car_id_to_be_changed)


                    except ValueError:
                        print("Invalid option, please try again.")

                # to complete

            elif option == "3":
                print("Removing a car functionality.")
                car_id_to_be_removed = input("Please select which car ID you want to remove: ")
                car_del(car_id_to_be_removed)
                # to complete
            elif option == "4":
                break
            else:
                print("Invalid option, please try again.")
        except ValueError:
            print("Invalid option, please try again.")


def main():




    while True:
        try:
            panel_choice = main_menu()

            if panel_choice == "1":
                admin_panel()
            elif panel_choice == "2":
                client_panel()
            elif panel_choice == "3":
                exit_menu()
                break
            else:
                print("Wrong input! Please select an option again.")
        except ValueError:
            print("Wrong input! Please select an option again.")


if __name__ == "__main__":
    main()

