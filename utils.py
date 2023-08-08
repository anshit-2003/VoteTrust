# Function to send OTP using Twilio
def send_otp(mob_no):
    account_sid = account_sid
    auth_token = auth_token
    client = Client(account_sid, auth_token)

    verification = client.verify \
        .v2 \
        .services(twilio_service) \
        .verifications \
        .create(to=mob_no, channel='sms')

    print(verification.status)

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
    account_sid = account_sid
    auth_token = auth_token
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="This Message is sent to confirm your Vote on VoteTrust. Thanks For Voting.",
        from_= os.getenv('twilio_phone'),
        to=phone
    )
