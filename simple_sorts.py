# simple_sorts.py
# bubble sort, selection sort, insertion sort
# Modified by: javaughn bradford 
# I had a problem with the list being named alll the same and I didn't notice until I had chat gpt check, so they changed the names and moves the numbers to the end 

def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swapped = True
        if not swapped:  
            break
    return lst

def selection_sort(lst):
    n = len(lst)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if lst[j] < lst[min_idx]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
    return lst

def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst

def print_list(lst):
    for val in lst:
        print(val, end=" ")
    print()

if __name__ == "__main__":
    lst1 = [64, 34, 25, 12, 22, 11, 90]
    bubble_sort(lst1)
    print("Bubble sorted array:")
    print_list(lst1)
    
    lst2 = [34, 64, 25, 22, 12, 11, 90]
    selection_sort(lst2)
    print("Selection sorted array:")
    print_list(lst2)
    
    lst3 = [90, 12, 25, 34, 64, 22, 11]
    insertion_sort(lst3)
    print("Insertion sorted array:")
    print_list(lst3)
