def bubble_sort(list):
    for i in range (0, len(list)-1):
        for j in range (0, len(list)-1-i):
            if list [j] > list [j+1]:
                list[j], list [j+1] = list [j+1] , list [j]

    return list

list = ['k', 'j', 'a', 'c', 'e']
print (bubble_sort(list))