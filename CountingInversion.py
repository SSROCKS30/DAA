def mergesort(arr):
    if len(arr) <= 1:
        return arr, 0
    
    mid = len(arr) // 2
    left, LI = mergesort(arr[:mid])
    right, RI = mergesort(arr[mid:])

    merged, M = merge(left, right)
    total = LI + RI + M

    return merged, total

def merge(left, right):
    result = []
    i = j = 0
    count = 0
    while(i < len(left) and j < len(right)):
        if(left[i] < right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            count += len(left) - i
            j += 1

    result += left[i:]
    result += right[j:]

    return result, count


arr = list(map(int, input("Enter the array: ").split()))
print("Original Array: ", arr)
sorted, inversions = mergesort(arr)
print("Sorted Array: ", sorted)
print("Inversions: ", inversions)