from .database import engine, Base

# just importing all the models is enough to have them created
# flake8: noqa
from .item.repos.model import Item
from .user.repos.model import User, CartItem

def create_db_schema():
    Base.metadata.create_all(bind=engine)
