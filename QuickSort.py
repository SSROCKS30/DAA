def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr if x < pivot]
    same = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quicksort(left) + same + quicksort(right)

arr = list(map(int, input("Enter the array: ").split()))
print("Original Array: ", arr)
print("Sorted Array: ", quicksort(arr))