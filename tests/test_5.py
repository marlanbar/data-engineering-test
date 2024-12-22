import unittest
import pandas as pd
from src.test_5_companies_salesowners import dataframe_of_companies_with_salesowners

class TestCompaniesWithSalesowners(unittest.TestCase):
    def test_companies_with_salesowners(self):
        # Mock data simulating orders.csv structure
        data = {
            'order_id': ['order1', 'order2', 'order3', 'order4'],
            'company_id': ['1', '2', '3', '4'],
            'company_name': ['Fresh Fruits Co', 'fresh fruits c.o', 'Veggies Inc', 'Veggies Inc.'],
            'salesowners': [['Alice'], ['Bob', 'Charlie'], ['Alice'], ['David']]
        }
        orders_df = pd.DataFrame(data)

        # Expected output
        expected_data = {
            'company_id': ['1', '3'],
            'company_name': ['Fresh Fruits Co', 'Veggies Inc'],
            'list_salesowners': ['Alice, Bob, Charlie', 'Alice, David']
        }
        expected_df = pd.DataFrame(expected_data)

        # Function call
        df_3 = dataframe_of_companies_with_salesowners(orders_df)

        # Sort results for comparison purposes
        df_3 = df_3.sort_values(by=['company_id']).reset_index(drop=True)
        expected_df = expected_df.sort_values(by=['company_id']).reset_index(drop=True)

        # Test
        pd.testing.assert_frame_equal(df_3, expected_df)

if __name__ == '__main__':
    unittest.main()