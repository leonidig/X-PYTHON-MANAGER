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
        balance = Balance(**data.model_dump())
        print(data.untouchable)
        if data.total > data.untouchable:
            return "Tran"
        else:
            session.add(balance)
            return balance



@app.get("/balance/{balance_id}")
def get_balance(balance_id):
    with Session.begin() as session:
        balance = session.scalar(select(Balance).where(Balance.id == balance_id))
        balance = BalanceData.model_validate(balance)
        return balance