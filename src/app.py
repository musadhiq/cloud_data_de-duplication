from functools import wraps
from flask import *
from flask_socketio import SocketIO, send
from src.dbconnection import *
from src.templates import *
from datetime import datetime

# bluprints
from src.admin.admin import admin
from src.leader.leader import leader
from src.member.member import member

app = Flask(__name__)


app.register_blueprint(admin, url_prefix="/admin")
app.register_blueprint(leader, url_prefix="/leader")
app.register_blueprint(member, url_prefix="/member")

app.secret_key = "anystringhere"

socketio = SocketIO(app)


# login required decorator
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "lid" not in session:
            return redirect("/")
        return f(*args, **kwargs)

    return decorated_function


@socketio.on("message")
def handle_notification(msg):
    print("received Notification: " + msg)
    send(msg, broadcast=True)
    qry = "insert into notification values (null, %s, %s)"
    val = (msg, datetime.now())
    iud(qry, val)


@app.route("/chat")
@login_required
def chat():
    return render_template("sock.html")


def messageReceived(methods=["GET", "POST"]):
    print("message was received!!!")


@socketio.on("complaint")
def handle_complaint(data):
    print("received complaint: " + data)
    socketio.emit("complaint", data, callback=messageReceived)


@app.route("/test")
def sockettest():
    return render_template("socket.html")


date = datetime.today()


@app.route("/")
def index():
    return render_template("login.html")


def set_session(id, username, email):
    session["user"] = session["user"] = {
        "id": id,
        "username": username,
        "email": email,
    }


@app.route("/login", methods=["post", "get"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    qry = "SELECT * FROM `login` WHERE `uname`=%s AND `password`=%s"
    val = (username, password)
    res = selectone(qry, val)
    if res is None:
        flash("incorrect username or password.")
        return """<script>window.location="/";</script>"""
    elif res["type"] == "admin":
        id = res["id"]
        userdata = selectall("select * from admin where id=%s", (id))
        print(userdata)
        session["user"] = id
        return """<script>alert("welcome to admin");window.location="/admin"</script>"""
    elif res["type"] == "leader":
        id = res["id"]
        userdata = selectall2("select * from leader where lid=%s", (id))
        set_session(userdata["lid"], res["uname"], userdata["email"])
        return (
            """<script>alert("welcome to leader");window.location="/leader"</script>"""
        )
    elif res["type"] == "member":
        id = res["id"]
        session["lid"] = id
        return (
            """<script>alert("welcome to member");window.location="/member"</script>"""
        )
    else:
        flash("incorrect username or password.")
        return """<script>window.location="/";</script>"""


if __name__ == "__main__":
    socketio.run(app)
