import pandas as pd

def distribution_of_crate_type_per_company(orders_df):
    """
    Calculate the distribution of crate types per company.

    Parameters:
    - orders_df: DataFrame containing orders data.

    Returns:
    - DataFrame with columns ['company_id', 'crate_type', 'order_count'].
    """
    # Group by company_id and crate_type, then count the number of orders
    crate_distribution = (
        orders_df.groupby(['company_id', 'crate_type'])
        .size()
        .reset_index(name='order_count')
    )
    return crate_distribution