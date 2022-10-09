from tkinter import CURRENT
from click import echo
from flask import *
from src.dbconnection import *
from src.templates import *
from datetime import datetime

app = Flask(__name__)
app.secret_key = "anystringhere"

date = datetime.today()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['post', 'get'])
def login():
    username = request.form['username']
    password = request.form['password']
    qry = "SELECT * FROM `login` WHERE `uname`=%s AND `password`=%s"
    val = (username, password)
    res = selectone(qry, val)
    if res is None:
        flash("incorrect username or password.")
        return '''<script>window.location="/";</script>'''
    elif res['type'] == 'admin':
        id = res['id']
        session['lid'] = id
        return '''<script>alert("welcome to admin");window.location="/admin"</script>'''
    elif res['type'] == 'leader':
        id = res['id']
        session['lid'] = id
        return '''<script>alert("welcome to leader");window.location="/leader"</script>'''
    elif res['type'] == 'member':
        return '''<script>alert("welcome to member");window.location="/member"</script>'''
    else:
        flash("incorrect username or password.")
        return '''<script>window.location="/";</script>'''


@app.route('/admin')
def admin_home():
    works = selectall("SELECT * FROM `works`")
    return render_template("/admin/admin_home.html", works=works)


@app.route('/manage_leaders')
def manage_leaders():
    data = selectall("SELECT id,Fname,Lname,Email FROM `leader`")
    return render_template("/admin/manage_leaders.html", data=data)


@app.route('/leaders/new')
def add_leader():
    return render_template("/admin/add_leader.html")


@app.route('/leaders/new1', methods=['post'])
def add_leader1():
    Fname = request.form['firstname']
    Lname = request.form['lastname']
    Gender = request.form['gender']
    Place = request.form['place']
    Pin = request.form['pin']
    Post = request.form['post']
    Email = request.form['email']
    Phone = request.form['phone']
    Username = request.form['username']
    password = request.form['password']
    qry = "insert into login values(Null,%s,%s,'leader')"
    val = (Username, password)
    id = iud(qry, val)
    qry1 = "insert  into leader values (Null,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val1 = (str(id), Fname, Lname, Gender, Place, Pin, Post, Email, Phone)
    iud(qry1, val1)
    return '''<script>alert("added");window.location="/manage_leaders"</script>'''


@app.route('/leaders/edit')
def edit_leader():
    id = request.args.get('id')
    session['id'] = id
    qry = "SELECT * FROM `leader` WHERE `id`=%s"
    val = (id)
    res = selectone(qry, val)
    return render_template("/admin/edit_leader.html", data=res)


@app.route('/leaders/delete')
def delete_leader():
    id = request.args.get('id')
    qry = "DELETE FROM `leader` WHERE `id`=%s"
    iud(qry, id)
    return '''<script>alert("deleted");window.location="/manage_leaders"</script>'''


@app.route('/add_work')
def add_work():
    return render_template("/admin/add_works.html")


@app.route('/add_work1', methods=['post'])
def add_work1():
    title = request.form['title']
    description = request.form['description']
    qry = "insert into works values(Null,%s,%s,%s,Null)"

    val = (title, description, date)
    iud(qry, val)
    return '''<script>alert("added");window.location="/admin"</script>'''


@app.route('/work/delete')
def delete_work():
    id = request.args.get('id')
    qry = "DELETE FROM `works` WHERE `workid`=%s"
    iud(qry, id)
    return '''<script>alert("deleted");window.location="/admin"</script>'''


@app.route('/admin/assign_works')
def assign_works():
    works = selectall("SELECT * FROM `works`")
    leaders = selectall("SELECT lid,Fname,Lname FROM `leader`")
    assign = selectall("SELECT * FROM `assign_to_leader`")
    filtered_works = list(filter(lambda x: x['workid'] not in [
        y['wid'] for y in assign], works))

    assignedstatus = selectall(
        "SELECT leader.lid, leader.fname, leader.lname ,works.workid, works.workname, works.status from leader JOIN assign_to_leader on assign_to_leader.lid = leader.lid JOIN works ON assign_to_leader.wid = works.workid")

    return render_template("/admin/assign_work.html", works=filtered_works, leaders=leaders, assigned=assignedstatus)


@app.route("/admin/assign_works1", methods=['post'])
def assign_works1():
    workid = request.form['workid']
    leaderid = request.form['leaderid']
    qry = "insert into assign_to_leader values(Null,%s,%s,%s,'pending')"
    val = (leaderid, workid, date)
    iud(qry, val)
    return '''<script>alert("assigned");window.location="/admin"</script>'''


