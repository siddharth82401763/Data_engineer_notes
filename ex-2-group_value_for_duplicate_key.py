data = [
 ("A", 10),
 ("B", 20),
 ("A", 30),
 ("B", 40),
 ("C", 50)
]
result = {}
for key,value in data:
    if key not in result:
        result[key] = [value]
    else:
        result[key].append(value)
print(result)
