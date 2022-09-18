from flask import *
from src.dbconnection import *
from src.templates import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/login_1', methods=['post', 'get'])
def login_1():
    username = request.form['textfield']
    password = request.form['textfield2']
    qry = "SELECT * FROM `login` WHERE `uname`=%s AND `password`=%s"
    val = (username, password)
    res = selectone(qry, val)
    if res is None:
        return '''<script>alert("invalid"); window.location="/"</script>'''
    elif res['type'] == 'admin':
        return '''<script>alert("welcome to admin");window.location="/admin_home"</script>'''
    elif res['type'] == 'leader':
        return '''<script>alert("welcome to leader");window.location="/leader"</script>'''
    elif res['type'] == 'member':
        return '''<script>alert("welcome to member");window.location="/member"</script>'''
    else:
        return '''<script>alert("invalid data");window.location="/"</script>'''


@app.route('/admin_home')
def admin_home():
    return render_template("admin_home.html")


@app.route('/manage_leaders')
def manage_leaders():
    return render_template("manage_leaders.html")


@app.route('/add_leader')
def add_leader():
    return render_template("add_leader.html")


@app.route('/edit_leader')
def edit_leader():
    return render_template("edit_leader.html")


@app.route('/complaint')
def complaint():
    return render_template("complaint.html")


@app.route('/complaint_reply')
def complaint_reply():
    return render_template("complaint_reply.html")


# Leader

@app.route('/leader')
def leader():
    return render_template("/leader_home.html")


@app.route('/leader_works')
def leader_works():
    return render_template("/works.html")


@app.route('/manage_members')
def manage_members():
    return render_template("/manage_members.html")


@app.route('/add_member')
def add_member():
    return render_template("/add_member.html")


@app.route('/edit_member')
def edit_member():
    return render_template("/edit_member.html")


@app.route('/feedback')
def feedback():
    return render_template("/feedback.html")


@app.route('/doubt')
def doubt():
    return render_template("doubt.html")


@app.route('/doubt_reply')
def doubt_reply():
    return render_template("/doubt_reply.html")


@app.route('/send_notification')
def send_notification():
    return render_template("/send_notification.html")


# member


@app.route('/member')
def member():
    return render_template("/member_home.html")


@app.route('/member_work')
def member_work():
    return render_template("/member_work.html")


@app.route('/notifications')
def notifications():
    return render_template("/notification.html")


@app.route('/send_feedback')
def send_feedback():
    return render_template("/send_feedback.html")


@app.route('/ask_doubt')
def ask_doubt():
    return render_template("/ask_doubt.html")


@app.route('/post_complaint')
def post_complaint():
    return render_template("/post_complaint.html")


app.run(debug=True)
