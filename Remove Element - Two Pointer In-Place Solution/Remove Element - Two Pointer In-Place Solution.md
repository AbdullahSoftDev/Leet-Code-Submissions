# LeetCode 27 — Remove Element

## Problem
Given an integer array `nums` and an integer `val`, remove all occurrences of
`val` **in-place**. The order of the remaining elements can change. Return
`k`, the number of elements not equal to `val` — the first `k` elements of
`nums` must be exactly those elements (in any order).

You can't just build a new list — the array must be modified in place, and
anything after index `k` doesn't matter.

## Key Idea: Two Pointers (Slow/Fast)
- `i` — the **scanning** pointer, walks through every element.
- `k` — the **write** pointer, marks where the next *kept* element goes.
  Starts at `0` and only advances when something is actually kept.

Rule at each step:
- If `nums[i] != val` → this element should survive. Copy it to `nums[k]`,
  then `k += 1`.
- If `nums[i] == val` → do nothing. Just let `i` move on (skip it).

At the end, `k` equals the count of kept elements, and `nums[0:k]` holds them.

## Why this works
Every element that isn't `val` gets copied, in order, to the front of the
array using `k` as the write cursor. `k` never advances during a skip, so
skipped (matching) elements simply get overwritten by later keeps — nothing
needs to be shifted or deleted explicitly.

## Solution
```python
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k
```

## Dry Run
`nums = [0,1,2,2,3,0,4,2]`, `val = 2`

| i | nums[i] | != val? | action        | k |
|---|---------|---------|---------------|---|
| 0 | 0       | yes     | nums[0]=0     | 1 |
| 1 | 1       | yes     | nums[1]=1     | 2 |
| 2 | 2       | no      | skip          | 2 |
| 3 | 2       | no      | skip          | 2 |
| 4 | 3       | yes     | nums[2]=3     | 3 |
| 5 | 0       | yes     | nums[3]=0     | 4 |
| 6 | 4       | yes     | nums[4]=4     | 5 |
| 7 | 2       | no      | skip          | 5 |

Result: `k = 5`, `nums[:5] = [0,1,3,0,4]` ✅

## Complexity
- Time complexity:
$$O(n)$$
Single pass through the array.

## Space complexity:
$$O(1)$$
In-place, no extra data structures used.

## Common Mistakes (from working through this one)
1. **Reusing a variable name in a loop that you still need elsewhere.**
   `for val in nums:` silently destroys the `val` parameter — Python won't
   warn you, it just overwrites it.
2. **Manually incrementing a `for i in range(...)` loop variable.**
   The loop already controls `i`; `i += 1` inside the body does nothing
   observable and is a sign you actually wanted a `while` loop with manual
   control instead.
3. **`range(nums)` vs `range(len(nums))`** — `range()` wants a count
   (integer), not the list itself.
4. **Flipping the `if` condition.** It's easy to accidentally write the
   *keep* logic under the *match* condition (`==`) instead of `!=`. Always
   trace one match and one non-match by hand before trusting the branch.
5. **Off-by-one via `nums[i+1]`.** Any solution that peeks ahead to
   `nums[i+1]` risks `IndexError` on the last index — a sign the two-pointer
   write approach (no look-ahead needed) is the better shape for this
   problem.

## Pattern to Remember
This is the **"in-place partition via read/write pointer"** pattern — same
idea used in:
- LeetCode 26 (Remove Duplicates from Sorted Array)
- LeetCode 283 (Move Zeroes)
- LeetCode 80 (Remove Duplicates II)

Whenever a problem says *"in-place," "O(1) extra space," "return length k,"*
this two-pointer read/write shape is usually the first thing to try.
