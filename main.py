from rental_car_planner_classes import *

cars = []
cars.append(Luxury_car("Urus", 7, 300, 50, False))
cars.append(Luxury_car("BMW M5", 9, 200, 30, True))
cars.append(SUV("Hyundai ix35", 12, 100, 10, 1000))
cars.append(Compact_car("Volkswagen Beetle", 11, 115, 5, "Manual"))

garage = []
garage.append(Garage("Gangnam Garage"))
garage.append(Garage("Yeoksam Garage"))
for i in range(2):
    for j in range(4):
        garage[i].add_car(cars[j])

garage[0].remove_car(cars[1])
garage[1].remove_car(cars[0])

destination_list = []
destination_list.append(Destination("Busan", 400))
destination_list.append(Destination("Gwangju", 300))
destination_list.append(Destination("Daegu", 285))

def car_selection(garage):
    print("Select a garage")
    for i in range(2):
        garage[i].display()

    garage_choice = int(input('\nEnter the garage number:'))
    garage_choice -= 1
    garage_chosen = garage[garage_choice]

    print("Select a car")
    garage_chosen.display_cars()

    car_choice = int(input('\nEnter the car number you would like to rent: '))

    valid(car_choice)
    #TODO fix valid car choice. Different length
    car_choice -= 1
    car = garage[garage_choice].garage[car_choice]

    name = car.get_name()
    fuel_efficiency = car.get_fuel_efficiency()
    max_speed = car.get_max_speed()
    price_per_hour = car.get_price_per_hour()

    return garage_choice, car_choice, name, fuel_efficiency, max_speed, price_per_hour

def destination_selection(p_destination):
    print("Select a destination: ")
    for i in range(3):
        p_destination[i].display()

    destination_choice = int(input('\nEnter the Destination number of where you would like to go: '))
    valid(destination_choice)
    destination_choice = destination_choice - 1

    destination_object = p_destination[destination_choice]

    destination = destination_object.get_name()
    distance = destination_object.get_distance()

    return destination_choice, destination, distance

def units(price_fuel):
    chosen_units = False
    while not chosen_units:
        units = input("Would you like to use imperial or metric units?")
        units = units.lower()
        if units == "imperial":
            price_fuel = imperial_to_metric(price_fuel)
            return price_fuel
        elif units != "metric":
            print("invalid input")
            continue
        else:
            return price_fuel

def imperial_to_metric(price_fuel):
    price_fuel = price_fuel/3.785
    return price_fuel

def travel_time(distance, max_speed, time_allowed):
    time = distance/max_speed
    time = float((f"{time:.2f}"))
    print("it will take:", time, "hours")
    if time_allowed < time:
        try_again = int(input("The trip will take too long. Quit the program or try again. Input 1 to quit or 2 to try again."))
        if try_again == 1:
            quit()
        elif try_again == 2:
            return -1
    else:
        print("There is enough time.")

    return time

def valid(value):
    valid = False
    while not valid:
        if value == 1 or value == 2 or value == 3:
            valid = True
        else:
            value = int(input("Invalid. Input 1, 2 or 3: "))
            valid = False

chosen = False
while not chosen:
    destination_choice, destination, distance = destination_selection(destination_list)
    print("\nYou have chosen", destination, "which is", distance, "km away.\n")

    garage_choice, car_choice, name, fuel_efficiency, max_speed, price_per_hour = car_selection(garage)
    chosen_car = garage[garage_choice].garage[car_choice]
    print("You have chosen:")
    chosen_car.display()

    num_passengers = int(input("How many passengers will there be?"))
    if not chosen_car.can_carry(num_passengers):
        print("Not enough seats in the car")
        continue
    print("Enough seats in car")

    time_allowed = float(input("how long do you have to travel(in hours)?"))

    time = travel_time(distance, max_speed, time_allowed)
    if time == -1:
        continue

    price_fuel = float(input("\nHow much does fuel cost per litre or gallon? "))
    price_fuel = units(price_fuel)

    price = (distance / fuel_efficiency) * price_fuel
    price = f"{price:.2f}"
    vehicle_price = price_per_hour * time
    vehicle_price = f"{vehicle_price:.2f}"
    print("\nFuel Price: ", price)
    print("Price for vehicle: ", vehicle_price)
    chosen = True
