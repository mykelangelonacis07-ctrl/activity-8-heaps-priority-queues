import random

from activity_8_applications import PriorityScheduler, kth_largest, merge_k_sorted_arrays
from activity_8_heaps import MaxHeap, MinHeap, heap_sort


def _assert_raises_index_error(fn) -> None:
    try:
        fn()
    except IndexError:
        return
    raise AssertionError("Expected IndexError was not raised")


def test_activity_1_min_heap() -> None:
    # Empty structure
    empty_h = MinHeap()
    assert empty_h.size() == 0
    _assert_raises_index_error(empty_h.peek)
    _assert_raises_index_error(empty_h.extract)

    # Single element
    single_h = MinHeap()
    single_h.insert(42)
    assert single_h.size() == 1
    assert single_h.peek() == 42
    assert single_h.extract() == 42
    assert single_h.size() == 0

    # Activity 1 prompt sequence
    sample = [5, 9, 11, 14, 19, 17, 18, 13]
    h = MinHeap()
    for val in sample:
        h.insert(val)
    assert h.size() == 8
    assert h.peek() == 5
    assert [h.extract() for _ in range(8)] == [5, 9, 11, 13, 14, 17, 18, 19]

    # Duplicates
    dup_h = MinHeap()
    for val in [7, 3, 7, 1, 3, 1, 9]:
        dup_h.insert(val)
    assert [dup_h.extract() for _ in range(7)] == [1, 1, 3, 3, 7, 7, 9]

    # Longer random sequence
    rng = random.Random(42)
    rand_seq = [rng.randint(-500, 500) for _ in range(250)]
    rand_h = MinHeap()
    for val in rand_seq:
        rand_h.insert(val)
    assert [rand_h.extract() for _ in range(len(rand_seq))] == sorted(rand_seq)


def test_activity_2_max_heap() -> None:
    # Empty structure
    empty_h = MaxHeap()
    assert empty_h.size() == 0
    _assert_raises_index_error(empty_h.peek)
    _assert_raises_index_error(empty_h.extract)

    # Single element
    single_h = MaxHeap()
    single_h.insert(99)
    assert single_h.peek() == 99
    assert single_h.extract() == 99

    # Activity 2 prompt sequence
    sample = [5, 9, 11, 14, 19, 17, 18, 13]
    h = MaxHeap()
    for val in sample:
        h.insert(val)
    assert h.size() == 8
    assert h.peek() == 19
    assert [h.extract() for _ in range(8)] == [19, 18, 17, 14, 13, 11, 9, 5]

    # Duplicates
    dup_h = MaxHeap()
    for val in [4, 9, 4, 2, 9, 2]:
        dup_h.insert(val)
    assert [dup_h.extract() for _ in range(6)] == [9, 9, 4, 4, 2, 2]

    # Longer random sequence
    rng = random.Random(77)
    rand_seq = [rng.randint(-500, 500) for _ in range(250)]
    rand_h = MaxHeap()
    for val in rand_seq:
        rand_h.insert(val)
    assert [rand_h.extract() for _ in range(len(rand_seq))] == sorted(rand_seq, reverse=True)


def test_activity_3_heap_sort() -> None:
    assert heap_sort([]) == []
    assert heap_sort([12]) == [12]
    assert heap_sort([4, 10, 3, 5, 1]) == [1, 3, 4, 5, 10]
    assert heap_sort([1, 2, 3, 4, 5, 6]) == [1, 2, 3, 4, 5, 6]
    assert heap_sort([6, 5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5, 6]
    assert heap_sort([5, 2, 5, 1, 2, 5, 1]) == [1, 1, 2, 2, 5, 5, 5]

    rng = random.Random(101)
    for _ in range(25):
        rand_seq = [rng.randint(-100, 100) for _ in range(80)]
        assert heap_sort(rand_seq) == sorted(rand_seq)


def test_activity_4_kth_largest() -> None:
    # Single element
    assert kth_largest([15], 1) == 15

    # Module example & duplicates
    assert kth_largest([7, 2, 9, 4, 15, 6], 3) == 7
    assert kth_largest([4, 4, 4, 2, 9, 9], 2) == 9
    assert kth_largest([4, 4, 4, 2, 9, 9], 3) == 4

    # Longer random sequence verified against sorting
    rng = random.Random(202)
    rand_seq = [rng.randint(-300, 300) for _ in range(200)]
    ref_desc = sorted(rand_seq, reverse=True)
    for k in [1, 3, 10, 50, 100, len(rand_seq)]:
        assert kth_largest(rand_seq, k) == ref_desc[k - 1]


def test_activity_5_merge_k_sorted_arrays() -> None:
    # Empty & single element
    assert merge_k_sorted_arrays([]) == []
    assert merge_k_sorted_arrays([[], [], []]) == []
    assert merge_k_sorted_arrays([[8]]) == [8]

    # Three sorted arrays of different lengths + duplicates
    assert merge_k_sorted_arrays([[1, 5, 9], [2, 6], [0, 12, 15, 20]]) == [
        0, 1, 2, 5, 6, 9, 12, 15, 20
    ]
    assert merge_k_sorted_arrays([[1, 3, 3, 7], [1, 2, 3], [0, 3, 8, 9, 10]]) == [
        0, 1, 1, 2, 3, 3, 3, 3, 7, 8, 9, 10
    ]

    # Longer random arrays
    rng = random.Random(303)
    arrays = [
        sorted(rng.randint(-150, 150) for _ in range(rng.randint(0, 50)))
        for _ in range(5)
    ]
    expected = sorted(val for arr in arrays for val in arr)
    assert merge_k_sorted_arrays(arrays) == expected


def test_activity_6_priority_scheduler() -> None:
    # Empty
    empty_sched = PriorityScheduler()
    assert empty_sched.step() is None
    assert empty_sched.release_order == []

    # Single element
    single_sched = PriorityScheduler()
    single_sched.submit("init-boot", 10)
    assert single_sched.run_all() == ["init-boot"]

    # Duplicates + mixed priorities
    sched = PriorityScheduler()
    sched.submit("disk-cleanup", 1)
    sched.submit("hardware-interrupt", 10)
    sched.submit("email-sync", 1)
    sched.submit("audio-stream", 7)
    sched.submit("network-packet", 7)

    order = sched.run_all()
    assert order == [
        "hardware-interrupt",
        "audio-stream",
        "network-packet",
        "disk-cleanup",
        "email-sync",
    ]
    print("Activity 6 Scheduler Release Order:", order)


if __name__ == "__main__":
    test_activity_1_min_heap()
    test_activity_2_max_heap()
    test_activity_3_heap_sort()
    test_activity_4_kth_largest()
    test_activity_5_merge_k_sorted_arrays()
    test_activity_6_priority_scheduler()
    print("All Activity 8 tests passed successfully!")