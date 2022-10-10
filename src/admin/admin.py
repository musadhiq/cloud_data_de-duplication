from datetime import datetime
from flask import *
from src.dbconnection import *

admin = Blueprint('admin', __name__, template_folder='templates')

date = datetime.now()


@admin.route('/')
def admin_home():
    works = selectall("SELECT * FROM `works`")
    return render_template("admin_home.html", works=works)


@admin.route('/manage_leaders')
def manage_leaders():
    data = selectall("SELECT id,Fname,Lname,Email FROM `leader`")
    return render_template("manage_leaders.html", data=data)


@admin.route('/leaders/new')
def add_leader():
    return render_template("add_leader.html")


@admin.route('/leaders/new1', methods=['post'])
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
    return '''<script>alert("added");window.location="/admin/manage_leaders"</script>'''


@admin.route('/leaders/edit')
def edit_leader():
    id = request.args.get('id')
    session['id'] = id
    qry = "SELECT * FROM `leader` WHERE `id`=%s"
    val = (id)
    res = selectone(qry, val)
    return render_template("edit_leader.html", data=res)


@admin.route('/leaders/delete')
def delete_leader():
    id = request.args.get('id')
    qry = "DELETE FROM `leader` WHERE `id`=%s"
    iud(qry, id)
    return '''<script>alert("deleted");window.location="/admin/manage_leaders"</script>'''


@admin.route('/add_work')
def add_work():
    return render_template("add_works.html")


@admin.route('/add_work1', methods=['post'])
def add_work1():
    title = request.form['title']
    description = request.form['description']
    qry = "insert into works values(Null,%s,%s,%s,Null)"

    val = (title, description, date)
    iud(qry, val)
    return '''<script>alert("added");window.location="/admin/add_work"</script>'''


@admin.route('/work/delete')
def delete_work():
    id = request.args.get('id')
    qry = "DELETE FROM `works` WHERE `workid`=%s"
    iud(qry, id)
    return '''<script>alert("deleted");window.location="/admin"</script>'''


@admin.route('/assign_works')
def assign_works():
    works = selectall("SELECT * FROM `works`")
    leaders = selectall("SELECT lid,Fname,Lname FROM `leader`")
    assign = selectall("SELECT * FROM `assign_to_leader`")
    filtered_works = list(filter(lambda x: x['workid'] not in [
        y['wid'] for y in assign], works))

    assignedstatus = selectall(
        "SELECT leader.lid, leader.fname, leader.lname ,works.workid, works.workname, works.status from leader JOIN assign_to_leader on assign_to_leader.lid = leader.lid JOIN works ON assign_to_leader.wid = works.workid")

    return render_template("assign_work.html", works=filtered_works, leaders=leaders, assigned=assignedstatus)


@admin.route("/assign_works1", methods=['post'])
def assign_works1():
    workid = request.form['workid']
    leaderid = request.form['leaderid']
    qry = "insert into assign_to_leader values(Null,%s,%s,%s,'pending')"
    val = (leaderid, workid, date)
    iud(qry, val)
    return '''<script>alert("assigned");window.location="/admin/assign_works"</script>'''


@admin.route('/complaint_reply')
def complaint_reply():
    return render_template("complaint_reply.html")
