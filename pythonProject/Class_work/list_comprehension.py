# Generate list from 1 to 10

lst = [num for num in range(1, 11)]
evens = [num for num in range(1, 11) if num % 2 == 0]
even_and_squared_odds = [num if num % 2 == 0 else num ** 2 for num in range(1, 11)]

print(lst)
print(evens)
print(even_and_squared_odds)

list_nested_for =[(x, y) for x in range(1, 5) for y in range(6, 10)]

print(list_nested_for)
upper_names = [name.upper() for name in ["Dolapo", "Tolani", "Florence", "Suya"]]

list_of_dicts = [{key: value} for key, value in zip(upper_names, evens)]
print(upper_names)
print(list_of_dicts)

