def quicksort(arr):
    b= len(arr)
    if len(arr)<=1:
        return arr
    pivot = arr[len(arr)//2]
    left = []
    for x in arr:
        if x < pivot:
            left.append(x)
    right = [x for x in arr if x>pivot]
    middle = [x for x in arr if x==pivot]
    return quicksort(left) + middle + quicksort(right)




result = quicksort([3,8,7,10,3,7,6,1,9,3])
print(result)