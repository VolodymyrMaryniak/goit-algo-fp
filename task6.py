def greedy_algorithm(items: dict, max_cost):
    items_array = sorted(
        items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True
    )

    current_cost = 0
    total_calories = 0
    for _, item_data in items_array:
        if current_cost + item_data["cost"] > max_cost:
            continue

        total_calories += item_data["calories"]
        current_cost += item_data["cost"]

    return total_calories


def dynamic_algorithm(items: dict, max_cost):
    items_array = list(items.items())
    total_count_of_items = len(items_array)

    # створюємо таблицю K для зберігання оптимальних значень підзадач
    K = [[0 for _ in range(max_cost + 1)] for _ in range(total_count_of_items + 1)]

    # будуємо таблицю K знизу вгору
    for sub_count_of_items in range(total_count_of_items + 1):
        for sub_max_cost in range(max_cost + 1):
            if sub_count_of_items == 0 or sub_max_cost == 0:
                K[sub_count_of_items][sub_max_cost] = 0
                continue

            _, item_data = items_array[sub_count_of_items - 1]
            if item_data["cost"] <= sub_max_cost:
                K[sub_count_of_items][sub_max_cost] = max(
                    item_data["calories"]
                    + K[sub_count_of_items - 1][sub_max_cost - item_data["cost"]],
                    K[sub_count_of_items - 1][sub_max_cost],
                )
            else:
                K[sub_count_of_items][sub_max_cost] = K[sub_count_of_items - 1][
                    sub_max_cost
                ]

    return K[total_count_of_items][max_cost]


def main():
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350},
    }

    max_cost = 75

    print("Max cost: ", max_cost)

    total_calories = greedy_algorithm(items, max_cost)
    print(f"Total calories (Greedy algorithm): {total_calories}")

    total_calories = dynamic_algorithm(items, max_cost)
    print(f"Total calories (Dynamic algorithm): {total_calories}")


if __name__ == "__main__":
    main()
