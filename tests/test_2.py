import unittest
import pandas as pd
from src.test_2_contact_full_name import dataframe_with_full_name

class TestContactFullName(unittest.TestCase):
    def test_full_name(self):
        # Mock data simulating orders.csv structure
        data = {
            'order_id': ['order1', 'order2', 'order3', 'order4'],
            'contact_data': [
                [{'contact_name': 'Alice', 'contact_surname': 'Smith'}],  # Full name
                [{'contact_name': 'Bob'}],  # Only first name
                [{'contact_surname': 'Johnson'}],  # Only last name
                {}  # No contact data
            ]
        }
        orders_df = pd.DataFrame(data)

        # Expected output
        expected_data = {
            'order_id': ['order1', 'order2', 'order3', 'order4'],
            'contact_full_name': ['Alice Smith', 'Bob', 'Johnson', 'John Doe']
        }
        expected_df = pd.DataFrame(expected_data)

        # Function call
        df_1 = dataframe_with_full_name(orders_df)

        # Test
        pd.testing.assert_frame_equal(df_1.reset_index(drop=True), expected_df)

if __name__ == '__main__':
    unittest.main()