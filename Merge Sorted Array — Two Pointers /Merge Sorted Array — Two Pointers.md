# Merge Sorted Array — Two Pointers (Merge from Back)

**LeetCode #88** | **Difficulty:** Easy | **Pattern:** Two Pointers

## Problem

You are given two integer arrays `nums1` and `nums2`, sorted in non-decreasing order, and two integers `m` and `n`, representing the number of elements in `nums1` and `nums2` respectively.

Merge `nums1` and `nums2` into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array `nums1`. `nums1` has a length of `m + n`, where the first `m` elements denote the elements that should be merged, and the last `n` elements are set to `0` and should be ignored. `nums2` has a length of `n`.

**Example:**
```
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
```

## Intuition

Since both `nums1` and `nums2` are already sorted, there's no need to sort the combined array from scratch. Instead, we can merge them directly, similar to the merge step in merge sort. The tricky part is that `nums1` must be modified in-place, and it has empty slots at the end reserved for the merged result.

## Approach

Merge from the **back** instead of the front. If we merged from the front, we'd risk overwriting real `nums1` values before we've had a chance to compare them.

Use three pointers:
- `i`: last real element in `nums1` (starts at `m - 1`)
- `j`: last element in `nums2` (starts at `n - 1`)
- `k`: last index of the full `nums1` array (starts at `m + n - 1`)

Compare `nums1[i]` and `nums2[j]`. Place whichever is larger at `nums1[k]`, then move that pointer (and `k`) one step back. Repeat until either `i` or `j` goes below 0.

If `nums2` still has leftover elements when the main loop ends, copy them into the remaining front positions of `nums1`. If `nums1` has leftovers instead, no action is needed — they're already correctly placed since `nums2` ran out first.

## Complexity

- **Time complexity:** O(m + n) — matches the follow-up requirement
- **Space complexity:** O(1) — in-place, no extra array used

## Common mistakes made while solving (good to remember)

- Confusing storing a *value* (`nums1[i]`) vs storing an *index* (`i`) in a pointer variable
- Forgetting `else:` needs a colon, and Python uses `and`/`or`, not `&&`/`||`
- Forgetting the object needs to be instantiated with `Solution()` (parentheses), not just `Solution`

## Code

```python
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        i = m - 1
        j = n - 1
        k = m + n - 1
        while i >= 0 and j >= 0:
            if nums1[i] < nums2[j]:
                nums1[k] = nums2[j]
                j -= 1
                k -= 1
            else:
                nums1[k] = nums1[i]
                i -= 1
                k -= 1

        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1

        return nums1


# Example usage
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 3, 5]
n = 3
obj = Solution()
print(obj.merge(nums1, m, nums2, n))
```

## Tags

`Array` `Two Pointers` `Sorting` `In-Place` `LeetCode-Easy` `Top-Interview-150`
