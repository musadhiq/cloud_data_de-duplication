from functools import wraps
from flask import *
from flask_socketio import *
from src.dbconnection import *
from templates import *
from datetime import datetime

# bluprints
from admin.admin import admin
from leader.leader import leader
from member.member import member

app = Flask(__name__)


app.register_blueprint(admin, url_prefix="/admin")
app.register_blueprint(leader, url_prefix="/leader")
app.register_blueprint(member, url_prefix="/member")

app.secret_key = "anystringhere"

socketio = SocketIO(app)

# login


date = datetime.today()


@app.route("/")
def index():
    return render_template("login.html")


def set_session(id, username, email):
    session["user"] = {
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
        id = res["userid"]
        # userdata = selectall2("select * from login where userid=%s", (id))
        session["userid"] = id
        return """<script>alert("welcome to admin");window.location="/admin"</script>"""
    elif res["type"] == "leader":
        id = res["userid"]
        # userdata = selectall2("select * from login where userid=%s", (id))
        session["userid"] = id
        return (
            """<script>alert("welcome to leader");window.location="/leader"</script>"""
        )
    elif res["type"] == "member":
        id = res["id"]
        session["userid"] = id
        return (
            """<script>alert("welcome to member");window.location="/member"</script>"""
        )
    else:
        flash("incorrect username or password.")
        return """<script>window.location="/";</script>"""


# login required decorator
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "lid" not in session:
            return redirect("/")
        return f(*args, **kwargs)

    return decorated_function


@socketio.on("notification")
def handle_notification(data):
    print("received Notification: " + data)
    emit("notification", data, broadcast=True)
    qry = "insert into notification values (null, %s, %s)"
    val = (data, datetime.now())
    iud(qry, val)


# chatroom
@socketio.on("join_room")
def handle_join_room(data):
    print("{} has joined the room {}".format(data["name"], data["room"]))
    join_room(1001)
    socketio.emit("join_alert", data)


@socketio.on("send_message")
def handle_send_message(data):
    print(
        "{} has send message the room {} : {}".format(
            data["name"], data["room"], data["message"]
        )
    )
    emit("receive_message", data, room=1001)


if __name__ == "__main__":
    socketio.run(app, allow_unsafe_werkzeug=True, debug=True)
