import unittest
import pandas as pd
from src.test_1_crate_distribution import distribution_of_crate_type_per_company

class TestCrateDistribution(unittest.TestCase):
    def test_distribution(self):
        # Mock data simulating orders.csv structure
        data = {
            'company_id': [
                '1e2b47e6-499e-41c6-91d3-09d12dddfbbd',  # Fresh Fruits Co
                '0f05a8f1-2bdf-4be7-8c82-4c9b58f04898',  # Veggies Inc
                '1e2b47e6-499e-41c6-91d3-09d12dddfbbd',  # Fresh Fruits Co (duplicate)
                '1c4b0b50-1d5d-463a-b56e-1a6fd3aeb7d6',  # Seafood Supplier
                '34538e39-cd2e-4641-8d24-3c94146e6f16',  # Meat Packers Ltd
            ],
            'crate_type': ['Plastic', 'Wood', 'Metal', 'Plastic', 'Plastic'],
            'order_id': [
                'order1',
                'order2',
                'order3',
                'order4',
                'order5',
            ]
        }
        orders_df = pd.DataFrame(data)

        # Expected output
        expected_data = {
            'company_id': [
                '0f05a8f1-2bdf-4be7-8c82-4c9b58f04898',
                '1c4b0b50-1d5d-463a-b56e-1a6fd3aeb7d6',
                '1e2b47e6-499e-41c6-91d3-09d12dddfbbd',
                '1e2b47e6-499e-41c6-91d3-09d12dddfbbd',
                '34538e39-cd2e-4641-8d24-3c94146e6f16',
            ],
            'crate_type': ['Wood', 'Plastic', 'Metal', 'Plastic', 'Plastic'],
            'order_count': [1, 1, 1, 1, 1]
        }
        expected_df = pd.DataFrame(expected_data)

        # Function call
        result_df = distribution_of_crate_type_per_company(orders_df)

        # Sort results for comparison purposes
        result_df = result_df.sort_values(by=['company_id', 'crate_type']).reset_index(drop=True)
        expected_df = expected_df.sort_values(by=['company_id', 'crate_type']).reset_index(drop=True)

        # Test
        pd.testing.assert_frame_equal(result_df, expected_df)

if __name__ == '__main__':
    unittest.main()