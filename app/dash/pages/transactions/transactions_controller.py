from app.mongo import db


def get_transactions_by_user(user_id):
    transactions = db.transactions.find({"user_id": user_id})

    return transactions
