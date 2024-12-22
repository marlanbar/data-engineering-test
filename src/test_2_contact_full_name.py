def create_full_name(contact_data):
    """
    Extract or construct the full name from contact_data.

    Parameters:
    - contact_data: Dictionary containing contact information.

    Returns:
    - Full name string or 'John Doe' placeholder.
    """
    if not contact_data:
        return 'John Doe'
    else:
        # Handle possible list or dict structures
        if isinstance(contact_data, list) and contact_data:
            contact_info = contact_data[0]
        elif isinstance(contact_data, dict):
            contact_info = contact_data
        else:
            return 'John Doe'
        
        first_name = contact_info.get('contact_name')
        last_name = contact_info.get('contact_surname')
        
        if first_name and last_name:
            return f"{first_name} {last_name}"
        elif first_name:
            return first_name
        elif last_name:
            return last_name
        else:
            return 'John Doe'

def dataframe_with_full_name(orders_df):
    """
    Provide a DataFrame containing order_id and contact_full_name.

    Parameters:
    - orders_df: DataFrame containing orders data.

    Returns:
    - DataFrame with columns ['order_id', 'contact_full_name'].
    """
    orders_df['contact_full_name'] = orders_df['contact_data'].apply(create_full_name)
    df_1 = orders_df[['order_id', 'contact_full_name']].copy()
    return df_1