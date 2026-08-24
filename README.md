# Leet-Code-Submissions

Daily DSA practice — problems solved on LeetCode (and GFG), with full reasoning, dry runs, and common mistakes logged for each one. The goal isn't just a working solution — it's understanding the pattern well enough to explain it cold in an interview.

Each problem gets its own folder with a solution file and a `README.md` covering the intuition, approach, complexity, and mistakes made along the way.

## 📌 Progress Log

| # | Problem | Difficulty | Pattern | Link |
|---|---------|-----------|---------|------|
| 27 | Remove Element | Easy | Two Pointers (Read/Write) | [Solution](./0027-remove-element) |
| 88 | Merge Sorted Array | Easy | Two Pointers (Merge from Back) | [Solution](./0088-merge-sorted-array) |

*(Table updated as new problems are added.)*

## 🧠 Patterns Covered So Far

- **In-place partition via read/write pointer** — LC 27 (Remove Element)
  - Same shape applies to: LC 26 (Remove Duplicates from Sorted Array), LC 283 (Move Zeroes), LC 80 (Remove Duplicates II)
- **Two-pointer merge from the back** — LC 88 (Merge Sorted Array)
  - Used whenever merging into a fixed-size array with reserved trailing space

## 🛠 How This Repo Is Organized

```
Leet-Code-Submissions/
├── 0027-remove-element/
│   ├── README.md
│   └── solution.py
├── 0088-merge-sorted-array/
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
