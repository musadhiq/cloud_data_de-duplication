from flask import *
from src.dbconnection import *
from datetime import datetime

member = Blueprint('member', __name__, template_folder='templates')


@member.route("/")
def member_home():
    return render_template("member_home.html")


@member.route('/manage_profile')
def member_profile():
    id = session['lid']
    qry = "SELECT * FROM `member` WHERE `lid`=%s"
    val = (id)
    res = selectone(qry, val)
    return render_template("m_editprofile.html", data=res)


@member.route('/update', methods=['post'])
def update_member():
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
    return '''<script>alert("success");window.location="/member"</script>'''


@member.route('/works')
def member_work():
    return render_template("member_work.html")


@member.route('/notifications')
def notifications():
    return render_template("notification.html")


@member.route('/send_feedback')
def send_feedback():
    return render_template("send_feedback.html")


@member.route('/ask_doubt')
def ask_doubt():
    return render_template("ask_doubt.html")


@member.route('/post_complaint')
def post_complaint():
    return render_template("post_complaint.html")
