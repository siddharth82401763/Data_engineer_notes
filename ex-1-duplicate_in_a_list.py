data = [1,2,3,2,4,5,1,6]
seen = set()
dublicate = set()
for i in data:
    if i not in seen:
        seen.add(i)
    else:
        dublicate.add(i)
print(list(seen))
print(list(dublicate))