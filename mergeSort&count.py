def merge_sort_and_count (array):

    if len(array)<=1:
        return array, 0
    

    mid = len(array)//2

    left, left_inv = merge_sort_and_count(array[:mid])
    right, right_inv = merge_sort_and_count(array[mid:])
    merged, merge_inv = merge_and_count(left, right)

    return merged, left_inv + right_inv + merge_inv

def merge_and_count(left, right):
    merged = []
    i=j=0
    inversions = 0


    while i<len(left) and j< len(right):
        if left[i] <= right [j]:
            merged.append(left[i])
            i+=1

        else:
            merged.append(right[j])

            inversions +=len(left) -1
            j+=1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged, inversions

array = [87, 6, 34,5]
sorted_list, inversions = merge_sort_and_count(array)
print ("Sorted list: ", sorted_list)
print ("Number of inversions: ", inversions)