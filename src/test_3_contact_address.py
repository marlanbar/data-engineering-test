def create_contact_address(contact_data):
    """
    Format the contact address as "city name, postal code",
    using placeholders if necessary.

    Parameters:
    - contact_data: Dictionary containing contact information.

    Returns:
    - String of the contact address.
    """
    if not contact_data:
        city = 'Unknown'
        postal_code = 'UNK00'
    else:
        if isinstance(contact_data, list) and contact_data:
            contact_info = contact_data[0]
        elif isinstance(contact_data, dict):
            contact_info = contact_data
        else:
            city = 'Unknown'
            postal_code = 'UNK00'
            return f"{city}, {postal_code}"
        
        city = contact_info.get('city', 'Unknown')
        postal_code = contact_info.get('cp', 'UNK00')
        
        if not city:
            city = 'Unknown'
        if not postal_code:
            postal_code = 'UNK00'
        postal_code = str(postal_code)
    
    return f"{city}, {postal_code}"

def dataframe_with_contact_address(orders_df):
    """
    Provide a DataFrame containing order_id and contact_address.

    Parameters:
    - orders_df: DataFrame containing orders data.

    Returns:
    - DataFrame with columns ['order_id', 'contact_address'].
    """
    orders_df['contact_address'] = orders_df['contact_data'].apply(create_contact_address)
    df_2 = orders_df[['order_id', 'contact_address']].copy()
    return df_2