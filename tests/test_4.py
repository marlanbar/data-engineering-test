import unittest
import pandas as pd
from src.test_4_commissions import calculate_total_commissions

class TestCommissions(unittest.TestCase):
    def test_commissions(self):
        # Mock orders data
        orders_data = {
            'order_id': ['ord1', 'ord2'],
            'salesowners': [['Alice', 'Bob', 'Charlie'], ['Dave', 'Eve']],
        }
        orders_df = pd.DataFrame(orders_data)

        # Mock invoicing data
        invoicing_data = {
            'orderId': ['ord1', 'ord2'],
            'grossValue': ['20000', '10000'],  # in cents
            'vat': ['0', '0']
        }
        invoicing_df = pd.DataFrame(invoicing_data)

        # Expected commissions
        expected_commissions = {
            'Alice': 12.00,    # 200 euros * 6%
            'Bob': 5.00,       # 200 euros * 2.5%
            'Charlie': 1.90,   # 200 euros * 0.95%
            'Dave': 6.00,      # 100 euros * 6%
            'Eve': 2.50        # 100 euros * 2.5%
        }

        # Function call
        total_commissions_df = calculate_total_commissions(orders_df, invoicing_df)

        # Convert to dictionary for testing
        result_commissions = dict(zip(
            total_commissions_df['salesowner'],
            total_commissions_df['commission']
        ))

        # Test
        for owner, expected in expected_commissions.items():
            self.assertAlmostEqual(result_commissions.get(owner, 0.0), expected, places=2)

if __name__ == '__main__':
    unittest.main()