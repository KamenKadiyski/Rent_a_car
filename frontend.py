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


def display_cars(cars):
    print("\nAvailable Cars:")
    for car in cars:
        status = "Available" if car["available"] else "Rented"
        print(f"ID: {car['id']} - {car['brand']} {car['model']} - ${car['rental_price']}/day - {status}")


def client_panel(cars):
    while True:
        option = main_menu_client()
        if option == "1":
            display_cars(cars)
        elif option == "2":
            print("Renting a car functionality.")

        elif option == "3":
            print("Returning a car functionality.")

        elif option == "4":
            break
        else:
            print("Invalid option, please try again.")


def admin_panel(cars):
    while True:
        option = main_menu_admin()
        if option == "1":
            print("Enter new car functionality.")

        elif option == "2":
            print("Changing data for existing car functionality.")

        elif option == "3":
            print("Removing a car functionality.")

        elif option == "4":
            break
        else:
            print("Invalid option, please try again.")


def main():
    cars = [
        {"id": 1, "brand": "Toyota", "model": "Corolla", "rental_price": 50, "available": True},
        {"id": 2, "brand": "Ford", "model": "Fiesta", "rental_price": 45, "available": False},
    ]

    while True:
        panel_choice = main_menu()

        if panel_choice == "admin":
            admin_panel(cars)
        elif panel_choice == "client":
            client_panel(cars)
        elif panel_choice == "exit":
            exit_menu()
            break
        else:
            print("Wrong input! Please select an option again.")


if __name__ == "__main__":
    main()

