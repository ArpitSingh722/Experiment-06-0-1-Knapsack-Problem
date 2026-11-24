# Experiment 06 – 0/1 Knapsack Problem

## Aim
Apply dynamic programming techniques for optimal selection of items to maximize value within a weight constraint using bottom-up and top-down approaches.

## Description
This program solves the 0/1 Knapsack Problem using two dynamic programming techniques:

- **Bottom-Up (Tabulation):** Builds a DP table iteratively and reconstructs the selected items.
- **Top-Down (Memoization):** Solves the problem recursively while caching previously computed results.

Each item can either be selected once or not selected. The total weight of selected items must not exceed the knapsack capacity.

## Files
- `knapsack.py` – Main program containing both approaches.
- `test_knapsack.py` – Unit tests.
- `sample_input.txt` – Example input.
- `sample_output.txt` – Expected output.
- `requirements.txt` – External dependencies (none required).
- `.gitignore` – Git ignore rules.

## How to Run
Make sure Python 3 is installed. Open a terminal in this folder and run:

```bash
python knapsack.py
```

Enter the number of items, each item's weight and value, and the maximum knapsack capacity.

## Sample Input
```text
4
2
12
1
10
3
20
2
15
5
```

## Sample Output
```text
Maximum value (Bottom-Up): 37
Maximum value (Top-Down): 37
Selected items (1-based): [1, 2, 4]
Total weight: 5
```

## Algorithm
1. Create a DP table for the bottom-up approach.
2. For each item and capacity, compare excluding the item with including it, if it fits.
3. Use the final DP table entry as the maximum value.
4. Trace the table to identify selected items.
5. In the top-down approach, use recursion and memoization to calculate the maximum value.
6. Compare the answers from both approaches.

## Complexity
Let `n` be the number of items and `W` be the knapsack capacity.

| Approach | Time Complexity | Space Complexity |
|---|---|---|
| Bottom-Up | O(n × W) | O(n × W) |
| Top-Down | O(n × W) | O(n × W) |

The top-down approach may also use recursion stack space.
