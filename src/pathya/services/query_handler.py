
from ..db.session import get_orders, get_order_details

def handle_query(intent, extracted_values, customer_id):
    if intent == "order_status":
        orders = get_orders(customer_id)
        if not orders:
            return "No orders found for your account."
        return "Here are your recent orders:\n" + "\n".join(
            [f"- Order {order['order_id']}: {order['status']}" for order in orders]
        )

    elif intent == "order_details":
        order_id = extracted_values[0] if extracted_values else None
        if not order_id:
            return "Please provide a valid order ID."
        order = get_order_details(order_id)
        if not order:
            return f"No details found for order {order_id}."
        return f"Order {order['order_id']} is {order['status']} and will be delivered by {order['delivery_date']}."

    return "Sorry, I don't understand your request."
