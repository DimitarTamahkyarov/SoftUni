def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


# Example usage:
array = [4, 2, 9, 6, 1, 7, 3, 5, 8]
sorted_array = quicksort(array)
print(sorted_array)
