cities = ["london", "paris", "athens", "barcelona"]

cap_cities = map(lambda city: city.title(), cities)

for cap_city in cap_cities:
    print(cap_city)