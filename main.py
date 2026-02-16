from fastapi import FastAPI,Depends
from models import Products
from database import session,engine
import database_models
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware


database_models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.add_middleware( CORSMiddleware,allow_origins=["http://localhost:3000"],allow_methods=["*"])




p= [Products(id=1,name="Phone",description="Used for calls and entertainment",price=299.99,quantity=5),
Products(id=2,name="Laptop",description="Used for professional work",price=1999.99,quantity=10),
Products(id=3,name="Dumbbells",description="Used for workouts",price=49.99,quantity=11),
Products(id=4,name="Potions",description="Used for gaining strength",price=999.99,quantity=12),
Products(id=5,name="Sunglasses",description="Used to cool your eyes from the sun",price=5.99,quantity=10)
    ]

def get_db():
    db=session()
    try:
        yield db
    finally:
        db.close()


def init_db():
    db=session()
    count=db.query(database_models.Products).count()
    if count==0:
        for product in p:
            db.add(database_models.Products(**product.model_dump()))
    db.commit() 
    db.close()
    
init_db()


@app.get("/products")
def get_all_products(db:Session = Depends(get_db)):
    db_products=db.query(database_models.Products).all()
    return db_products

@app.get("/products/{id}")
def get_product_by_id(id:int,db:Session=Depends(get_db)):
    db_products=db.query(database_models.Products).filter(database_models.Products.id==id).first()
    if db_products:
        return db_products
    return "No such product found"    

@app.post("/products")
def add_product(product:Products,db:Session=Depends(get_db)):
    db.add(database_models.Products(**product.model_dump()))
    db.commit()
    db_product=db.query(database_models.Products).all()
    return db_product

@app.put("/products/{id}")
def update_product(id:int,product:Products,db:Session=Depends(get_db)):
    db_products=db.query(database_models.Products).filter(database_models.Products.id==id).first()
    if db_products:
        db_products.name=product.name
        db_products.description=product.description
        db_products.price=product.price
        db_products.quantity=product.quantity
        db.commit()
        return "Product updated"
    else:
        return "Product Not Found"
        
@app.delete("/products/{id}")
def delete_product(id:int,db:Session=Depends(get_db)):
    db_product=db.query(database_models.Products).filter(database_models.Products.id==id).first()
    if(db_product):
        db.delete(db_product)
        db.commit()
    else:
        return "Product not removed"
