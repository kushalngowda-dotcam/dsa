def maxProduct(nums):
    max_so_far = nums[0]
    min_so_far = nums[0]
    result = nums[0]
    for x in nums[1:]:
        temp_max = max(x, x * max_so_far, x * min_so_far)
        min_so_far = min(x, x * max_so_far, x * min_so_far)
        max_so_far = temp_max
        result = max(result, max_so_far)
    return result
arr = [2,3,-2,4]
print("Maximum Product Subarray:", maxProduct(arr))
