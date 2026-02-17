📦 Product Manager

A simple and efficient Product Management System that allows users to create, manage, and organize products.
This project demonstrates full-stack development using PostgreSQL (AWS RDS) and SQLAlchemy ORM.

🚀 Features

➕ Add new products

📋 View all products

✏️ Update product details

❌ Delete products

☁️ Cloud database using AWS RDS (PostgreSQL)

⚡ Fast database access using SQLAlchemy ORM

🔒 Secure SSL database connection

🛠️ Tech Stack

Backend

Python

SQLAlchemy

PostgreSQL

Database

AWS RDS (PostgreSQL)

Other

SSL enabled DB connection

Connection pooling (pool_pre_ping=True)

🗄️ Database Configuration

The project connects to AWS RDS PostgreSQL using SQLAlchemy.

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_url="postgresql://username:password@rdsproj.cnwcewm0mb3c.ap-south-1.rds.amazonaws.com:5432/postgres?sslmode=require"

engine=create_engine(db_url,pool_pre_ping=True)
session=sessionmaker(autocommit=False,autoflush=False,bind=engine)


⚠️ Important: Never expose your real database username/password in public repositories.
Use environment variables instead.

⚙️ Installation & Setup
1. Clone the repository
git clone https://github.com/DanielSebastin/ProductManager.git
cd ProductManager

2. Create virtual environment
python -m venv venv
source venv/bin/activate     # Linux / Mac
venv\Scripts\activate        # Windows

3. Install dependencies
pip install -r requirements.txt

4. Configure Environment Variables (Recommended)

Create .env

DB_USER=your_username
DB_PASS=your_password
DB_HOST=rdsproj.cnwcewm0mb3c.ap-south-1.rds.amazonaws.com
DB_PORT=5432
DB_NAME=postgres

5. Run the project
python app.py

📂 Project Structure
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

SSL connection enabled (sslmode=require)

Avoid committing .env file

Use IAM / Security Groups to restrict DB access

Rotate DB credentials regularly

🎯 Purpose of the Project

This project was built to:

Learn Cloud Database (AWS RDS)

Practice SQLAlchemy ORM

Implement real-world CRUD system

Understand database connection pooling

🔮 Future Improvements

Authentication (Login / Signup)

Role-based access (Admin / User)

Product image upload

REST API / FastAPI integration

Docker deployment

AWS EC2 hosting

🤝 Contributing

Pull requests are welcome. Open an issue first to discuss major changes.

📜 License

MIT License
