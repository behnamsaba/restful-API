from models import db, connect_db, Cupcake
from app import app

db.drop_all()
db.create_all()

cupcakes = [
    Cupcake(flavor="chocolate",size="large",rating=4.7),
    Cupcake(flavor="french vanilla",size="small",rating=4.4,image="https://cdn.cupcakeproject.com/wp-content/uploads/2011/09/Best-Vanilla-Cupcakes-04.jpg"),
    Cupcake(flavor="strawberry",size="medium",rating=3.9,image="https://preppykitchen.com/wp-content/uploads/2022/07/Strawberry-Cupcakes-Feature.jpg")
]


db.session.add_all(cupcakes)
db.session.commit()
