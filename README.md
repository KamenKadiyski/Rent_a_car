`Task: Platform for rent-a-car`

The project simulates the process of renting and returning rental cars.

It includes the following panels and their features:
1. Admin panel
   
    1.1 Entering a car - When entering data for a new car, check if it does not already exist.
   
    1.2 Change of vehicle data
   
    1.3 Deleting a Vehicle
   
2. Client panel
   
    2.1. Browse cars - see all available cars
   
    2.2. Car rental
        If the customer has already used the services, their data should be filled in automatically.
        If the customer has a driver's license issued by a country outside the EU, they should not be allowed to rent a car for more than 90 days.
        To calculate the rental amount for the period and the full amount, including the deposit, payable on the car rental.
        If the client adds insurance - the deposit will be reduced.
        If he is a regular customer / more than 3 rentals / to have the opportunity to give him a discount on the rental price per day.
        It is assumed that the user may have made a pre-booking and made a partial pre-payment. *
        It is allowed that the user can leave the country, for which a fee of BGN 160 is provided. *

    2.3. Returning a car
        When returning the car, check whether there is damage and, if there is, depending on whether there is insurance, determine whether to return the deposit or only part of it.
        When returning a car, check if the car is returned with a full tank and if not - charge a fee. * Price per liter of fuel BGN 2.90/l + BGN 30 admin fee. Electricity - BGN 1/kWh + BGN 30 admin fee.
        Fee for being late for more than an hour - one rental day. Each subsequent day started is charged with a full rental day*

5. Exiting the system - when exiting the system, it is required to refresh and close all files opened during the work with the system.*



QA guidelines:

To check whether the age of the customer is over 18 years, when entering data for a new customer.

Don't give an opportunity to rent a car that has already been rented out

Not allowing the car return function to be performed if it is not rented

The program should not react when entering an option that does not exist in the menu.

Do not respond until the choice expected by the client is entered, when choosing between Y/N and accepting both lowercase and uppercase letters.


*  updated
