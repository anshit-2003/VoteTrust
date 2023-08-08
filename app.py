# Importing required modules
import sqlite3
import os
from dotenv import load_dotenv
from blockchain import start_election, get_election_results, vote, end_election, get_candidate_ids_and_names, \
    get_election_status
from utils import send_otp,voter_login_required,admin_login_required,confirmation
from flask import Flask, render_template, url_for, request, redirect, session, jsonify, flash
from flask_session import Session
from twilio.rest import Client
from functools import wraps


# Loading Environment Variables from .env file
load_dotenv()
account_sid = os.getenv("account_sid")
auth_token = os.getenv("auth_token")
twilio_service = os.getenv("twilio-service")
admin_id = os.getenv("admin_id")
admin_password = os.getenv("admin_password")


# Database Connection
conn = sqlite3.connect('project.db', check_same_thread=False)
db = conn.cursor()

#Initialising App
app = Flask(__name__)

# Configuring Flask App
app.config["TEMPLATES_AUTO_RELOAD"] = True
admin_id = admin_id
admin_password = admin_password
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Dictionary mapping state IDs to state names
states_dict = {
    # ... State ID to State Name mappings ...
    1: "Andhra Pradesh",
    2: "Arunachal Pradesh",
    3: "Assam",
    4: "Bihar",
    5: "Chhattisgarh",
    6: "Goa",
    7: "Gujarat",
    8: "Haryana",
    9: "Himachal Pradesh",
    10: "Jharkhand",
    11: "Karnataka",
    12: "Kerala",
    13: "Madhya Pradesh",
    14: "Maharashtra",
    15: "Manipur",
    16: "Meghalaya",
    17: "Mizoram",
    18: "Nagaland",
    19: "Odisha",
    20: "Punjab",
    21: "Rajasthan",
    22: "Sikkim",
    23: "Tamil Nadu",
    24: "Telangana",
    25: "Tripura",
    26: "Uttar Pradesh",
    27: "Uttarakhand",
    28: "West Bengal",
    29: "Andaman and Nicobar Islands",
    30: "Chandigarh",
    31: "Dadra and Nagar Haveli and Daman and Diu",
    32: "Lakshadweep",
    33: "Delhi",
    34: "Puducherry",
    35: "Ladakh",
    36: "Lakshadweep",
    37: "Jammu and Kashmir"
}

# Route for the homepage
@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form.get('admin') == 'ADMIN':
            return redirect("/login_admin")
        elif request.form.get('voter') == 'VOTER':
            return redirect("/login_voter")
        else:
            return redirect("/")
    elif request.method == 'GET':
        return render_template("index.html")

# Route for voter login
@app.route("/login_voter", methods=["GET", "POST"])
def login_voter():
    session.clear()
    if request.method == "POST":

        if not request.form.get("aadhar_no"):
            return redirect("/login_voter")

        elif not request.form.get("phone_no"):
            return redirect("/login_voter")

        aadhar_no = request.form['aadhar_no']
        phone_no = request.form['phone_no']

        row = db.execute("SELECT * FROM voter WHERE aadhar_number=?", (aadhar_no,))
        print(row)
        row = list(row)
        print(row)
        print(len(row))
        if len(row) != 1 or row[0][2] != phone_no:
            return redirect("/login_voter")

        session["user_id"] = row[0][0]
        print(phone_no)

        mob_no = '+91' + phone_no
        send_otp(mob_no)
        return render_template("otp_verify.html", phone_no=mob_no)

    else:
        return render_template("login_voter.html")

# Route for OTP verification
@app.route("/verify", methods=["GET", "POST"])
def otp_verify():
    if request.method == "POST":
        otp = request.form["otp"]
        phone = request.form["mobile_no"]
        account_sid = account_sid
        auth_token = auth_token
        client = Client(account_sid, auth_token)
        verification_check = client.verify \
            .v2 \
            .services(twilio_service) \
            .verification_checks \
            .create(to=phone, code=otp)
        print(verification_check)
        if verification_check and verification_check.status == "approved":
            return redirect("/vote")
        else:
            return redirect("/login_voter")
    else:
        return redirect("/login_voter")

# Route for admin login
@app.route("/login_admin", methods=["GET", "POST"])
def login_admin():
    session.clear()
    if request.method == "POST":
        if not request.form.get("user_id"):
            return render_template("login_admin.html")

        elif not request.form.get("password"):
            return render_template("login_admin.html")

        user_id = request.form['user_id']
        password = request.form['password']

        if user_id != admin_id or password != admin_password:
            return render_template("login_admin.html")

        session["user_id"] = admin_id
        return redirect("/admin_portal")

    else:
        return render_template("login_admin.html")

# Route for admin portal
@app.route("/admin_portal", methods=["GET", "POST"])
@admin_login_required
def admin_portal():
    db.execute("SELECT state_id FROM election WHERE is_running = 1")
    curr_elections = db.fetchall()
    states = []
    for i in curr_elections:
        states.append(states_dict[i[0]])
    return render_template("admin_portal.html", states=states)

# Route to end an election
@app.route("/end_election", methods=["GET", "POST"])
@admin_login_required
def endelection():
    if request.method == "POST":
        state = request.form["state_name"]
        for key, value in states_dict.items():
            if value == state:
                state_id = key
                break
        db.execute("UPDATE election SET is_running = 0 WHERE state_id = ?", (state_id,))
        conn.commit()
        end_election()
    return redirect("/admin_portal")

# Route for voting process
@app.route('/vote', methods=["GET", "POST"])
@voter_login_required
def voter():
    candidates = db.execute("SELECT id,candidate_name FROM candidate").fetchall()
    if request.method == "POST":
        candidate_chosen = int(request.form.get("candidate_chosen"))
        print(candidate_chosen)
        query = "UPDATE voter SET is_voted = ?, candidate_id = ? WHERE id = ?"
        db.execute(query, (True, candidate_chosen, session["user_id"]))
        vote(candidate_chosen, session["user_id"])
        conn.commit()
        return redirect("/")
    else:
        return render_template("vote.html", candidates=candidates)

# Route to create a new election
@app.route('/create', methods=["GET", "POST"])
@admin_login_required
def create():
    if request.method == "POST":
        new_state_id = request.form.get("new_state_id")
        db.execute("INSERT INTO election (state_id) VALUES (?)", (new_state_id,))
        conn.commit()
        candidate_count = int(request.form.get("candidate_count"))
        eid = db.execute("SELECT id from election where state_id=?", (new_state_id,)).fetchall()
        print(eid)
        candidate_names = []
        for i in range(0, candidate_count):
            candidate_name = request.form.get(f'candidate{i}')
            candidate_names.append(candidate_name)
            db.execute("INSERT INTO candidate (candidate_name, state_id,election_id) VALUES (?, ?, ?)",
                       (candidate_name, new_state_id, eid[0][0]))
            conn.commit()
        start_election(candidate_names)
        return redirect("/admin_portal")
    else:
        return render_template("create.html")

# Route to display election results
@app.route("/results", methods=["GET"])
def results():
    if (get_election_status() == True):
        flash('Election Running!')
        return redirect("/")
    results = get_election_results()
    print(results)

    return render_template("results.html", results=results)

# Running the Flask app
if __name__ == '__main__':
    app.run(debug=True, port=5050)
