from fastapi import FastAPI
from db import Balance, Session
from sqlalchemy import select


app = FastAPI()



@app.get("/get_balances")
def get_balance():
    with Session.begin() as session:
        balance = Balance(owner="Leonid", total=1298.7)
        session.add(balance)
        balances = session.scalars(select(Balance)).all()
        return [{
            "id": balance.id,
            "owner": balance.owner,
            "total": balance.total
        } for balance in balances]