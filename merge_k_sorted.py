import heapq

def merge_k_lists(lists):
    """Об'єднує k відсортованих списків у один."""
    heap = []
    
    for i, lst in enumerate(lists):
        if lst:  # Якщо список не порожній
            heapq.heappush(heap, (lst[0], i, 0))  # (значення, індекс списку, індекс елемента)
    
    result = []
    while heap:
        val, list_idx, elem_idx = heapq.heappop(heap)
        result.append(val)

        if elem_idx + 1 < len(lists[list_idx]):
            heapq.heappush(heap, (lists[list_idx][elem_idx + 1], list_idx, elem_idx + 1))

    return result

if __name__ == "__main__":
    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    print("Відсортований список:", merge_k_lists(lists))
