cities = ["New York", "London", "Paris", "Tokyo", "Sydney"]

cities.append("Dubai")
cities.insert(1, "Los Angeles")

print("Cities after adding new elements:", cities)

print("Alternate cities from the list:", cities[::2])

p_cities = [city for city in cities if city.startswith('P')]
print("Cities whose name starts with 'P':", p_cities)

cities.pop(2)
print("Cities after removing one element:", cities)

numbers = [1, 2, 3, 4, 5]
numbers = [num + 10 for num in numbers]
print("Numbers after adding 10 to each element:", numbers)