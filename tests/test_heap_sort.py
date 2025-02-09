from heap_sort import heap_sort

def test_heap_sort():
    assert heap_sort([3, 1, 4, 1, 5, 9]) == [1, 1, 3, 4, 5, 9]
    assert heap_sort([]) == []
    assert heap_sort([5]) == [5]
