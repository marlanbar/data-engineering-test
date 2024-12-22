import os
from data_loading import load_orders_data, load_invoicing_data
from test_1_crate_distribution import distribution_of_crate_type_per_company
from test_2_contact_full_name import dataframe_with_full_name
from test_3_contact_address import dataframe_with_contact_address
from test_4_commissions import calculate_total_commissions
from test_5_companies_salesowners import dataframe_of_companies_with_salesowners

def main():
    # Load data
    print("Loading data...")
    orders_df = load_orders_data('resources/orders.csv')
    invoicing_df = load_invoicing_data('resources/invoicing_data.json')

    output_dir = 'output'

    # Test 1: Distribution of Crate Type per Company
    print("Running Test 1: Distribution of Crate Type per Company")
    crate_distribution_df = distribution_of_crate_type_per_company(orders_df)
    crate_distribution_df.to_csv(os.path.join(output_dir, 'crate_distribution.csv'), index=False)
    print("Test 1 completed. Output written to crate_distribution.csv\n")

    # Test 2: DataFrame of Orders with Full Name of the Contact
    print("Running Test 2: DataFrame of Orders with Full Name of the Contact")
    df_1 = dataframe_with_full_name(orders_df)
    df_1.to_csv(os.path.join(output_dir, 'orders_with_full_name.csv'), index=False)
    print("Test 2 completed. Output written to orders_with_full_name.csv\n")

    # Test 3: DataFrame of Orders with Contact Address
    print("Running Test 3: DataFrame of Orders with Contact Address")
    df_2 = dataframe_with_contact_address(orders_df)
    df_2.to_csv(os.path.join(output_dir, 'orders_with_contact_address.csv'), index=False)
    print("Test 3 completed. Output written to orders_with_contact_address.csv\n")

    # Test 4: Calculation of Sales Team Commissions
    print("Running Test 4: Calculation of Sales Team Commissions")
    total_commissions_df = calculate_total_commissions(orders_df, invoicing_df)
    total_commissions_df.to_csv(os.path.join(output_dir, 'sales_team_commissions.csv'), index=False)
    print("Test 4 completed. Output written to sales_team_commissions.csv\n")

    # Test 5: DataFrame of Companies with Sales Owners
    print("Running Test 5: DataFrame of Companies with Sales Owners")
    df_3 = dataframe_of_companies_with_salesowners(orders_df)
    df_3.to_csv(os.path.join(output_dir, 'companies_with_salesowners.csv'), index=False)
    print("Test 5 completed. Output written to companies_with_salesowners.csv\n")

if __name__ == '__main__':
    main()
