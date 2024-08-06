from .. import Base
from sqlalchemy.orm import Mapped


class Balance(Base):
    __tablename__ = "balances"

    owner: Mapped[str]
    total: Mapped[float]
    date: Mapped[str]
    theme: Mapped[str]
    untouchable: Mapped[float]