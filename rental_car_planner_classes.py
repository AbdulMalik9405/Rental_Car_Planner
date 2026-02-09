class Cars:
    car_number = 1
    passengers = 4
    def __init__(self, name, fuel_efficiency, max_speed, price_per_hour):
        self.car_number = Cars.car_number
        self.name = name
        self.fuel_efficiency = fuel_efficiency
        self.max_speed = max_speed
        self.price_per_hour = price_per_hour
        Cars.car_number +=1

    def display(self):
        print("Car:", self.name, "Fuel Efficiency:", self.fuel_efficiency, "max speed:", self.max_speed, "price per hour:", self.price_per_hour)

    def get_name(self):
        return self.name

    def get_fuel_efficiency(self):
        return self.fuel_efficiency

    def get_max_speed(self):
        return self.max_speed

    def get_price_per_hour(self):
        return self.price_per_hour

    def can_carry(self, num_passengers):
        if Cars.passengers >= num_passengers:
            return True
        return False

class Compact_car(Cars):
    def __init__(self, name, fuel_efficiency, max_speed, price_per_hour, manual):
        super().__init__(name, fuel_efficiency, max_speed, price_per_hour)
        self.manual = manual

    def display(self):
        super().display()
        print("Manual or Automatic:", self.manual)

    def can_carry(self, num_passengers):
        Cars.passengers = 4
        return super().can_carry(num_passengers)

class SUV(Cars):
    def __init__(self, name, fuel_efficiency, max_speed, price_per_hour, storage_space_litres):
        super().__init__(name, fuel_efficiency, max_speed, price_per_hour)
        self.storage_space = storage_space_litres

    def display(self):
        super().display()
        print("Storage Space:", self.storage_space)

    def can_carry(self, num_passengers):
        Cars.passengers = 6
        return super().can_carry(num_passengers)

class Luxury_car(Cars):
    def __init__(self, name, fuel_efficiency, max_speed, price_per_hour, convertable):
        super().__init__(name, fuel_efficiency, max_speed, price_per_hour)
        self.convertable = convertable

    def display(self):
        super().display()
        print("Convertable:", self.convertable)

    def can_carry(self, num_passengers):
        Cars.passengers = 2
        return super().can_carry(num_passengers)

class Garage():
    garage_number = 1
    def __init__(self, name):
        self.garage_number = Garage.garage_number
        self.garage = []
        self.name = name
        Garage.garage_number +=1

    def display(self):
        print(self.garage_number, ":", self.name)

    def add_car(self, cars):
        self.garage.append(cars)

    def remove_car(self, cars):
        self.garage.remove(cars)

    def display_cars(self):
        for i in range(3):
            print("Car", i+1)
            self.garage[i].display()

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
