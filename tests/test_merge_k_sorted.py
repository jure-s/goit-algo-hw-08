from merge_k_sorted import merge_k_lists

def test_merge_k_lists():
    assert merge_k_lists([[1, 4, 5], [1, 3, 4], [2, 6]]) == [1, 1, 2, 3, 4, 4, 5, 6]
    assert merge_k_lists([[], [1], [2, 3]]) == [1, 2, 3]
    assert merge_k_lists([[]]) == []
