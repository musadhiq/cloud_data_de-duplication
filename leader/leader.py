from flask import *
from src.dbconnection import *
from datetime import datetime

leader = Blueprint("leader", __name__, template_folder="templates")

date = datetime.now()


@leader.route("/")
def leader_home():
    return render_template("l_index.html")


@leader.route("/edit_profile")
def edit_profile():
    id = session["userid"]
    print(id)
    qry = "SELECT * FROM `user` WHERE `userid`=%s"
    val = id
    res = selectone(qry, val)
    return render_template("edit_profile.html", data=res)


@leader.route("/update", methods=["post"])
def update_leader():
    id = session["userid"]
    name = request.form["name"]
    gender = request.form["gender"]
    place = request.form["place"]
    pin = request.form["pin"]
    post = request.form["post"]
    email = request.form["email"]
    phone = request.form["phone"]
    address = request.form["address"]

    qry = "update user set name=%s,gender=%s,place=%s,pin=%s,post=%s,email=%s,phone=%s,address=%s where userid=%s"
    val = (name, gender, place, pin, post, email, phone, address, id)
    iud(qry, val)
    return """<script>alert("success");window.location="/leader"</script>"""


@leader.route("/manage_members")
def manage_members():
    data = selectall(
        "SELECT user.userid,user.name,user.email ,login.userid FROM `user` JOIN login on login.type = `member`"
    )
    return render_template("manage_members.html", data=data)


@leader.route("/add_member")
def add_member():
    return render_template("add_member.html")


@leader.route("/add_member1", methods=["post"])
def add_member1():
    Fname = request.form["firstname"]
    Lname = request.form["lastname"]
    Gender = request.form["gender"]
    Place = request.form["place"]
    Pin = request.form["pin"]
    Post = request.form["post"]
    Email = request.form["email"]
    Phone = request.form["phone"]
    Username = request.form["username"]
    password = request.form["password"]
    qry = "insert into login values(Null,%s,%s,'member')"
    val = (Username, password)
    id = iud(qry, val)
    qry1 = "insert  into member values (Null,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val1 = (str(id), Fname, Lname, Gender, Place, Pin, Post, Email, Phone)
    iud(qry1, val1)
    return (
        """<script>alert("added");window.location="/leader/manage_members"</script>"""
    )


@leader.route("/edit_member")
def edit_member():
    id = request.args.get("id")
    session["id"] = id
    qry = "SELECT * FROM `member` WHERE `lid`=%s"
    val = id
    res = selectone(qry, val)
    print(res)
    return render_template("edit_member.html", data=res)


@leader.route("/edit_member1", methods=["post"])
def edit_member1():
    Lid = request.form["lid"]
    Fname = request.form["firstname"]
    Lname = request.form["lastname"]
    Gender = request.form["gender"]
    Place = request.form["place"]
    Pin = request.form["pin"]
    Post = request.form["post"]
    Email = request.form["email"]
    Phone = request.form["phone"]
    qry = "update member set fname=%s,lname=%s,gender=%s,place=%s,pin=%s,post=%s,email=%s,phone=%s where lid=%s"
    val = (Fname, Lname, Gender, Place, Pin, Post, Email, Phone, Lid)
    print(Lid)
    iud(qry, val)
    return (
        """<script>alert("success");window.location="/leader/manage_members"</script>"""
    )

# works

@leader.route("/get_works")
def get_works():
    return render_template("get_works.html")



@leader.route("/assign_works")
def leader_works():
    id = session["lid"]
    val = id
    qry = "SELECT * FROM works WHERE `workid` IN (SELECT wid FROM `assign_to_leader` WHERE `lid`=%s)"
    works = selectall2(qry, val)
    members = selectall("SELECT * FROM `member`")
    assign = selectall("SELECT * FROM `assign_to_member`")
    filtered_works = list(
        filter(lambda x: x["workid"] not in [y["wid"] for y in assign], works)
    )
    assignedstatus = selectall(
        "SELECT member.lid, member.fname, member.lname ,works.workid, works.workname, works.status from member JOIN assign_to_member on assign_to_member.lid = member.lid JOIN works ON assign_to_member.wid = works.workid"
    )
    return render_template(
        "assign_works.html",
        works=filtered_works,
        members=members,
        assigned=assignedstatus,
    )


@leader.route("/assign_works1", methods=["post"])
def assign_to_mem():
    workid = request.form["workid"]
    memberid = request.form["memberid"]
    qry = "insert into assign_to_member values(Null,%s,%s,%s,'pending')"
    val = (memberid, workid, date)
    iud(qry, val)
    return """<script>alert("assigned");window.location="/leader"</script>"""


@leader.route("/view_team")
def view_team():
    return render_template("view_team.html")


@leader.route("/view_feedbacks")
def feedback():
    feedbacks = selectall("select * from feedback")
    print(feedbacks)
    return render_template("view_feedbacks.html")


@leader.route("/doubt")
def doubt():
    return render_template("doubt.html")


@leader.route("/doubt_reply")
def doubt_reply():
    return render_template("doubt_reply.html")


@leader.route("/send_notification")
def send_notification():
    return render_template("send_notification.html")


@leader.route("/discord")
def l_chatroom():
    return render_template("l_chatroom.html")
