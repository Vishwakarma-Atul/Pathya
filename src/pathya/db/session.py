
import os
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker


DATABASE_URL = os.environ.get("DATABASE_URL")
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_orders(customer_id: str):
    with SessionLocal() as session:
        query = text("SELECT order_id, status FROM orders WHERE customer_id = :customer_id")
        result = session.execute(query, {"customer_id": customer_id}).fetchall()
        return [{"order_id": row[0], "status": row[1]} for row in result]

def get_order_details(order_id: str):
    with SessionLocal() as session:
        query = text("SELECT order_id, status, delivery_date FROM orders WHERE order_id = :order_id")
        result = session.execute(query, {"order_id": order_id}).fetchone()
        return {"order_id": result[0], "status": result[1], "delivery_date": result[2]} if result else None
