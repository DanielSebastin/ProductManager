# 📦 Product Manager

A simple and efficient **Product Management System** to create, manage, and organize products.  
Built using **Python, SQLAlchemy, and AWS RDS (PostgreSQL)**.

---

## 🚀 Features

- ➕ Add new products  
- 📋 View all products  
- ✏️ Update product details  
- ❌ Delete products  
- ☁️ Cloud database with AWS RDS (PostgreSQL)  
- ⚡ Fast ORM using SQLAlchemy  
- 🔒 Secure SSL database connection  

---

## 🛠️ Tech Stack

**Backend**
- Python
- SQLAlchemy

**Database**
- AWS RDS (PostgreSQL)

---

## 🗄️ Database Configuration

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_url = "postgresql://username:password@rdsproj.cnwcewm0mb3c.ap-south-1.rds.amazonaws.com:5432/postgres?sslmode=require"

engine = create_engine(db_url, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)



