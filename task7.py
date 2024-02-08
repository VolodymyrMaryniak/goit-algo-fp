import random
import tabulate


def main():
    dice_sums = dict()

    count_of_experiments = 100_000
    for _ in range(count_of_experiments):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)

        dice_sum = dice1 + dice2
        dice_sums[dice_sum] = dice_sums.get(dice_sum, 0) + 1

    dice_sums_probabilities = [
        (sum, "{:.2%}".format(count / count_of_experiments))
        for (sum, count) in dice_sums.items()
    ]

    dice_sums_probabilities.sort(key=lambda x: x[0])
    print(tabulate.tabulate(dice_sums_probabilities, headers=["Sum", "Probability"], tablefmt="github"))


if __name__ == "__main__":
    main()
