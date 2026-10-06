def maxsubarray(target, arr):
    start = 0
    curr_sum = arr[0]
    for end in range(1, len(arr) + 1):
        while curr_sum > target and start < end - 1:
            curr_sum -= arr[start]
            start += 1
        if curr_sum == target:
            return [start, end - 1]  # return indices
        if end < len(arr):
            curr_sum += arr[end]
    return [-1]  # if no subarray found

# Example usage
arr = [1, 2, 3, 7, 5]
target = 12
print("Subarray indices:", maxsubarray(target, arr))
