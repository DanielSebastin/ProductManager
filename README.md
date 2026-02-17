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
⚠️ Never expose real database credentials in public repositories. Use environment variables instead.

⚙️ Installation & Setup
1. Clone the repository
bash
Copy code
git clone https://github.com/DanielSebastin/ProductManager.git
cd ProductManager
2. Create virtual environment
bash
Copy code
python -m venv venv
Activate (Windows)

bash
Copy code
venv\Scripts\activate
Activate (Linux / Mac)

bash
Copy code
source venv/bin/activate
3. Install dependencies
bash
Copy code
pip install -r requirements.txt
4. Configure Environment Variables
Create a .env file:

env
Copy code
DB_USER=your_username
DB_PASS=your_password
DB_HOST=rdsproj.cnwcewm0mb3c.ap-south-1.rds.amazonaws.com
DB_PORT=5432
DB_NAME=postgres
5. Run the project
bash
Copy code
python app.py
📂 Project Structure
text
Copy code
ProductManager/
│── backend/
│   ├── database.py
│   ├── models.py
│   ├── crud.py
│   └── app.py
│
│── frontend/ (optional)
│── requirements.txt
│── README.md
🔐 Security Notes
SSL enabled (sslmode=require)

Do NOT commit .env

Restrict RDS Security Group to trusted IPs

Rotate DB credentials regularly

🎯 Purpose
Learn AWS RDS (Cloud DB)

Practice SQLAlchemy ORM

Build real-world CRUD system

🔮 Future Improvements
Authentication (Login / Signup)

Role-based access

Product image upload

REST API / FastAPI

Docker deployment

AWS EC2 hosting

📜 License
MIT License
