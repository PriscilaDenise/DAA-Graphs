# def insertion_sort (A):
#     for i in range(1, len(A)):
#         curNum = A[i]
#         for j in range (i-1, 0, -1):
#             if A[j] > curNum:
#                 A[j+1] = A[j]
#             else:
#                 A[j+1] = curNum
#                 break
#     return A
        
# A = [23, 56, 31, 1, -27, 70000]
# sorted_list = insertion_sort(A)

# print ("The sorted list is;", sorted_list)

def insertion_sort(A):
    for i in range(1, len(A)):
        curNum = A[i]
        j = i - 1
        while j >= 0 and A[j] > curNum:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = curNum
    return A

A = [23, 56, 31, 1, -27, 70000]
sorted_list = insertion_sort(A)

print("The sorted list is:", sorted_list)
