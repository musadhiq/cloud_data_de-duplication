from datetime import datetime
from flask import *
from src.dbconnection import *

admin = Blueprint("admin", __name__, template_folder="templates")

date = datetime.now()


@admin.route("/")
def admin_home():
    # works = selectall("SELECT * FROM `works`")
    return render_template("a_index.html")


# user management


@admin.route("/manage_users")
def manage_users():
    data = selectall("select login.userid, login.type, user.name, user.email from login  join user where user.userid = login.userid;")
    return render_template("manage_users.html" ,users=data)


@admin.route("/manage_users/new_user")
def new_user():
    return render_template("add_user.html")


@admin.route("/add_user", methods=["post"])
def add_user():
    username = request.form["username"]
    name = request.form["name"]
    email = request.form["email"]
    phone = request.form["phone"]
    pin = request.form["pin"]
    post = request.form["post"]
    address = request.form["address"]
    gender = request.form["gender"]
    place = request.form["place"]
    password = request.form["password"]
    role = request.form['role']
    qry = "insert into login values(Null,%s,%s,%s)"
    val = (username, password,role)
    id = iud(qry, val)
    qry1 = "insert  into user values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val1 = (id, name, email, address, post, pin, phone, place, gender)
    iud(qry1, val1)
    return """<script>alert("added");window.location="/admin/manage_users"</script>"""


@admin.route("/manage_users/edit_user")
def edit_user():
    id = request.args.get("id")
    qry = "SELECT * FROM `user` WHERE `userid`=%s"
    res = selectone(qry, id)
    return render_template("edit_user.html", user=res)


@admin.route("/edit_user", methods=["post"])
def update_user():
    id = request.args.get("id")
    name = request.form["name"]
    email = request.form["email"]
    phone = request.form["phone"]
    pin = request.form["pin"]
    post = request.form["post"]
    address = request.form["address"]
    gender = request.form["gender"]
    place = request.form["place"]
    qry1 = "update user  set name=%s, email=%s, address=%s, post=%s, pin=%s, phone=%s, place=%s,gender=%s where userid=%s"
    val1 = (name, email, address, post, pin, phone, place, gender,id)
    iud(qry1, val1)
    return """<script>alert("Success");window.location="/admin/manage_users"</script>"""


@admin.route("/manage_users/delete_user")
def delete_user():
    id = request.args.get("id")
    qry = "delete user, login from user inner join login on user.userid = login.userid where login.userid = %s"
    iud(qry, id)
    return (
        """<script>alert("deleted");window.location="/admin/manage_users"</script>"""
    )


# end user management

# works management
@admin.route("/manage_works")
def manage_works():
    return render_template("manage_works.html")


@admin.route("/manage_works/add_work")
def add_work():
    return render_template("add_works.html")


@admin.route("/add_work", methods=["post"])
def add_work1():
    title = request.form["title"]
    description = request.form["description"]
    qry = "insert into works values(Null,%s,%s,%s,Null)"

    val = (title, description, date)
    iud(qry, val)
    return """<script>alert("added");window.location="/admin/add_work"</script>"""


@admin.route("/work/delete")
def delete_work():
    id = request.args.get("id")
    qry = "DELETE FROM `works` WHERE `workid`=%s"
    iud(qry, id)
    return """<script>alert("deleted");window.location="/admin"</script>"""


@admin.route("/manage_works/assign")
def assign_works():
    works = selectall("SELECT * FROM `works`")
    leaders = selectall("SELECT userid,name FROM `user`")
    assign = selectall("SELECT * FROM `worktoleader`")
    filtered_works = list(
        filter(lambda x: x["workid"] not in [y["wid"] for y in assign], works)
    )

    # assignedstatus = selectall(
    #     "SELECT user.userid, user.name ,works.workid, works.workname, works.status from user JOIN worktoleader on worktoleader.lid = user.userid JOIN works ON worktoleader.workid = works.workid"
    # )

    return render_template(
        "assign_work.html",
        works=filtered_works,
        leaders=leaders,
        # assigned=assignedstatus,
    )


@admin.route("/assign_works1", methods=["post"])
def assign_works1():
    workid = request.form["workid"]
    leaderid = request.form["leaderid"]
    qry = "insert into assign_to_leader values(Null,%s,%s,%s,'pending')"
    val = (leaderid, workid, date)
    iud(qry, val)
    return (
        """<script>alert("assigned");window.location="/admin/assign_works"</script>"""
    )


# end works management

#  team


@admin.route("/manage_teams")
def teams():
    return render_template("teams.html")


@admin.route("/manage_teams/new_team")
def add_team():
    return render_template("add_team.html")
