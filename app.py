from flask import Flask, render_template
from models import db, User
from flask_login import LoginManager

# ===== CREATE APP ONCE ONLY =====
app = Flask(__name__)

app.config['SECRET_KEY'] = "sitesphere-secret"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"

# ===== INIT DATABASE =====
db.init_app(app)

# ===== LOGIN SYSTEM =====
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# ===== YOUR OLD ROUTES (KEPT SAME) =====

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/services")
def services():
    return render_template("services.html")


@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route('/privacy')
def privacy():
    return render_template("privacy.html")


@app.route('/terms')
def terms():
    return render_template("terms.html")


@app.route('/disclaimer')
def disclaimer():
    return render_template("disclaimer.html")


@app.route('/about')
def about():
    return render_template("about.html")


# ===== SERVER START =====
if __name__ == "__main__":
    with app.app_context():
        db.create_all()        # auto create database

    app.run(debug=True)