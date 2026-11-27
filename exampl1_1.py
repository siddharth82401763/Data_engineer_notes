def aloo(bhalu):
    if len(bhalu)<=1:
        return bhalu
    pivot = bhalu[len(bhalu)//2]
    left =[]
    for x in bhalu:
        if x>pivot:
            left.append(x)
    middle=[]
    for x in bhalu:
        if x == pivot:
            middle.append(x)
    right=[]
    for x in bhalu:
        if x < pivot:
            right.append(x)
    return aloo(left)+middle+aloo(right)

bhalu=[1,22,33,44,55,66,77,88,99]
result = aloo(bhalu)
print(result)
