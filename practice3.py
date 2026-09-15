distance = float(input("distance in km: "))
fuel_efficiency = float(input("fuel efficiency (km per liter): "))
fuel_price = float(input("fuel price per liter: "))

fuel_needed = round(distance / fuel_efficiency, 2)
total_cost = fuel_needed * fuel_price

print(f"Distance: {distance}")
print(f"Fuel efficiency: {fuel_efficiency}")
print(f"Fuel price: {fuel_price}")

print(f"Fuel needed: {fuel_needed}")
print(f"Total fuel cost: {total_cost}")