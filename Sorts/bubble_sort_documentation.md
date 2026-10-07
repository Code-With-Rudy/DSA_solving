# Bubble Sort Algorithm

## Overview
Bubble Sort is one of the simplest sorting algorithms. It works by repeatedly stepping through the list, comparing adjacent elements, and swapping them if they are in the wrong order. The pass through the list is repeated until the list is sorted. 

The algorithm gets its name because the largest elements "bubble" up to the end of the list during each pass, much like bubbles rising to the surface of water.

## Python Implementation

Here is a standard implementation of the Bubble Sort algorithm in Python:

```python
numbers = [64, 34, 25, 12, 22, 11, 90]

def bubble_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

print("Unsorted array:", numbers)
sorted_numbers = bubble_sort(numbers)
print("Sorted array:", sorted_numbers)
```

## Complexity Analysis

### Time Complexity
* **Worst Case: `O(n²)`** 
  Occurs when the array is reverse sorted. The outer loop runs `n` times, and the inner loop runs `n - i - 1` times, leading to roughly `n²/2` comparisons.
* **Average Case: `O(n²)`** 
  Occurs when the elements are in a random order.
* **Best Case: `O(n²)`** *(for this specific unoptimized code)*
  Even if the array is already sorted, this specific implementation will still run through all the loops. *(Note: Bubble sort can be optimized to `O(n)` best-case time complexity by adding a boolean flag to check if any swaps were made during a pass).*

### Space Complexity
* **Space Complexity: `O(1)`**
  Bubble sort is an **in-place** sorting algorithm. It only requires a single additional memory space for the temporary variable used during the swapping process, meaning the memory used does not increase with the size of the input array.