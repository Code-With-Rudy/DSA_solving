arr=[2,1,4,0,5,6]
#expected_sum = sum(range(len(arr) + 1))
#actualsum=0
# Sum of numbers from 0 to n
#actual_sum = sum(arr)  # Sum of the elements in the array
#missing_number = expected_sum - actual_sum  # Calculate the missing number
#print(missing_number)  # Print the missing number
def find_missing_number(arr):
    n = len(arr)
    expsum = n * (n + 1) // 2
    actualsum = 0
    for num in arr:
        actualsum += num
    return expsum - actualsum
print(find_missing_number(arr))
