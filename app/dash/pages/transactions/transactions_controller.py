from datetime import datetime
from app.mongo import db


def get_transactions_by_user(user_id):
    transactions = db.transactions.find({"user_id": user_id})
    return transactions


def prepare_transaction_for_insertion(
    date,
    transaction_type,
    name,
    category,
    value,
    frequency,
    description,
    user_id,
):
    transaction = {
        "date": datetime.strptime(date, "%Y-%m-%d"),
        "type": "income" if transaction_type else "expense",
        "name": name,
        "category": category,
        "value": value,
        "frequency": frequency,
        "description": description,
        "user_id": user_id,
    }

    return transaction


def insert_transaction(transaction):
    try:
        db.transactions.insert_one(transaction)
    except Exception as error:
        print(error)
        return False
    return True
