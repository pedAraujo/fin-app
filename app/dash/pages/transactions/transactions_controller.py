from app.mongo import db
import pandas as pd
from app import logger


from bson.objectid import ObjectId


def get_user_by_id(user_id):
    user = db.users.find_one({"_id": ObjectId(user_id)})
    return user


def update_user_balance_info(user_id, balance_info):
    try:
        updated = db.users.update_one(
            {"_id": ObjectId(user_id)},
            {"$set": {"account_balance": balance_info}},
        )
        return updated
    except Exception as e:
        logger.error(f"Error updating user balance info: {e}")
        return False


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
