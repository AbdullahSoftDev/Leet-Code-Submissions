# Leet-Code-Submissions
Daily DSA practice — problems solved on LeetCode (and GFG), with full reasoning, dry runs, and common mistakes logged for each one. The goal isn't just a working solution — it's understanding the pattern well enough to explain it cold in an interview.

Each problem gets its own folder with a solution file and a `README.md` covering the intuition, approach, complexity, and mistakes made along the way.

## 📌 Progress Log
| # | Problem | Difficulty | Pattern | Link |
|---|---------|-----------|---------|------|
| 26 | Remove Duplicates from Sorted Array | Easy | Two Pointers (Read/Write) | [Solution](./0026-remove-duplicates-from-sorted-array) |
| 27 | Remove Element | Easy | Two Pointers (Read/Write) | [Solution](./0027-remove-element) |
| 45 | Jump Game II | Medium | Greedy (Frontier Expansion / BFS-style) | [Solution](./0045-jump-game-ii) |
| 55 | Jump Game | Medium | Greedy (Farthest Reachable Index) | [Solution](./0055-jump-game) |
| 80 | Remove Duplicates from Sorted Array II | Medium | Two Pointers (Read/Write) | [Solution](./0080-remove-duplicates-from-sorted-array-ii) |
| 88 | Merge Sorted Array | Easy | Two Pointers (Merge from Back) | [Solution](./0088-merge-sorted-array) |
| 121 | Best Time to Buy and Sell Stock | Easy | One-Pass Running Min/Max | [Solution](./0121-best-time-to-buy-and-sell-stock) |
| 122 | Best Time to Buy and Sell Stock II | Medium | Greedy (Sum of Positive Differences) | [Solution](./0122-best-time-to-buy-and-sell-stock-ii) |
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
- **Greedy sum of positive differences** — LC 122 (Best Time to Buy and Sell Stock II)
  - Unlike LC 121, unlimited transactions are allowed, so there's no need to track a running minimum at all
  - Compare each day only to the day *immediately before it*; whenever the price rises, add that gain to the running total, and skip every day it falls
  - Works because of the telescoping-sum property: `(pn - p1) = (p2-p1) + (p3-p2) + ... + (pn - p(n-1))`, so summing every positive daily change always equals the best possible profit
  - Do not confuse this with LC 121's single-transaction pattern — reusing a global-minimum tracker here silently produces the wrong (lower) answer
- **Greedy farthest-reachable-index** — LC 55 (Jump Game)
  - Track `max_reach`, the furthest index reachable using every jump considered so far, while scanning left to right
  - At each index `i`, first confirm it's actually reachable (`i <= max_reach`) before trusting `nums[i]` — if `i > max_reach`, the reachability "wave" has permanently stalled and cannot recover, so return `False` immediately
  - Works because `max_reach` represents the union of every reachable position from all jumps so far, not one committed path, and it only ever grows as the scan proceeds
  - Common mistake made here: inverting the branches — writing `if i <= max_reach: return False` instead of using that condition as the *proceed* case — which flips the entire logic and fails even on the first index
  - Next step to revisit: LC 45 (Jump Game II), which asks for the *minimum number of jumps* rather than just reachability — same greedy family, different tracked quantity ✅ **done**
- **Greedy frontier expansion (BFS-style levels)** — LC 45 (Jump Game II)
  - Builds directly on LC 55's `max_reach` idea, but now tracks *two* values instead of one: `current_end` (edge of the frontier reachable with jumps used so far) and `farthest` (best reach achievable with one more jump), updated every iteration as `max(farthest, i + nums[i])`
  - The moment the scanner `i` catches up to `current_end`, the current frontier has been fully explored — commit to another jump (`jumps += 1`) and advance `current_end = farthest`
  - Loop only through `n - 2`, not `n - 1` — landing exactly on the last index shouldn't itself trigger a "phantom" extra jump, since no further jump is needed once you've arrived
  - Common mistake made here: comparing `i` against the `farthest` value just computed in the *same* iteration instead of the `current_end` carried over from the *previous* jump trigger — the check must always use the last committed boundary, not the number just calculated this round
  - Also easy to conflate the scanner `i` with an actual jump target — `i` always walks forward sequentially one index at a time; it never "jumps to" whatever `farthest` becomes
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
├── 0045-jump-game-ii/
│   ├── README.md
│   └── solution.py
├── 0055-jump-game/
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
├── 0122-best-time-to-buy-and-sell-stock-ii/
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
