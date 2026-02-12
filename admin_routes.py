from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user
from models import db, User
from werkzeug.security import generate_password_hash, check_password_hash

def register_admin(app):

    @app.route('/admin')
    def admin_login():
        return render_template("admin_login.html")

    @app.route('/admin/login', methods=['POST'])
    def admin_do_login():

        email = request.form['email']
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(email=email, username=username).first()

        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect("/admin/dashboard")

        return "Invalid Credentials"

    @app.route('/admin/dashboard')
    @login_required
    def dashboard():
        return render_template("admin_dashboard.html", user=current_user)

    # ONLY SUPERADMIN CAN CREATE USERS
    @app.route('/admin/create-user', methods=['POST'])
    @login_required
    def create_user():

        if current_user.role != "superadmin":
            return "Not Allowed"

        u = User(
            username=request.form['username'],
            email=request.form['email'],
            password=generate_password_hash(request.form['password']),
            role=request.form['role']
        )

        db.session.add(u)
        db.session.commit()

        return "User Created"