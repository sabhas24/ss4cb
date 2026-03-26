# Binary Search

## Algorithm name

Binary Search

## Author

Victor Manuel Montini (2026-03-23)

## Algorithm description

Binary search is an efficient algorithm for finding a target value within a sorted array. It works by repeatedly dividing the search interval in half. If the target value is less than the middle element, the search continues in the lower half; if greater, in the upper half. This continues until the target is found or the interval is empty. Binary search runs in O(log n) time, making it significantly faster than linear search for large datasets.

## Model used to create the base code

claude-sonnet-4-6

### Prompt

```
Write a Python function called binary_search that receives a sorted list `sorted_list` and a `target_value`, and returns the index of the target value if found or -1 if not present. Use the binary search algorithm with descriptive English variable names.
```

## Obfuscated version

manually obfuscated
