# LeetCode 26 — Remove Duplicates from Sorted Array

## Problem
Given an integer array `nums` sorted in non-decreasing order, remove
duplicates **in-place** so each unique element appears only once, keeping
relative order. Return `k`, the number of unique elements — the first `k`
elements of `nums` must contain those uniques in sorted order.

## Key Idea: Two Pointers (Write / Scan), Backward Comparison
Because the array is **sorted**, duplicates are always adjacent — so you
never need to compare an element against every other element, only against
the **last unique value you've already kept**.

- `k` — write pointer. Tracks how many uniques kept so far, and doubles as
  the index for the next open "kept" slot. Starts at `1`, since `nums[0]`
  is always automatically unique (nothing before it to duplicate).
- `i` — scan pointer. Walks every index from `1` to `len(nums)-1`.

At each `i`, compare `nums[i]` to `nums[k-1]` — **not** `nums[i+1]** (forward)
and not `nums[k]` (that slot may still hold stale data). `nums[k-1]` is the
one guaranteed-correct reference: the last value actually written into the
kept region.

- If `nums[i] != nums[k-1]` → new unique value found. Write it:
  `nums[k] = nums[i]`, then `k += 1`.
- If `nums[i] == nums[k-1]` → duplicate. Do nothing, move on.

Return `k` at the end.

## Solution
```python
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[k-1]:
                nums[k] = nums[i]
                k += 1
        return k
```

## Dry Run
`nums = [0,0,1,1,1,2,2,3,3,4]`

| i | nums[i] | vs nums[k-1] | action        | k |
|---|---------|--------------|----------------|---|
| 1 | 0       | 0 (same)     | skip           | 1 |
| 2 | 1       | 0 (diff)     | nums[1]=1      | 2 |
| 3 | 1       | 1 (same)     | skip           | 2 |
| 4 | 1       | 1 (same)     | skip           | 2 |
| 5 | 2       | 1 (diff)     | nums[2]=2      | 3 |
| 6 | 2       | 2 (same)     | skip           | 3 |
| 7 | 3       | 2 (diff)     | nums[3]=3      | 4 |
| 8 | 3       | 3 (same)     | skip           | 4 |
| 9 | 4       | 3 (diff)     | nums[4]=4      | 5 |

Result: `k=5`, `nums[:5] = [0,1,2,3,4]` ✅

## Complexity
- **Time:** O(n) — single pass.
- **Space:** O(1) — in-place, no extra structures.

## Common Mistakes (from working through this one)
1. **Comparing forward (`nums[i+1]`) instead of backward (`nums[k-1]`).**
   Forward comparison crashes at the last index (no `i+1`) and also makes it
   ambiguous which value (`nums[i]` or `nums[i+1]`) is the "new" one to
   write — leading to writing the wrong (already-counted) value.
2. **Comparing against `nums[k]` instead of `nums[k-1]`.** Right after
   incrementing `k`, index `k` hasn't been written to yet — it still holds
   stale original data, not the real last-kept value. Off-by-one in this
   direction causes false "new value" detections.
3. **Comparing against a single fixed value (e.g. `nums[0]`) for the whole
   array.** Only catches duplicates of one specific value — misses that the
   "value to compare against" must update as you move through the array to
   whatever was most recently kept.
4. **Manually incrementing a `for i in range(...)` loop variable.** Same as
   other problems — the loop already controls `i`; extra `i+=1` inside does
   nothing.

## Pattern to Remember
Same **"in-place read/write pointer"** family as:
- LeetCode 27 (Remove Element)
- LeetCode 283 (Move Zeroes)
- LeetCode 80 (Remove Duplicates II — allows up to 2 occurrences)

The twist here vs. LeetCode 27: comparison is against the **last kept
value** (`nums[k-1]`), not a fixed target — because "new vs. duplicate"
depends on what came before, not a constant.
