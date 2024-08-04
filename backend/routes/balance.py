from main import app
from db import Session, Balance

from sqlalchemy import select



@app.get("/get_balances")
def get_balance():
    with Session.begin() as session:
        balance1 = Balance(owner="Leonid", total=1298.7)
        balance2 = Balance(owner="John", total=457.2)
        balance3 = Balance(owner="Patric", total=711)
        balance4 = Balance(owner="Json", total=123)
        balance5 = Balance(owner="Mary", total=417.9)
        session.add(balance1)
        session.add(balance2)
        session.add(balance3)
        session.add(balance4)
        session.add(balance5)

        balances = session.scalars(select(Balance)).all()

        return [{
            "id": balance.id,
            "owner": balance.owner,
            "total": balance.total
        } for balance in balances]