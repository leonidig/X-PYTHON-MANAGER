from main import app
from db import Session, Balance
from schemas import BalanceData
from sqlalchemy import select, func
from flask_login import login_required, current_user

from sqlalchemy.sql.functions import sum

from flask import jsonify, request


@app.get("/get_total_sum")
@login_required
def get_total_sum():
    user_id = request.args.get("user_id")
    if not user_id:
        return jsonify({"error": "User ID not provided"}), 400

    with Session.begin() as session:
        stmt = select(func.sum(Balance.total)).where(Balance.owner == user_id)
        total_sum = session.execute(stmt).scalar_one_or_none()
    
    return jsonify({"total_sum": total_sum or 0})


# @app.get("/get_total_sum")
# @login_required
# def get_total_sum():
#     with Session.begin() as session:
#         total_sum = session.execute(select(func.sum(Balance.total)).where(Balance.owner == current_user.email.split('@')[0])).scalar()
#         return total_sum



@app.get("/get_balances")
def get_balance():
    with Session.begin() as session:
        balances = session.scalars(select(Balance)).all()
        balances = [BalanceData.model_validate(balance) for balance in balances]
        return balances
    

@app.post("/append_balance")
def append_balance(data: BalanceData):
    with Session.begin() as session:
        balance = Balance(**data.model_dump())
        session.add(balance)
        return balance
