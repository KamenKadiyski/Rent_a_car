from backend_cars import add_car
from rent_a_car import list_cars, rent_a_car

# frontend.py, който ти написа съм го прекръстил на
# frontend_old.py и съм добавил нов, в който са нещата
# които съм добавил аз към това, което ти си написла
#Разгледай ги и двата. Тествай как върви frontend_new.py,
#разгледай какво и как се случва.
#Ако забележиш нещо, добави или кажи да изчистя като грешка



def main_menu():
    print("Welcome to RentACar Turtle Team!")
    print("Do you want to go into the Admin panel or in the Client panel?")
    return input("Please choose an option (Admin, Client or Exit): ").lower()


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
    return None


def display_cars():
    print("\nAvailable Cars:")
    list_cars()
    #for car in cars:
    #    status = "Available" if car["available"] else "Rented"
    #    print(f"ID: {car['id']} - {car['brand']} {car['model']} - ${car['rental_price']}/day - {status}")


def client_panel():
    while True:
        try:
            option = main_menu_client()
            if option == "1":
                display_cars()
            elif option == "2":
                print("Renting a car functionality.")
                rent_a_car()
            elif option == "3":
                print("Returning a car functionality.")

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
                add_car()

            elif option == "2":
                print("Changing data for existing car functionality.")

            elif option == "3":
                print("Removing a car functionality.")

            elif option == "4":
                break
            else:
                print("Invalid option, please try again.")
        except ValueError:
            print("Invalid option, please try again.")


def main():
   # cars = [
   #     {"id": 1, "brand": "Toyota", "model": "Corolla", "rental_price": 50, "available": True},
   #     {"id": 2, "brand": "Ford", "model": "Fiesta", "rental_price": 45, "available": False},
    #]

    while True:
        try:
            panel_choice = main_menu()

            if panel_choice == "admin":
                admin_panel()
            elif panel_choice == "client":
                client_panel()
            elif panel_choice == "exit":
                exit_menu()
                break
            else:
                print("Wrong input! Please select an option again.")
        except ValueError:
            print("Wrong input! Please select an option again.")


if __name__ == "__main__":
    main()

