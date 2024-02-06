import numpy as np
import matplotlib.pyplot as plt


def draw_tree(ax, x, y, length, angle, depth):
    if depth == 0:
        return

    x_end = x + length * np.cos(np.radians(angle))
    y_end = y + length * np.sin(np.radians(angle))
    ax.plot([x, x_end], [y, y_end], color="brown")

    # Calculate new lengths for the branches
    left_length = length * np.cos(np.radians(45))
    right_length = length * np.sin(np.radians(45))

    # Calculate new angles for the branches
    left_angle = angle - 45
    right_angle = angle + 45

    draw_tree(ax, x_end, y_end, left_length, left_angle, depth - 1)
    draw_tree(ax, x_end, y_end, right_length, right_angle, depth - 1)


def main():
    depth_input = input("Enter the recursion depth level for build Pythagoras tree: ")
    if not depth_input.isdigit():
        print("Invalid input")
        return

    depth = int(depth_input)

    _, ax = plt.subplots()
    ax.set_aspect("equal", "box")
    ax.axis("off")

    # Set the initial parameters
    x_start, y_start = 0, 0
    trunk_length = 1
    trunk_angle = 90

    draw_tree(ax, x_start, y_start, trunk_length, trunk_angle, depth)

    plt.show()


if __name__ == "__main__":
    main()
