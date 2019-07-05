def median(list1):
    half = len(list1) // 2
    list1.sort()
    if not len(list1) % 2:
        return (list1[half - 1] + list1[half]) / 2.0
    return list1[half]

print(median([1,2,3,4,5,6,7,8,9]))