# dsa-archives

My archive of solved DSA problems. Each file has the solution plus a short
explanation of the approach (written at the top), so I can revise quickly later.

## Layout

Organized by topic — one file per problem:

```
topics/
├── arrays/
│   └── two_sum.py
├── strings/
└── ...
```

## Format

Each solution file starts with a docstring explaining the approach, then the code:

```python
"""
Two Sum  (Easy)  — https://leetcode.com/problems/two-sum

Approach:
    Walk the array once, keeping a dict of value -> index. For each number,
    check if (target - number) was already seen. O(n) instead of O(n^2).

Time:  O(n)
Space: O(n)
"""

def two_sum(nums, target):
    seen = {}
    for i, n in enumerate(nums):
        if target - n in seen:
            return [seen[target - n], i]
        seen[n] = i
```
