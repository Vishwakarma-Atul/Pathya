import pandas as pd
import os
from pathlib import Path

# Define the data directory
DATA_DIR = Path(__file__).parent

ORDERS_FILE = DATA_DIR / "orders.csv"

def get_orders(customer_id: str):
    df = pd.read_csv(ORDERS_FILE)
    customer_orders = df[df['customer_id'] == customer_id].to_dict('records')
    return customer_orders

def get_order_details(order_id: str):
    df = pd.read_csv(ORDERS_FILE)
    order = df[df['order_id'] == order_id].to_dict('records')
    return order[0] if order else None