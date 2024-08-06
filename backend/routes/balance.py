from main import app
from db import Session, Balance
from schemas import BalanceData, TotalSum
from sqlalchemy import select, func

from sqlalchemy.sql.functions import sum



@app.get("/get_balances")
def get_balance(data: TotalSum):
    with Session.begin() as session:
        balances = session.scalars(select(Balance).where(Balance.owner == data.current_user)).all()
        balances = [BalanceData.model_validate(balance) for balance in balances]
        return balances


@app.get("/get_total_sum")
def get_total_sum(data: TotalSum):
    with Session.begin() as session:
        total_sum = session.scalar(select(func.sum(Balance.total)).where(Balance.owner == data.current_user))
        return total_sum



@app.post("/append_balance")
def append_balance(data: BalanceData):
    with Session.begin() as session:
        user_balance = session.scalar(select(Balance).where(Balance.owner == data.owner))
        if user_balance == None:
            user_balance = 0
            data.total_sum = user_balance + data.total
        else:
            data.total_sum = user_balance.total_sum + data.total
        if data.total_sum > data.untouchable:
            balance = Balance(**data.model_dump())
            session.add(balance)
            return balance
        else:
            return "Error"




@app.get("/balance/{balance_id}")
def get_balance(balance_id):
    with Session.begin() as session:
        balance = session.scalar(select(Balance).where(Balance.id == balance_id))
        balance = BalanceData.model_validate(balance)
        return balance