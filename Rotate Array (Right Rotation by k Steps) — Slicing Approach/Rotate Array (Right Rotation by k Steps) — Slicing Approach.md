
# 189. Rotate Array (by k Steps) — Slicing Approach

**Difficulty:** Medium
**Link:** https://leetcode.com/problems/rotate-array/

## Problem

Given an integer array `nums`, rotate the array to the right by `k` steps, where `k` is non-negative.

## Examples

**Example 1:**
```
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
```

**Example 2:**
```
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
```

## Constraints

- `1 <= nums.length <= 10^5`
- `-2^31 <= nums[i] <= 2^31 - 1`
- `0 <= k <= 10^5`

## Follow-up

- Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
- Could you do it in-place with O(1) extra space?

---

## Solution — Slicing Approach

### Intuition

Rotating an array to the right by `k` steps means the last `k` elements move to the front, and the remaining elements shift to the back while keeping their relative order. Instead of rotating one step at a time in a loop, the whole result can be built directly by splitting the array into two chunks and swapping their order.

### Approach

1. Normalize `k` using `k = k % n`, since rotating by a multiple of the array's length brings it back to the same arrangement — this also handles `k` values larger than `n`.
2. Compute the split point as `n - k`, which marks where the "last `k` elements" begin.
3. Slice the array into two parts: everything before the split point, and everything from the split point onward.
4. Concatenate the second part followed by the first part — this produces the fully rotated array.
5. Since the problem requires in-place modification rather than returning a new array, assign the result to `nums[:]` (not `nums`), which overwrites the contents of the original list object rather than rebinding the local variable to a new one.

### Code

```python
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        k = n - k
        a = nums[:k]
        b = nums[k:]
        nums[:] = b + a
```

### Complexity

- **Time complexity:** $$O(n)$$
  Each slice and the concatenation touch every element once.

- **Space complexity:** $$O(n)$$
  Two new slices and their concatenation are created before being copied back into `nums`, so extra space proportional to `n` is used. This does **not** meet the O(1) follow-up requirement.

---

## Follow-up: O(1) Extra Space (Not Yet Implemented)

A classic approach for true in-place rotation is the **three-reversal trick**:

1. Reverse the entire array.
2. Reverse the first `k` elements.
3. Reverse the remaining `n - k` elements.

This achieves the same rotation without allocating new lists, meeting the O(1) extra space requirement.
