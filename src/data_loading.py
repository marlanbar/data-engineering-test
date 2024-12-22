import pandas as pd
import json

def parse_contact_data(contact_data_str):
    """
    Parse the contact_data JSON string.

    Handles various data formats:
    - JSON array
    - JSON object
    - Malformed JSON starting as an array but ending as an object.

    Parameters:
    - contact_data_str: String containing JSON data.

    Returns:
    - Dictionary with contact information or empty dict if invalid.
    """
    if pd.isna(contact_data_str) or contact_data_str.strip() == '':
        return {}

    # Normalize the string by replacing single quotes with double quotes
    normalized_str = contact_data_str.replace("'", '"').replace('""', '"')

    try:
        if normalized_str.startswith('[') and not normalized_str.endswith(']'):
            # Handle the case where it starts as an array but ends as an object
            normalized_str = normalized_str.lstrip('[').rstrip(']')
            # Attempt to load it as a JSON object
            contact_data = json.loads(normalized_str)
            if isinstance(contact_data, dict):
                return contact_data
        
        # Attempt to parse the normalized string as JSON
        contact_data = json.loads(normalized_str)
        
        if isinstance(contact_data, list) and contact_data:
            return contact_data[0]  # Return the first element if a list
        elif isinstance(contact_data, dict):
            return contact_data  # Directly return if it's a JSON object
        else:
            print(f"Unexpected JSON format: {contact_data_str}")
            return {}
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {contact_data_str} - {e}")
        return {}

def parse_salesowners(salesowners_str):
    """
    Split the salesowners string into a list.
    """
    if pd.isna(salesowners_str) or salesowners_str.strip() == '':
        return []
    return [name.strip() for name in salesowners_str.split(',')]

def load_orders_data(filepath):
    """
    Load and preprocess orders data from CSV file.
    """
    orders_df = pd.read_csv(filepath, sep=';', converters={
        'contact_data': parse_contact_data,
        'salesowners': parse_salesowners
    })
    return orders_df

def load_invoicing_data(filepath):
    """
    Load and preprocess invoicing data from JSON file.
    """
    with open(filepath, 'r') as f:
        invoicing_json = json.load(f)
    # Extract the invoices list
    invoices = invoicing_json.get('data', {}).get('invoices', [])
    invoicing_df = pd.DataFrame(invoices)
    return invoicing_df