# 80. Remove Duplicates from Sorted Array II

## Problem Statement

Given an integer array `nums` sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears **at most twice**. The relative order of elements must be preserved.

Since some languages can't resize arrays, place the result in the first `k` elements of `nums` and return `k`. Elements beyond index `k-1` don't matter.

**Constraints:**
- Must be done in-place with O(1) extra memory.
- `1 <= nums.length <= 3 * 10^4`
- `-10^4 <= nums[i] <= 10^4`
- `nums` is sorted in non-decreasing order.

### Examples

```
Input:  nums = [1,1,1,2,2,3]
Output: k = 5, nums = [1,1,2,2,3,_]

Input:  nums = [0,0,1,1,1,1,2,3,3]
Output: k = 7, nums = [0,0,1,1,2,3,3,_,_]
```

---

## Why the "naive" approach fails

A first instinct is something like:

```python
for i in nums:
    if nums.count(i) > 2:
        nums.remove(i)
return len(nums)
```

This looks reasonable and even **passes small test cases**, but it's broken for two separate reasons:

1. **Mutating a list while iterating over it.** `for i in nums:` tracks a numeric index internally. Calling `nums.remove(i)` shifts every later element left by one, but the loop's index still advances by one — so the next element effectively gets skipped. On short duplicate runs (e.g. 3 copies of a value) this accidentally self-corrects, which is why small tests pass. On longer duplicate runs (e.g. 6 copies of the same value), the skipping compounds and too many copies survive.
2. **Performance.** `count()` and `remove()` are each O(n), called inside a loop — worst case O(n²). With `n` up to `3*10^4`, an adversarial input (many repeated values) risks a timeout even where correctness holds.

**Lesson:** passing a handful of test cases is not proof of correctness. A solution that mutates a collection while iterating over it needs a specific, deliberate justification — otherwise assume it's a bug waiting for a bigger input to expose it.

---

## The correct approach: two pointers

### Core insight

The array is **sorted**, so all duplicates of a value are always grouped together, consecutively. This means you never need global information (like `count()`) to decide whether to keep an element — you only need to look at what you've **already placed** in your result so far.

### Roles

- **Read pointer (`i`)** — scans the original array left to right, once.
- **Write pointer (`k`)** — tracks how many valid elements have been placed. `nums[0:k]` is always a valid, correctly-deduplicated prefix.

### Decision rule

For each element `nums[i]` being read, ask:

> "Would placing this at the next write slot create a 3rd consecutive copy of this value in my result?"

Since duplicates are grouped, this is answered by comparing `nums[i]` to `nums[k-2]` — the element **two positions back** in the result built so far:

- If `nums[i] == nums[k-2]`, keeping it would make 3 copies in a row → **skip**.
- Otherwise → **keep**: write `nums[k] = nums[i]`, then `k += 1`.

### Base case

The first two elements of any array can *always* be kept — with fewer than 2 elements placed, there's no way to have already violated the "max 2" rule. So:

- If `len(nums) <= 2`, just return `len(nums)` immediately (nothing to remove).
- Otherwise, start `k = 2` (accepting the first two elements as-is) and read from `i = 2` onward.

### Common mistakes when implementing this

- **Re-assigning `i` before a `for i in range(...)` loop does nothing** — the loop's own range controls `i` and overwrites any prior assignment. To start scanning at index 2, the range itself must be `range(2, len(nums))`.
- **Negative index wraparound.** If `k` is allowed to be less than 2 when you compute `nums[k-2]`, Python doesn't error — it silently wraps to the end of the array (`nums[-1]`, `nums[-2]`, ...) and compares against unrelated elements. This is a silent-failure bug, not a crash, which makes it easy to miss. Guaranteeing `k >= 2` before ever computing `nums[k-2]` avoids this entirely.
- **Returning the wrong quantity.** `k` is both the count of valid elements *and* the correct return value — no separate bookkeeping needed.

---

## Reference implementation

```python
class Solution(object):
    def removeDuplicates(self, nums):
        n = len(nums)
        if n <= 2:
            return n

        k = 2  # first two elements are always kept
        for i in range(2, n):
            if nums[i] != nums[k - 2]:
                nums[k] = nums[i]
                k += 1

        return k
```

### Manual trace: `[1,1,1,2,2,3]`

| i | nums[i] | compare to nums[k-2] | action        | k |
|---|---------|----------------------|---------------|---|
| - | -       | -                    | start         | 2 |
| 2 | 1       | nums[0] = 1          | equal → skip  | 2 |
| 3 | 2       | nums[0] = 1          | differ → keep | 3 |
| 4 | 2       | nums[1] = 1          | differ → keep | 4 |
| 5 | 3       | nums[2] = 2          | differ → keep | 5 |

Result: `k = 5`, `nums[:5] = [1,1,2,2,3]` ✅

---

## Complexity

| | Naive (`count` + `remove`) | Two-pointer |
|---|---|---|
| Time | O(n²) worst case | **O(n)** — single pass |
| Space | O(1) extra (but risky/buggy) | **O(1)** extra, genuinely correct |

The two-pointer version reads each element exactly once and does O(1) work per element, so it's linear overall, and it never mutates the array in a way that invalidates its own iteration.
