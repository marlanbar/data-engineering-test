import pandas as pd
import re

def normalize_company_name(name):
    """
    Normalize the company name by converting to lowercase and removing special characters.

    Parameters:
    - name: Original company name.

    Returns:
    - Normalized company name.
    """
    if pd.isna(name):
        return ''
    return re.sub(r'\W+', '', name).lower()

def get_unique_salesowners(salesowners_list):
    """
    Get a list of unique salesowners sorted alphabetically by first name.

    Parameters:
    - salesowners_list: List of salesowners lists.

    Returns:
    - List of unique salesowners sorted alphabetically by first name.
    """
    unique_salesowners = set(salesowners_list)
    sorted_salesowners = sorted(unique_salesowners, key=lambda x: x.split()[0])
    return sorted_salesowners

def dataframe_of_companies_with_salesowners(orders_df):
    """
    Provide a DataFrame containing company_id, company_name, and list_salesowners.

    Parameters:
    - orders_df: DataFrame containing orders data.

    Returns:
    - DataFrame with columns ['company_id', 'company_name', 'list_salesowners'].
    """
    # Normalize company names to identify duplicates
    orders_df['normalized_company_name'] = orders_df['company_name'].apply(normalize_company_name)

    # Group by normalized company name and aggregate salesowners
    grouped = orders_df.groupby('normalized_company_name').agg({
        'company_id': 'first',  # Take the first company_id encountered
        'company_name': 'first',  # Take the first company_name encountered
        'salesowners': lambda x: sum(x, [])  # Flatten the list of lists
    }).reset_index(drop=True)

    # Get unique salesowners per company
    grouped['list_salesowners'] = grouped['salesowners'].apply(get_unique_salesowners)

    # Convert list to comma-separated string
    grouped['list_salesowners'] = grouped['list_salesowners'].apply(lambda lst: ', '.join(lst))

    df_3 = grouped[['company_id', 'company_name', 'list_salesowners']].copy()

    return df_3