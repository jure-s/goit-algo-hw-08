import heapq

def heap_sort(arr):
    """Пірамідальне сортування з використанням купи."""
    heapq.heapify(arr)  # Створюємо мінімальну купу
    return [heapq.heappop(arr) for _ in range(len(arr))]

if __name__ == "__main__":
    numbers = [5, 3, 8, 1, 2, 7]
    print("Відсортований список:", heap_sort(numbers))