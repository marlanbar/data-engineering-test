import pandas as pd

def calculate_commission_per_order(row):
    """
    Calculate the commissions for sales owners of an order.

    Parameters:
    - row: A row of the merged DataFrame containing salesowners and netInvoicedAmount.

    Returns:
    - List of dictionaries with 'salesowner' and 'commission' keys.
    """
    salesowners = row.get('salesowners', [])
    net_invoiced_amount = float(row.get('netInvoicedAmount', 0)) / 100  # Convert to euros

    commissions = []
    for idx, owner in enumerate(salesowners):
        if idx == 0:
            commission_rate = 0.06
        elif idx == 1:
            commission_rate = 0.025
        elif idx == 2:
            commission_rate = 0.0095
        else:
            continue  # No commission for others
        commission_amount = round(net_invoiced_amount * commission_rate, 2)
        commissions.append({'salesowner': owner, 'commission': commission_amount})
    return commissions

def calculate_total_commissions(orders_df, invoicing_df):
    """
    Calculate the total commissions per salesowner.

    Parameters:
    - orders_df: DataFrame containing orders data.
    - invoicing_df: DataFrame containing invoicing data.

    Returns:
    - DataFrame with columns ['salesowner', 'commission'] sorted by descending commission.
    """
    # Adjust column names for consistency
    invoicing_df = invoicing_df.rename(columns={
        'orderId': 'order_id',
        'grossValue': 'grossValue',
        'vat': 'vat'
    })

    # Calculate net invoiced amount
    invoicing_df['netInvoicedAmount'] = invoicing_df['grossValue'].astype(float) - invoicing_df['vat'].astype(float)

    # Merge orders and invoicing data on 'order_id'
    merged_df = pd.merge(orders_df, invoicing_df[['order_id', 'netInvoicedAmount']], on='order_id', how='left')

    # Calculate commissions
    merged_df['commissions'] = merged_df.apply(calculate_commission_per_order, axis=1)

    # Flatten the list of commissions
    commissions_list = []
    for commissions in merged_df['commissions']:
        commissions_list.extend(commissions)

    commissions_df = pd.DataFrame(commissions_list)

    # Sum commissions per salesowner
    total_commissions_df = (
        commissions_df.groupby('salesowner')['commission']
        .sum()
        .reset_index()
        .sort_values(by='commission', ascending=False)
    )
    return total_commissions_df