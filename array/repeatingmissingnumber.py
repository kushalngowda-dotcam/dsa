def findMissingRepeating(arr, n):
    # Expected sums
    S = n * (n + 1) // 2
    S2 = n * (n + 1) * (2*n + 1) // 6

    # Actual sums
    arr_sum = sum(arr)
    arr_sq_sum = sum(x*x for x in arr)

    # Equations
    diff1 = arr_sum - S          # R - M
    diff2 = arr_sq_sum - S2      # R^2 - M^2

    # (R^2 - M^2) = (R - M)(R + M)
    sumRM = diff2 // diff1       # R + M

    R = (diff1 + sumRM) // 2
    M = R - diff1

    return (M, R)
