import heapq
import colorama
from colorama import Fore, Style
from heap_sort import heap_sort
from cable_merging import min_cable_cost
from merge_k_sorted import merge_k_lists

colorama.init(autoreset=True)  # Автоматично скидає колір після кожного виводу

def main():
    while True:
        print(Fore.CYAN + "\n🔹 Виберіть операцію:")
        print(Fore.YELLOW + "1 - Пірамідальне сортування")
        print(Fore.YELLOW + "2 - Об'єднання кабелів з мінімальними витратами")
        print(Fore.YELLOW + "3 - Об'єднання k відсортованих списків")
        print(Fore.RED + "4 - Вийти")

        choice = input(Fore.GREEN + "Введіть номер операції: ")

        if choice == "1":
            numbers = list(map(int, input(Fore.BLUE + "Введіть числа через пробіл: ").split()))
            sorted_numbers = heap_sort(numbers)
            print(Fore.MAGENTA + "✅ Відсортований список:", sorted_numbers)

        elif choice == "2":
            cables = list(map(int, input(Fore.BLUE + "Введіть довжини кабелів через пробіл: ").split()))
            cost = min_cable_cost(cables)
            print(Fore.MAGENTA + "✅ Мінімальна вартість з'єднання:", cost)

        elif choice == "3":
            k = int(input(Fore.BLUE + "Скільки списків хочете ввести? "))
            lists = []
            for i in range(k):
                lst = sorted(map(int, input(Fore.BLUE + f"Введіть числа для списку {i+1} через пробіл: ").split()))
                lists.append(lst)  # Сортуємо кожен підсписок перед додаванням

            merged_list = merge_k_lists(lists)
            print(Fore.MAGENTA + "✅ Відсортований список:", merged_list)

        elif choice == "4":
            print(Fore.RED + "👋 Вихід...")
            break

        else:
            print(Fore.RED + "❌ Некоректний вибір, спробуйте ще раз.")

if __name__ == "__main__":
    main()
