numbers = [64, 34, 25, 12, 22, 11, 90]

def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
print("Unsorted array:", numbers)
sorted_numbers = bubble_sort(numbers)
print("Sorted array:", sorted_numbers)

#Time Complexity: 
#$O(n^2)$Worst and Average Case: $O(n^2)$ 
#because there are two nested loops. The outer loop runs $n$ times, and the inner loop runs $n-i-1$ times, resulting in roughly $n^2 / 2$ comparisons and swaps.
#Best Case: $O(n^2)$ for this specific implementation. Even if the array is already sorted, the loops will still execute fully because there is no optimization (like a swapped flag) to break early.
#Space Complexity: $O(1)$The algorithm sorts the list in-place. It does not require any extra proportional memory, only utilizing a few variables for indices and swapping.
