from sqlalchemy import Executable, Numeric, String, select 
from sqlalchemy.orm import DeclarativeBase ,Mapped , mapped_column
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

class Base(DeclarativeBase):
    pass

class Investment(Base):
    __tablename__='investment'

    id:Mapped[int]= mapped_column(primary_key=True)
    coin:Mapped[str]=mapped_column(String(32))
    currency:Mapped[str]=mapped_column(String(3))
    amount:Mapped[float]=mapped_column(Numeric(5,2))


    def __repr__(self):
        return f"<Investment coin: {self.coin}, currence: {self.currency}, amount: {self.amount}>"


#engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)
engine = create_engine("sqlite+pysqlite:///demo.db", echo=True)

Base.metadata.create_all(engine)

bitcoin = Investment(coin="bitcoin",currency="USD",amount=2.0)
ethereum = Investment(coin="ethereum",currency="GBP",amount=10.0)
dogecoin = Investment(coin="dogecoin",currency="EUR",amount=100.0)

with Session(engine) as session:
    session.add(bitcoin)
    session.add_all([ethereum, dogecoin])
    session.commit()

#     # To get the model class back we will use Fluid API
#     stmt = select(Investment).where(Investment.coin=='bitcoin')
#     bitcoin=session.execute(stmt).scalar_one()

#     print(f"{bitcoin.coin} - {bitcoin.currency} - {bitcoin.amount}")