class Cars:
    car_number = 1
    def __init__(self, name, fuel_efficiency, max_speed, price_per_hour):
        self.car_number = Cars.car_number
        self.name = name
        self.fuel_efficiency = fuel_efficiency
        self.max_speed = max_speed
        self.price_per_hour = price_per_hour
        Cars.car_number +=1

    def display(self):
        print("Car Number:", self.car_number, "Car:", self.name, "Fuel Efficiency:", self.fuel_efficiency, "max speed:", self.max_speed, "price per hour:", self.price_per_hour)

    def get_name(self):
        return self.name

    def get_fuel_efficiency(self):
        return self.fuel_efficiency

    def get_max_speed(self):
        return self.max_speed

    def get_price_per_hour(self):
        return self.price_per_hour

car1 = Cars("Urus", 7, 300, 50)
car2 = Cars("BMW M5", 9, 200, 30)
car3 = Cars("Hyundai ix35", 12, 100, 10)
car4 = Cars("Volkswagen Beetle", 11, 115, 5)
cars = [car1, car2, car3, car3]

class Destination:
    dest_number = 1
    def __init__(self, name, distance):
        self.dest_number = Destination.dest_number
        self.name = name
        self.distance = distance
        Destination.dest_number += 1

    def display(self):
        print("Destination Number:", self.dest_number, "Destination:", self.name, "Distance:", self.distance)

    def get_name(self):
        return self.name

    def get_distance(self):
        return self.distance

destination1 = Destination("Busan", 400)
destination2 = Destination("Gwangju", 300)
destination3 = Destination("Daegu", 285)
destination_list = [destination1, destination2, destination3]

def car_selection(cars):
    print("Select a car")
    for i in range(4):
        cars[i].display()

    car_choice = int(input('\nEnter the car number you would like to rent: '))

    valid(car_choice)
    #TODO fix valid car choice. 4th Vehicle
    car_choice -= 1
    car = cars[car_choice]

    name = car.get_name()
    fuel_efficiency = car.get_fuel_efficiency()
    max_speed = car.get_max_speed()
    price_per_hour = car.get_price_per_hour()

    return car_choice, name, fuel_efficiency, max_speed, price_per_hour

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
    units = input("Would you like to use imperial or metric units?")
    units = units.lower()
    if units == "imperial":
        price_fuel = imperial_to_metric(price_fuel)
        return price_fuel
    elif units != "metric":
        print("invalid input")
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
        try_again = int(input(
            "The trip will take too long. Quit the program or try again. Input 1 to quit or 2 to try again."))
        if try_again == 1:
            quit()
        elif try_again == 2:
            return 1
    else:
        print("There is enough time.")

    return time

def valid(value):
    valid = False
    while valid == False:
        if value == 1 or value == 2 or value == 3:
            valid = True
        else:
            value = int(input("Invalid. Input 1, 2 or 3: "))
            valid = False

chosen = False
while chosen == False:
    destination_choice, destination, distance = destination_selection(destination_list)
    print("\nYou have chosen", destination, "which is", distance, "km away.\n")

    car_choice, name, fuel_efficiency, max_speed, price_per_hour = car_selection(cars)
    print("\nYou have chosen", name, "with a fuel efficiency of", fuel_efficiency, "a max speed of", max_speed, "km/h", "and a price per hour of", price_per_hour, "dollars.\n")

    time_allowed = float(input("how long do you have to travel(in hours)?"))

    if destination_choice == 0:
        time = travel_time(distance, max_speed, time_allowed)
        if time == 1:
            continue
    elif destination_choice == 1:
        time = travel_time(distance, max_speed, time_allowed)
        if time == 1:
            continue
    else:
        time = travel_time(distance, max_speed, time_allowed)
        if time == 1:
            continue

    price_fuel = float(input("\nHow much does fuel cost per litre or gallon? "))
    price_fuel = units(price_fuel)

    price = (distance / fuel_efficiency) * price_fuel
    price = (f"{price:.2f}")
    vehicle_price = price_per_hour * time
    vehicle_price = (f"{vehicle_price:.2f}")
    print("\nFuel Price: ", price)
    print("Price for vehicle: ", vehicle_price)
    chosen = True
