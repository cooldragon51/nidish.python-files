temperature = int(input("Enter today's temperature in Celsius: "))

if temperature < 20:
    outfit = "Jacket"
    print("It is cold today.")
    print("wear a ",outfit)

else:
    outfit = "T-Shirt"
    print("It is a warm day today.")
    print("wear a",outfit)

is_raining = input("Is it raining today? (yes/no): ")

if is_raining == "yes":
    print("Bring a umbrella!")

wind_speed = int(input("Enter the wind speed in km\h: "))

if wind_speed < 30:
    needs_windbreaker = "yes"
    print("It is windy today.")
    print("Wear a windbreaker over your ",outfit)

else:
    needs_windbreaker = "yes"
    print("It is calm today.")
    print("No windbreaker needed over your ",outfit)

has_puddles = int(input("Are there puddles? (yes/no): "))

if has_puddles < "yes":
    has_puddles = "yes"
    shoes = "boots"
    print("The ground is wet.")
    print("Wear ",shoes)

else:
    shoes = "sneakers"
    print("The ground is dry.")
    print("Wear ",shoes)

print("")
print("Weather check complete!")

print("======= WEATHER OUTFIT PICKER =======")
print("Temperture: ",temperature)
print("Outfit chosen: ",outfit)
print("Raining: ",is_raining)
print("Windbreaker Needed: ",needs_windbreaker)
print("Shoes Chosen: ",shoes)
print("======================================")