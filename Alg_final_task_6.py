items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}


def greedy_algorithm(items, budget):
    # Сортуємо елементи за калоріями на одиницю вартості у спадному порядку
    sorted_items = sorted(
        items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)

    total_calories = 0
    remaining_budget = budget
    chosen_items = []

    for item, details in sorted_items:
        if details['cost'] <= remaining_budget:
            chosen_items.append(item)
            total_calories += details['calories']
            remaining_budget -= details['cost']

    return total_calories, budget - remaining_budget, chosen_items


def dynamic_programming(items, budget):
    item_names = list(items.keys())
    dp_table = [[0 for x in range(budget+1)] for y in range(len(items)+1)]

    # Заповнюємо таблицю динамічного програмування
    for i in range(1, len(items) + 1):
        for b in range(budget + 1):
            item = item_names[i-1]
            item_cost = items[item]['cost']
            item_calories = items[item]['calories']

            if item_cost <= b:
                dp_table[i][b] = max(
                    dp_table[i-1][b], dp_table[i-1][b-item_cost] + item_calories)
            else:
                dp_table[i][b] = dp_table[i-1][b]

    # Визначаємо вибрані елементи
    chosen_items = []
    temp_budget = budget
    for i in range(len(items), 0, -1):
        if dp_table[i][temp_budget] != dp_table[i-1][temp_budget]:
            item = item_names[i-1]
            chosen_items.append(item)
            temp_budget -= items[item]['cost']

    return dp_table[len(items)][budget], budget - temp_budget, chosen_items


if __name__ == '__main__':
    budget = 100
    print(greedy_algorithm(items, budget))
    print(dynamic_programming(items, budget))
