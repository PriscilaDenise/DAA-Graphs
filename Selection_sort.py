def selection_sort (A):
    for i in range (0, len(A)-1):
        minIndex = i
        for j in range (i+1, len(A)):
            if A[j] < A[minIndex]:
                minIndex = j
        if minIndex != 1:
            A[i], A [minIndex] =  A[minIndex], A[i]


    return A
A = [-9, 876, 34, 23, 56, -34]
sorted_list = selection_sort(A)
print ("The sorted list is;", sorted_list)