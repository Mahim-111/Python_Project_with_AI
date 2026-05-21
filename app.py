from flask import Flask, render_template, request, redirect, session, flash
from werkzeug.security import generate_password_hash, check_password_hash

from db import SessionLocal
from ai import analyze_resume

import models
import json
import PyPDF2
import docx
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")


@app.route("/")
def home():
    if "user_id" in session:
        return redirect("/dashboard")
    return redirect("/login")


# ---------------- SIGNUP ---------------- #

@app.route("/signup", methods=["GET", "POST"])
def signup():

    db = SessionLocal()

    if request.method == "POST":

        email = request.form.get("email")
        password = request.form.get("password")

        if len(password) < 6:
            flash("Password must be at least 6 characters.")
            return redirect("/signup")

        existing_user = db.query(models.User).filter_by(email=email).first()

        if existing_user:
            flash("Email already exists.")
            return redirect("/signup")

        hashed_password = generate_password_hash(password)

        new_user = models.User(
            email=email,
            password=hashed_password
        )

        db.add(new_user)
        db.commit()

        flash("Account created successfully.")
        return redirect("/login")

    return render_template("signup.html")


# ---------------- LOGIN ---------------- #

@app.route("/login", methods=["GET", "POST"])
def login():

    db = SessionLocal()

    if request.method == "POST":

        email = request.form.get("email")
        password = request.form.get("password")

        user = db.query(models.User).filter_by(email=email).first()

        if not user:
            flash("User not found.")
            return redirect("/login")

        if not check_password_hash(user.password, password):
            flash("Incorrect password.")
            return redirect("/login")

        session["user_id"] = user.id
        session["user_email"] = user.email

        return redirect("/dashboard")

    return render_template("login.html")


# ---------------- DASHBOARD ---------------- #

@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():

    if "user_id" not in session:
        return redirect("/login")

    db = SessionLocal()

    user = db.query(models.User).filter_by(
        id=session["user_id"]
    ).first()

    result = None

    if request.method == "POST":

        user_goal = request.form.get("role")
        resume_text = request.form.get("resume")

        file = request.files.get("file")

        if file and file.filename != "":

            # PDF
            if file.filename.endswith(".pdf"):

                try:
                    pdf_reader = PyPDF2.PdfReader(file)

                    text = ""

                    for page in pdf_reader.pages:
                        text += page.extract_text() or ""

                    resume_text = text

                except Exception:
                    flash("Failed to read PDF file.")
                    return redirect("/dashboard")

            # DOCX
            elif file.filename.endswith(".docx"):

                try:
                    doc = docx.Document(file)

                    text = ""

                    for para in doc.paragraphs:
                        text += para.text + "\n"

                    resume_text = text

                except Exception:
                    flash("Failed to read DOCX file.")
                    return redirect("/dashboard")

        if not resume_text:
            flash("Please upload or paste a resume.")
            return redirect("/dashboard")

        result = analyze_resume(resume_text, user_goal)

        report = models.Report(
            user_id=user.id,
            resume_text=resume_text,
            result=json.dumps(result)
        )

        db.add(report)
        db.commit()

    return render_template(
        "dashboard.html",
        user=user,
        result=result
    )


# ---------------- HISTORY ---------------- #

@app.route("/history")
def history():

    if "user_id" not in session:
        return redirect("/login")

    db = SessionLocal()

    reports = db.query(models.Report).filter_by(
        user_id=session["user_id"]
    ).all()

    parsed_reports = []

    for r in reports:

        try:
            parsed_result = json.loads(r.result)

        except Exception:
            parsed_result = {"error": "Invalid result"}

        parsed_reports.append({
            "resume_text": r.resume_text,
            "result": parsed_result
        })

    return render_template(
        "history.html",
        reports=parsed_reports
    )


# ---------------- LOGOUT ---------------- #

@app.route("/logout")
def logout():

    session.clear()

    return redirect("/login")


if __name__ == "__main__":
    app.run(debug=True)