add = lambda a, b: a + b
print(add(10, 20))

maximum = lambda a, b, c: max(a, b, c)
print(maximum(10, 50, 30))

#salary (descending) and then age (ascending)
employees = [
    ("Alice", 50000, 30),
    ("Bob", 50000, 25),
    ("Charlie", 60000, 35),
    ("David", 45000, 28)
]

employees.sort(key=lambda x: (-x[1], x[2]))
print(employees)
