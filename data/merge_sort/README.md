# Merge Sort

## Algorithm name

Merge Sort

## Author

Victor Manuel Montini (2026-03-23)

## Algorithm description

Merge sort is an efficient, divide-and-conquer sorting algorithm. It works by recursively splitting the array into two halves, sorting each half, and then merging the sorted halves back together. The merge step compares elements from both halves and places them in order into the original array. Merge sort has a time complexity of O(n log n) in all cases and is a stable sort.

## Model used to create the base code

claude-sonnet-4-6

### Prompt

```
Write a C implementation of merge sort with a function called merge_sort that receives an integer array `number_array`, a `left_index` and a `right_index`, and sorts the subarray in ascending order recursively. Include a helper function merge_halves. Use descriptive English variable names and comments.
```

## Obfuscated version

manually obfuscated
