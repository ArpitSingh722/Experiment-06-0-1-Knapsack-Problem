import unittest
from knapsack import knapsack_bottom_up, knapsack_top_down


class TestKnapsack(unittest.TestCase):
    def test_sample_case(self):
        weights = [2, 1, 3, 2]
        values = [12, 10, 20, 15]
        capacity = 5

        best_value, selected = knapsack_bottom_up(weights, values, capacity)
        self.assertEqual(best_value, 37)
        self.assertEqual(knapsack_top_down(weights, values, capacity), 37)
        self.assertEqual(sum(weights[i] for i in selected), 5)
        self.assertEqual(sum(values[i] for i in selected), 37)

    def test_capacity_zero(self):
        self.assertEqual(knapsack_bottom_up([1, 2], [10, 20], 0), (0, []))
        self.assertEqual(knapsack_top_down([1, 2], [10, 20], 0), 0)

    def test_no_item_fits(self):
        self.assertEqual(knapsack_bottom_up([4, 5], [10, 20], 3), (0, []))
        self.assertEqual(knapsack_top_down([4, 5], [10, 20], 3), 0)

    def test_empty_items(self):
        self.assertEqual(knapsack_bottom_up([], [], 10), (0, []))
        self.assertEqual(knapsack_top_down([], [], 10), 0)


if __name__ == "__main__":
    unittest.main()
