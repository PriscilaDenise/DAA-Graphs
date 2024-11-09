def quick_sort(array):
    #base case; if array has 1 or 0 elements
    # it is aleready sorted. 
    if len(array) <= 1:
        return array
    

    # step 1: Choose a pivot 
    pivot = array [len(array)//2]

    # Step 2: Partition the array innto 3 part
    left = [x for x in array if x < pivot]
    middle = [x for x in array if x == pivot]
    right = [x for x in array if x > pivot]

    #step 3: Recursively sort the left
    return quick_sort(left) + middle + quick_sort(right)

array = [26, 67, 127, 98, 9, 200000, 100, 12, 15]
sorted_array = quick_sort(array)
print ("Sorted array is; ", sorted_array)


