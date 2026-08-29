# Leet-Code-Submissions
Daily DSA practice — problems solved on LeetCode (and GFG), with full reasoning, dry runs, and common mistakes logged for each one. The goal isn't just a working solution — it's understanding the pattern well enough to explain it cold in an interview.

Each problem gets its own folder with a solution file and a `README.md` covering the intuition, approach, complexity, and mistakes made along the way.

## 📌 Progress Log
| # | Problem | Difficulty | Pattern | Link |
|---|---------|-----------|---------|------|
| 26 | Remove Duplicates from Sorted Array | Easy | Two Pointers (Read/Write) | [Solution](./0026-remove-duplicates-from-sorted-array) |
| 27 | Remove Element | Easy | Two Pointers (Read/Write) | [Solution](./0027-remove-element) |
| 80 | Remove Duplicates from Sorted Array II | Medium | Two Pointers (Read/Write) | [Solution](./0080-remove-duplicates-from-sorted-array-ii) |
| 88 | Merge Sorted Array | Easy | Two Pointers (Merge from Back) | [Solution](./0088-merge-sorted-array) |
| 121 | Best Time to Buy and Sell Stock | Easy | One-Pass Running Min/Max | [Solution](./0121-best-time-to-buy-and-sell-stock) |
| 169 | Majority Element | Easy | Hash Map Frequency Count | [Solution](./0169-majority-element) |
| 189 | Rotate Array | Medium | Array Slicing / Rotation | [Solution](./0189-rotate-array) |

*(Updations are made daily.)*

## 🧠 Patterns Covered So Far
- **In-place partition via read/write pointer** — LC 27 (Remove Element), LC 26 (Remove Duplicates from Sorted Array), LC 80 (Remove Duplicates from Sorted Array II)
  - Same shape applies to: LC 283 (Move Zeroes)
  - LC 80 extends the pattern by comparing against `nums[k-2]` instead of `nums[k-1]`, allowing up to 2 copies instead of 1
- **Two-pointer merge from the back** — LC 88 (Merge Sorted Array)
  - Used whenever merging into a fixed-size array with reserved trailing space
- **One-pass running min/max** — LC 121 (Best Time to Buy and Sell Stock)
  - Track the lowest price seen *so far* while scanning left to right, and compare profit against it at every index — don't find the global min first and search after it, since the true min can come after the best sell point
  - Same shape applies to: any "best pair where first index < second index" problem solvable in a single forward pass
- **Hash map frequency counting** — LC 169 (Majority Element)
  - Build a `value -> count` map in one pass, then pick the key with the max value via `max(dict, key=dict.get)`
  - Next step to revisit: Boyer-Moore Voting Algorithm solves the same problem in O(1) space instead of O(n)
- **Array rotation via slicing** — LC 189 (Rotate Array)
  - Normalize `k` with `k = k % n` first to handle `k >= n` safely
  - Split the array at `n - k`, then concatenate the two halves in swapped order and write back with `nums[:] = ...` for true in-place modification
  - Next step to revisit: the three-reversal trick (reverse whole array, then reverse each half) solves it in O(1) extra space instead of O(n)
  
## 🛠 How This Repo Is Organized
```
Leet-Code-Submissions/
├── 0026-remove-duplicates-from-sorted-array/
│   ├── README.md
│   └── solution.py
├── 0027-remove-element/
│   ├── README.md
│   └── solution.py
├── 0080-remove-duplicates-from-sorted-array-ii/
│   ├── README.md
│   └── solution.py
├── 0088-merge-sorted-array/
│   ├── README.md
│   └── solution.py
├── 0121-best-time-to-buy-and-sell-stock/
│   ├── README.md
│   └── solution.py
├── 0169-majority-element/
│   ├── README.md
│   └── solution.py
├── 0189-rotate-array/
│   ├── README.md
│   └── solution.py
└── README.md   ← you are here
```

## 🎯 Why I Log Mistakes
Getting a solution accepted isn't the finish line — being able to explain *why* it works, and where I went wrong along the way, is what actually matters for interviews. Each problem's README includes a "Common Mistakes" section for exactly that reason — it's as much a record of the debugging/reasoning process as it is the final answer.

## 📈 Platforms
- **LeetCode** — primary, using the [Top Interview 150](https://leetcode.com/studyplan/top-interview-150/) study plan, going pattern by pattern
- **GeeksforGeeks** — supplementary, for concept explanations before diving into similar LeetCode problems
  
## 👤 About
Muhammad Abdullah — CS student, full-stack AI developer, building DSA fundamentals daily alongside frontend practice.
- GitHub: [@AbdullahSoftDev](https://github.com/AbdullahSoftDev)
