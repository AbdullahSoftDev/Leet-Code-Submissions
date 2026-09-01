def jump(nums):
    n = len(nums)
    jumps = 0
    current_end = 0   # boundary of the range reachable with 'jumps' jumps
    farthest = 0       # farthest index reachable with one more jump

    for i in range(n - 1):  # stop at n-2, not n-1
        farthest = max(farthest, i + nums[i])

        if i == current_end:      # we've exhausted this frontier
            jumps += 1
            current_end = farthest

    return jumps
