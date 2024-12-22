import unittest
import pandas as pd
from src.test_3_contact_address import dataframe_with_contact_address

class TestContactAddress(unittest.TestCase):
    def test_contact_address(self):
        # Mock data simulating orders.csv structure
        data = {
            'order_id': ['order1', 'order2', 'order3', 'order4'],
            'contact_data': [
                [{'city': 'New York', 'cp': '10001'}],  # Full address
                [{'city': 'Los Angeles'}],  # Only city
                [{'cp': '90210'}],  # Only postal code
                {}  # No contact data
            ]
        }
        orders_df = pd.DataFrame(data)

        # Expected output
        expected_data = {
            'order_id': ['order1', 'order2', 'order3', 'order4'],
            'contact_address': ['New York, 10001', 'Los Angeles, UNK00', 'Unknown, 90210', 'Unknown, UNK00']
        }
        expected_df = pd.DataFrame(expected_data)

        # Function call
        df_2 = dataframe_with_contact_address(orders_df)

        # Test
        pd.testing.assert_frame_equal(df_2.reset_index(drop=True), expected_df)

if __name__ == '__main__':
    unittest.main()