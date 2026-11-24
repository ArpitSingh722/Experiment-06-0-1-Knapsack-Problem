from functools import lru_cache


def knapsack_bottom_up(weights, values, capacity):
    """Solve 0/1 Knapsack using tabulation and return max value and chosen indices."""
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for current_capacity in range(capacity + 1):
            dp[i][current_capacity] = dp[i - 1][current_capacity]

            if weights[i - 1] <= current_capacity:
                include = values[i - 1] + dp[i - 1][current_capacity - weights[i - 1]]
                dp[i][current_capacity] = max(
                    dp[i][current_capacity], include
                )

    # Reconstruct the selected items from the DP table.
    selected_indices = []
    current_capacity = capacity

    for i in range(n, 0, -1):
        if dp[i][current_capacity] != dp[i - 1][current_capacity]:
            selected_indices.append(i - 1)
            current_capacity -= weights[i - 1]

    selected_indices.reverse()
    return dp[n][capacity], selected_indices


def knapsack_top_down(weights, values, capacity):
    """Solve 0/1 Knapsack using recursion with memoization."""
    n = len(weights)

    @lru_cache(maxsize=None)
    def solve(index, remaining_capacity):
        if index == n or remaining_capacity == 0:
            return 0

        # Option 1: do not select the current item.
        best = solve(index + 1, remaining_capacity)

        # Option 2: select it if it fits.
        if weights[index] <= remaining_capacity:
            best = max(
                best,
                values[index] + solve(
                    index + 1, remaining_capacity - weights[index]
                )
            )

        return best

    return solve(0, capacity)


def main():
    print("0/1 KNAPSACK PROBLEM")
    n = int(input("Enter the number of items: "))

    weights = []
    values = []

    for i in range(n):
        print(f"Item {i + 1}:")
        weights.append(int(input("  Enter weight: ")))
        values.append(int(input("  Enter value: ")))

    capacity = int(input("Enter the maximum capacity of the knapsack: "))

    if n < 0 or capacity < 0 or any(w < 0 for w in weights):
        raise ValueError("Number of items, weights, and capacity must be non-negative.")

    max_value, selected = knapsack_bottom_up(weights, values, capacity)
    top_down_value = knapsack_top_down(weights, values, capacity)

    print("\nMaximum value (Bottom-Up):", max_value)
    print("Maximum value (Top-Down):", top_down_value)
    print("Selected items (1-based):", [index + 1 for index in selected])
    print("Total weight:", sum(weights[index] for index in selected))


if __name__ == "__main__":
    main()
