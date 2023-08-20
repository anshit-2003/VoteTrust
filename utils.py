from functools import wraps
from twilio.rest import Client
from flask import session, render_template, redirect
import os

admin_id = os.getenv("admin_id")
account_sid = os.getenv("account_sid")
auth_token = os.getenv("auth_token")
twilio_service = os.getenv("twilio_service")
admin_password = os.getenv("admin_password")

# Function to send OTP using Twilio
def send_otp(mob_no):
    client = Client(account_sid, auth_token)

    verification = client.verify \
        .v2 \
        .services(twilio_service) \
        .verifications \
        .create(to=mob_no, channel='sms')
    return verification
# Decorator function for voter login required
def voter_login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return render_template("index.html")
        return f(*args, **kwargs)

    return decorated_function

# Decorator function for admin login required
def admin_login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") != admin_id:
            return redirect("/")
        return f(*args, **kwargs)

    return decorated_function

# Function to send confirmation message
def confirmation(phone):
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="This Message is sent to confirm your Vote on VoteTrust. Thanks For Voting.",
        from_= os.getenv('twilio_phone'),
        to=phone
    )
