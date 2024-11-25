def car_selection():
  car = ['Urus', 'BMW M5', 'Hyundai ix35', 'Volkswagen Beetle']
  fuel_efficiency = [7, 9, 12, 11] #km per liter
  max_speed = [300, 200, 100, 115]
  price_per_hour = [50, 30, 10, 5]

  print('Select a car: ')
  for i in range(len(car)):
    print("Car Number:", i+1, "Car:", car[i], "fuel efficiency:", fuel_efficiency[i], "max_speed:", max_speed[i], "price per hour:", price_per_hour[i])
  car_choice = int(input('\nEnter the car number you would like to rent: '))
  valid(car_choice)
  car_choice = car_choice - 1
  return car_choice, car, fuel_efficiency, max_speed, price_per_hour

def destination_selection():
  destination = ["Busan", "Gwangju", "Daegu"]
  distance = [400, 300, 285]

  print("Select a destination: ")
  for i in range(len(destination)):
    print("Destination Number:", i+1, "Destination: ", destination[i], "Distance: ", distance[i])
  destination_choice = int(input('\nEnter the Destination number of where you would like to go: '))
  valid(destination_choice)
  destination_choice = destination_choice - 1
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
    try_again = int(input("The trip will take too long. Quit the program or try again. Input 1 to quit or 2 to try again."))
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
  destination_choice, destination, distance = destination_selection()
  print("\nYou have chosen", destination[destination_choice], "which is" , distance[destination_choice], "km away.\n")

  car_choice, car, fuel_efficiency, max_speed, price_per_hour =       car_selection() 
  print("\nYou have chosen", car[car_choice], "with a fuel efficiency of", fuel_efficiency[car_choice], "a max speed of", max_speed[car_choice], "km/h", "and a price per hour of", price_per_hour[car_choice], "dollars.\n")
  
  time_allowed = float(input("how long do you have to travel(in hours)?"))
  
  if destination_choice == 0:
    time = travel_time(distance[destination_choice], max_speed[car_choice], time_allowed)
    if time == 1:
      continue
  elif destination_choice == 1:
    time = travel_time(distance[destination_choice], max_speed[car_choice], time_allowed)
    if time == 1:
      continue
  else:
    time = travel_time(distance[destination_choice], max_speed[car_choice], time_allowed)
    if time == 1:
      continue
  
  price_fuel = float(input("\nHow much does fuel cost per litre or gallon? "))
  price_fuel = units(price_fuel)
  
  price = (distance[destination_choice]/fuel_efficiency[car_choice]) * price_fuel
  price = (f"{price:.2f}")
  vehicle_price = price_per_hour[car_choice] * time
  vehicle_price = (f"{vehicle_price:.2f}")
  print("\nFuel Price: ", price)
  print("Price for vehicle: ", vehicle_price)
  chosen = True