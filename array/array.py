def kadane(arr):
    maxstarting = arr[0]   # global max
    maxending = arr[0]     # current max

    for x in arr[1:]:
        # either start new subarray at x or extend previous
        maxending = max(x, maxending + x)
        # update global max
        maxstarting = max(maxstarting, maxending)

    return maxstarting

# Example usage
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print("Maximum Subarray Sum:", kadane(arr))
