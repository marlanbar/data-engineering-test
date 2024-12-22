import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_distribution_of_crate_type(orders_df, output_dir):
    """Plot and save the distribution of orders by crate type."""
    plt.figure(figsize=(10, 6))
    sns.countplot(data=orders_df, x='crate_type', order=orders_df['crate_type'].value_counts().index)
    plt.title('Distribution of Orders by Crate Type')
    plt.xlabel('Crate Type')
    plt.ylabel('Number of Orders')
    plt.savefig(os.path.join(output_dir, 'distribution_of_orders_by_crate_type.png'))
    plt.close()

def plot_sales_owners_needing_training(orders_df, output_dir):
    """Plot and save sales owners needing training for plastic crates over the last 12 months."""
    # Ensure the 'date' column is in datetime format
    orders_df['date'] = pd.to_datetime(orders_df['date'], format='%d.%m.%y', errors='coerce')
    
    # Determine the last date in the dataset
    last_date = orders_df['date'].max()
    
    # Filter for the last 12 months
    start_date = last_date - pd.DateOffset(months=12)
    recent_orders = orders_df[(orders_df['date'] > start_date) & (orders_df['crate_type'].str.lower() == 'plastic')]
    
    # Count orders per sales owner
    plastic_salesowners = recent_orders['salesowners'].explode().value_counts()
    
    plt.figure(figsize=(14, 6))
    sns.barplot(x=plastic_salesowners.values, y=plastic_salesowners.index)
    plt.title('Sales Owners Needing Training on Plastic Crates (Last 12 Months)')
    plt.xlabel('Number of Plastic Crate Orders')
    plt.ylabel('Sales Owner')
    plt.savefig(os.path.join(output_dir, 'sales_owners_needing_training.png'))
    plt.close()

def plot_top_performers_plastic_crates(orders_df, output_dir):
    """Plot and save top performers selling plastic crates."""
    # Ensure the 'date' column is in datetime format
    orders_df['date'] = pd.to_datetime(orders_df['date'], format='%d.%m.%y', errors='coerce')
    
    # Filter for plastic crates and create a copy to avoid SettingWithCopyWarning
    plastic_orders = orders_df[orders_df['crate_type'].str.lower() == 'plastic'].copy()
    
    # Drop rows with invalid dates
    plastic_orders.dropna(subset=['date'], inplace=True)
    
    # Extract the month from the date
    plastic_orders['month'] = plastic_orders['date'].dt.to_period('M').astype(str)
    
    # Explode salesowners and group by month and salesowners
    exploded = plastic_orders.explode('salesowners')
    monthly_counts = exploded.groupby(['month', 'salesowners']).size().reset_index(name='order_count')
    
    # Calculate rolling 3-month sum
    monthly_counts['rolling_sum'] = monthly_counts.groupby('salesowners')['order_count'].transform(lambda x: x.rolling(3, min_periods=1).sum())
    
    # Get top 5 performers based on the latest rolling sum
    latest_month = monthly_counts['month'].max()
    top_performers = monthly_counts[monthly_counts['month'] == latest_month].nlargest(5, 'rolling_sum')['salesowners']
    
    # Filter data for top performers
    top_performers_data = monthly_counts[monthly_counts['salesowners'].isin(top_performers)]
    
    plt.figure(figsize=(12, 8))
    sns.lineplot(data=top_performers_data, x='month', y='rolling_sum', hue='salesowners', marker='o')
    plt.title('Top 5 Performers Selling Plastic Crates (Rolling 3-Month Window)')
    plt.xlabel('Month')
    plt.ylabel('Number of Plastic Crate Orders (3-Month Rolling Sum)')
    plt.xticks(rotation=45)
    plt.legend(title='Sales Owner')
    plt.savefig(os.path.join(output_dir, 'top_performers_plastic_crates.png'))
    plt.close()