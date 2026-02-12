from app import app, db
from models import User
from werkzeug.security import generate_password_hash

with app.app_context():

    db.create_all()

    u = User(
        username="Mukesh@123",
        email="sitesphere229@gmail.com",
        password=generate_password_hash("Mukesh@924166"),
        role="superadmin"
    )

    db.session.add(u)
    db.session.commit()

print("✅ Admin Created Successfully!")