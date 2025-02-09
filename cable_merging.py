import heapq

def min_cable_cost(cables):
    """Знаходить мінімальну вартість об'єднання кабелів."""
    heapq.heapify(cables)  # Перетворюємо список у мінімальну купу
    total_cost = 0

    while len(cables) > 1:
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)
        cost = first + second
        total_cost += cost
        heapq.heappush(cables, cost)

    return total_cost

if __name__ == "__main__":
    cables = [8, 4, 6, 12]
    print("Мінімальна вартість з'єднання:", min_cable_cost(cables))
