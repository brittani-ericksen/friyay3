def bubble(list_a):
    indexing_length = len(list_a) - 1
    sorted = False

    while not sorted:
        sorted = True #when all numbers are sorted, if statement won't activate and sorted will remain True, thus ending the while loop
        for i in range(0, indexing_length):
            if list_a[i] > list_a[i+1]:
                sorted = False
                list_a[i], list_a[i+1] = list_a[i+1], list_a[i]
                print(list_a)
        
    return list_a

print(bubble([2, 5, 7, 1, 6, 3, 8, 2, 3, 3, 10, 14, 11]))