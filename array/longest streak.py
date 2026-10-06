def longestConsecutive(nums):
    num_set = set(nums)   # step 1
    longest = 0

    for num in num_set:   # step 2
        if num - 1 not in num_set:   # start of sequence
            length = 1
            while num + length in num_set:   # step 3
                length += 1
            longest = max(longest, length)   # step 4

    return longest

# Example
arr = [100, 4, 200, 1, 3, 2]
print("Longest Consecutive Sequence Length:", longestConsecutive(arr))
