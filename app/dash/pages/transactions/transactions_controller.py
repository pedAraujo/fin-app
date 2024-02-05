from app.mongo import db
import pandas as pd


def get_transactions_by_user(user_id):
    transactions_list = list(db.transactions.find({"user_id": user_id}))
    transactions_df = pd.DataFrame(transactions_list)
    return transactions_df


def prepare_transaction_for_insertion(transaction_info):
    transaction = {
        "date": transaction_info["date"],
        "type": "income" if transaction_info["transaction_type"] else "expense",
        "name": transaction_info["name"],
        "category": transaction_info["category"],
        "value": float(transaction_info["value"]),
        "frequency": transaction_info["frequency"],
        "description": transaction_info["description"],
        "user_id": transaction_info["user_id"],
        "created_at": transaction_info["created_at"],
    }

    return transaction


def insert_transaction(**kwargs):
    transaction = prepare_transaction_for_insertion(kwargs)
    inserted = db.transactions.insert_one(transaction)
    return inserted
