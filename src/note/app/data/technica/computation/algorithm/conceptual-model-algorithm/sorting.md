---
tags: [problem]
---

# Sorting


> 

| Algorithm | Best Case | Average Case | Worst Case | Space | Stable | In-place | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Bubble Sort** | O(n) | O(n²) | O(n²) | O(1) | Yes | Yes | Repeatedly swaps adjacent elements if they are in the wrong order; continues until sorted. |
| **Selection Sort** | O(n²) | O(n²) | O(n²) | O(1) | No | Yes | Finds the minimum element and moves it to the front in each iteration; reduces unsorted region. |
| **Insertion Sort** | O(n) | O(n²) | O(n²) | O(1) | Yes | Yes | Builds sorted array one item at a time by inserting elements into their correct position. |
| **Merge Sort** | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes | No | Recursively splits the array, sorts subarrays, and merges them. |
| **Quick Sort** | O(n log n) | O(n log n) | O(n²) | O(log n) | No | Yes | Picks a pivot, partitions array into two halves, recursively sorts them. |
| **Heap Sort** | O(n log n) | O(n log n) | O(n log n) | O(1) | No | Yes | Builds a max-heap and repeatedly swaps the root with the last item and re-heapifies. |
| **Counting Sort** | O(n + k) | O(n + k) | O(n + k) | O(k) | Yes | No | Counts the frequency of each element; uses this to place elements in sorted order. Only for integers or categories. |
| **Radix Sort** | O(nk) | O(nk) | O(nk) | O(n + k) | Yes | No | Processes digits from least to most significant using a stable sort like counting sort. |
| **Bucket Sort** | O(n + k) | O(n + k) | O(n²) | O(n + k) | Yes | No | Divides input into buckets, sorts each bucket (often with insertion sort), and concatenates results. |
| **Tim Sort** | O(n) | O(n log n) | O(n log n) | O(n) | Yes | No | Hybrid stable algorithm that combines merge sort and insertion sort; used in Python/Java built-ins. |

## References

- https://en.wikipedia.org/wiki/Sorting