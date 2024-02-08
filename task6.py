def greedy_algorithm(items: dict, max_cost):
    items_array = sorted(
        items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True
    )

    current_cost = 0
    total_calories = 0
    chosen_items = []

    for item_name, item_data in items_array:
        if current_cost + item_data["cost"] > max_cost:
            continue

        chosen_items.append(item_name)
        total_calories += item_data["calories"]
        current_cost += item_data["cost"]

    return (total_calories, chosen_items)


def dynamic_algorithm(items: dict, max_cost):
    items_array = list(items.items())
    total_count_of_items = len(items_array)

    last_item_used = [[None] * (max_cost + 1) for _ in range(total_count_of_items + 1)]

    # створюємо таблицю K для зберігання оптимальних значень підзадач
    K = [[0] * (max_cost + 1) for _ in range(total_count_of_items + 1)]

    # будуємо таблицю K знизу вгору
    for item_index in range(total_count_of_items + 1):
        for cost_index in range(max_cost + 1):
            if item_index == 0 or cost_index == 0:
                K[item_index][cost_index] = 0
                continue

            item_name, item_data = items_array[item_index - 1]
            if item_data["cost"] > cost_index:
                K[item_index][cost_index] = K[item_index - 1][cost_index]
                last_item_used[item_index][cost_index] = last_item_used[item_index - 1][
                    cost_index
                ]
                continue

            cost_index_without_item = cost_index - item_data["cost"]
            calories_with_item = (
                item_data["calories"] + K[item_index - 1][cost_index_without_item]
            )

            if calories_with_item > K[item_index - 1][cost_index]:
                K[item_index][cost_index] = calories_with_item
                last_item_used[item_index][cost_index] = item_name
                continue

            K[item_index][cost_index] = K[item_index - 1][cost_index]
            last_item_used[item_index][cost_index] = last_item_used[item_index - 1][
                cost_index
            ]

    item_names = build_solution(last_item_used, max_cost, items)
    return (K[total_count_of_items][max_cost], item_names)


def build_solution(last_item_used: list[list[str]], max_cost: int, items: dict):
    count_of_items = len(items)
    item_names = []
    while max_cost > 0:
        item_name = last_item_used[count_of_items][max_cost]
        if item_name is None:
            break

        item_names.append(item_name)
        max_cost -= items[item_name]["cost"]
        count_of_items -= 1

    return item_names


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

    total_calories, item_names = greedy_algorithm(items, max_cost)
    print(f"Total calories (Greedy algorithm): {total_calories}")
    print(f"Items: {item_names}\n")

    total_calories, item_names = dynamic_algorithm(items, max_cost)
    print(f"Total calories (Dynamic algorithm): {total_calories}")
    print(f"Items: {item_names}")


if __name__ == "__main__":
    main()