@app.route('/complaint')
def complaint():
    return render_template("/admin/complaint.html")


@app.route('/complaint_reply')
def complaint_reply():
    return render_template("/admin/complaint_reply.html")


# Leader

@app.route('/leader')
def leader():
    return render_template("/leader/leader_home.html")


@app.route('/leader/edit_profile')
def edit_profile():
    id = session['lid']
    print(id)
    qry = "SELECT * FROM `leader` WHERE `lid`=%s"
    val = (id)
    res = selectone(qry, val)
    return render_template("/leader/edit_profile.html", data=res)


@app.route('/leader/update', methods=['post'])
def update_leader():
    Lid = request.form['lid']
    Fname = request.form['firstname']
    Lname = request.form['lastname']
    Gender = request.form['gender']
    Place = request.form['place']
    Pin = request.form['pin']
    Post = request.form['post']
    Email = request.form['email']
    Phone = request.form['phone']
    qry = "update leader set Fname=%s,Lname=%s,Gender=%s,Place=%s,Pin=%s,Post=%s,Email=%s,Phone=%s where id=%s"
    val = (Fname, Lname, Gender, Place, Pin, Post, Email, Phone, Lid)
    iud(qry, val)
    return '''<script>alert("success");window.location="/leader"</script>'''


@app.route('/leader/manage_members')
def manage_members():
    data = selectall("SELECT lid,Fname,Lname,Email FROM `member`")
    return render_template("/leader/manage_members.html", data=data)


@app.route('/leader/add_member')
def add_member():
    return render_template("/leader/add_member.html")


@app.route('/leader/add_member1', methods=['post'])
def add_member1():
    Fname = request.form['firstname']
    Lname = request.form['lastname']
    Gender = request.form['gender']
    Place = request.form['place']
    Pin = request.form['pin']
    Post = request.form['post']
    Email = request.form['email']
    Phone = request.form['phone']
    Username = request.form['username']
    password = request.form['password']
    qry = "insert into login values(Null,%s,%s,'member')"
    val = (Username, password)
    id = iud(qry, val)
    qry1 = "insert  into member values (Null,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val1 = (str(id), Fname, Lname, Gender, Place, Pin, Post, Email, Phone)
    iud(qry1, val1)
    return '''<script>alert("added");window.location="/leader/manage_members"</script>'''


@app.route('/leader/edit_member')
def edit_member():
    id = request.args.get('id')
    session['id'] = id
    qry = "SELECT * FROM `member` WHERE `lid`=%s"
    val = (id)
    res = selectone(qry, val)
    print(res)
    return render_template("/leader/edit_member.html", data=res)


@app.route('/leader/edit_member1', methods=['post'])
def edit_member1():
    Lid = request.form['lid']
    Fname = request.form['firstname']
    Lname = request.form['lastname']
    Gender = request.form['gender']
    Place = request.form['place']
    Pin = request.form['pin']
    Post = request.form['post']
    Email = request.form['email']
    Phone = request.form['phone']
    qry = "update member set fname=%s,lname=%s,gender=%s,place=%s,pin=%s,post=%s,email=%s,phone=%s where lid=%s"
    val = (Fname, Lname, Gender, Place, Pin, Post, Email, Phone, Lid)
    print(Lid)
    iud(qry, val)
    return '''<script>alert("success");window.location="/leader/manage_members"</script>'''


@app.route('/leader/assign_works')
def leader_works():
    id = session['lid']
    val = (id)
    qry = "SELECT * FROM works WHERE `workid` IN (SELECT wid FROM `assign_to_leader` WHERE `lid`=%s)"
    works = selectall2(qry, val)
    members = selectall("SELECT * FROM `member`")
    assign = selectall("SELECT * FROM `assign_to_member`")
    filtered_works = list(filter(lambda x: x['workid'] not in [
        y['wid'] for y in assign], works))
    assignedstatus = selectall(
        "SELECT member.lid, member.fname, member.lname ,works.workid, works.workname, works.status from member JOIN assign_to_member on assign_to_member.lid = member.lid JOIN works ON assign_to_member.wid = works.workid")

    return render_template("/leader/assign_works.html", works=filtered_works, members=members, assigned=assignedstatus)


@app.route('/leader/assign_works1', methods=['post'])
def assign_to_mem():
    workid = request.form['workid']
    memberid = request.form['memberid']
    qry = "insert into assign_to_member values(Null,%s,%s,%s,'pending')"
    val = (memberid, workid, date)
    iud(qry, val)
    return '''<script>alert("assigned");window.location="/leader"</script>'''


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
    return render_template("/member/member_home.html")


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
