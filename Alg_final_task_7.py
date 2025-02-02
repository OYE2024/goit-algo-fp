import random
import matplotlib.pyplot as plt


def simulate_dice_rolls(num_rolls=1000000):
    sums_count = {i: 0 for i in range(2, 13)}  # Можливі суми (від 2 до 12)

    for _ in range(num_rolls):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        roll_sum = dice1 + dice2
        sums_count[roll_sum] += 1

    probabilities = {s: count / num_rolls for s, count in sums_count.items()}
    return sums_count, probabilities


def plot_probabilities(probabilities):
    sums = list(probabilities.keys())
    probs = [p * 100 for p in probabilities.values()]

    plt.bar(sums, probs, color='blue', alpha=0.7, edgecolor='black')
    plt.xlabel('Сума чисел на кубиках')
    plt.ylabel('Ймовірність (%)')
    plt.title('Ймовірності сум чисел на двох кубиках')
    plt.xticks(sums)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()


def print_table(sums_count, probabilities):
    print("\nТаблиця ймовірностей сум чисел на двох кубиках:")
    print("Сума | Кількість | Ймовірність (%)")
    print("---------------------------------")
    for s in range(2, 13):
        print(f" {s:2d}  | {sums_count[s]:9d} | {probabilities[s] * 100:.2f}")


if __name__ == "__main__":
    num_rolls = 1000000  # Кількість кидків
    sums_count, probabilities = simulate_dice_rolls(num_rolls)
    print_table(sums_count, probabilities)
    plot_probabilities(probabilities)
