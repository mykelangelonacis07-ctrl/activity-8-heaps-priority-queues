# Activity 8 – Heaps and Priority Queues

Python implementations and unit tests for Module 8 (Heaps and Priority Queues).

## Files
- `activity_8_heaps.py`: Array-based `MinHeap` (Activity 1), `MaxHeap` (Activity 2), and in-place `heap_sort` (Activity 3).
- `activity_8_applications.py`: `kth_largest` (Activity 4), `merge_k_sorted_arrays` (Activity 5), and `PriorityScheduler` (Activity 6).
- `test_activity_8.py`: Automated tests covering empty structures, single-element inputs, duplicates, and longer random sequences.

## Time & Space Complexity Summary
| Operation / Algorithm | Time Complexity | Extra Space |
| :--- | :--- | :--- |
| `peek` | $O(1)$ | $O(1)$ |
| `insert` (sift up) | $O(\log n)$ | $O(1)$ |
| `extract` (sift down) | $O(\log n)$ | $O(1)$ |
| `build_heap` | $O(n)$ | $O(1)$ |
| `heap_sort` (in-place) | $O(n \log n)$ | $O(1)$ |
| `kth_largest` | $O(n \log k)$ | $O(k)$ |
| `merge_k_sorted_arrays` | $O(N \log k)$ | $O(k)$ |

## Running Tests
```bash
python test_activity_8.py