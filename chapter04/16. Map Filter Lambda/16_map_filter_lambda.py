cities = ["london", "paris", "barcelona", "athens", "Casablanka"]

# Filtering city names longer than 5 character using filter and lambda
long_cities = filter(lambda city: len(city) > 5, cities)

# Capitalize the filter cities using map and lambda
cap_length_cities = map(lambda city: city.tittle(), long_cities)

# All in one
cap_long_cities = list(map(lambda city: city.tittle(), filter(lambda city: len(city) > 5, cities)))

print(*cap_long_cities)