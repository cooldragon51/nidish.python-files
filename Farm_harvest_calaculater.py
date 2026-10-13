Farm_1 = 206
Farm_2 = 96
Farm_3 = 183
Farm_4 = 147
Farm_5 = 89

Total = Farm_1 + Farm_2 + Farm_3 + Farm_4 + Farm_5
Average = Total/5
print("Total is: ",Total)
print("Average is: ",Average)
price_per_kg = 15
earnings = Total * price_per_kg
print("Total earnings: Rs.",earnings)

bags = Total // 25
leftover = Total % 25
print("Full bags packed: ",bags)
print("Leftover grain: ",leftover)

last_year = 500
print("Better than last year? :", Total > last_year)
print("Same as last year?: ",Total == last_year)
print("At least as good?: ",Total >= last_year)

Total += 30
print("After bonus crop: ",Total,"kg")

Total -= 15
print("After seed reserve: ",Total,"kg")

bags = Total // 25
leftover = Total % 25
print("Full bags packed: ",bags)
print("Leftover grain: ",leftover)