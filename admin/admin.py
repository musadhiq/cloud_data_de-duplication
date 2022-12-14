from datetime import datetime
from flask import *
from src.dbconnection import *

admin = Blueprint("admin", __name__, template_folder="templates")

date = datetime.now()


@admin.route("/")
def admin_home():
    # works = selectall("SELECT * FROM `works`")
    return render_template("index.html")


# user management


@admin.route("/manage_users")
def manage_users():
    # data = selectall("SELECT userid,name,email FROM `user`")
    return render_template("manage_users.html")


@admin.route("/manage_users/new_user")
def new_user():
    return render_template("add_user.html")


@admin.route("/add_user", methods=["post"])
def add_user():
    name = request.form["name"]
    gender = request.form["gender"]
    place = request.form["place"]
    pin = request.form["pin"]
    post = request.form["post"]
    email = request.form["email"]
    phone = request.form["phone"]
    address = request.form["address"]
    password = request.form["password"]
    qry = "insert into login values(Null,%s,%s,'leader')"
    val = (name, password)
    id = iud(qry, val)
    qry1 = "insert  into user values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val1 = (id, name, email, address, post, pin, phone, place, gender)
    iud(qry1, val1)
    return """<script>alert("added");window.location="/admin/manage_leaders"</script>"""


@admin.route("/manage_users/edit_user")
def edit_user():
    # id = request.args.get("id")
    # session["id"] = id
    # qry = "SELECT * FROM `leader` WHERE `id`=%s"
    # val = id
    # res = selectone(qry, val)
    return render_template("edit_user.html")


@admin.route("/user/delete")
def delete_leader():
    id = request.args.get("id")
    qry = "DELETE FROM `leader` WHERE `id`=%s"
    iud(qry, id)
    return (
        """<script>alert("deleted");window.location="/admin/manage_leaders"</script>"""
    )


# end user management

# works management
@admin.route("/manage_works")
def manage_works():
    return render_template("manage_works.html")


@admin.route("/manage_works/add_work")
def add_work():
    return render_template("add_work.html")


@admin.route("/add_work1", methods=["post"])
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


@admin.route("/assign_works")
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


@admin.route("/complaint_reply")
def complaint_reply():
    return render_template("complaint_reply.html")
