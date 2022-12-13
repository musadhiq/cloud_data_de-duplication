from flask import *
from src.dbconnection import *

member = Blueprint("member", __name__, template_folder="templates")


# login user
@member.route("/login",methods=['post'])
def memberLogin():
    username = request.form['username']
    password = request.form['password']

    qry = "SELECT * FROM `login` WHERE `uname`=%s AND `password`=%s"
    val = (username, password)
    res = selectone(qry, val)
    if res is None:
        return jsonify({'result':"invalid"})
    else:
        return jsonify({"user":res})

  
# get User
@member.route("/get_user", methods=['post'])
def get_user():
    id = request.form['userid']
    qry = "select * from users where userid=%s"
    res = selectone(qry, id)
    return jsonify({"data":res})


# update user profile
@member.route("/update_profile", methods=["post"])
def update_member():
    id = request.form["userid"]
    name = request.form["name"]
    Gender = request.form["gender"]
    Place = request.form["place"]
    Pin = request.form["pin"]
    Post = request.form["post"]
    Email = request.form["email"]
    Phone = request.form["phone"]
    qry = "update user set name=%s,gender=%s,place=%s,pin=%s,post=%s,email=%s,phone=%s where id=%s"
    val = (name, Gender, Place, Pin, Post, Email, Phone, id)
    iud(qry, val)
    return jsonify({"status":"success"})


# update Work Status
@member.route("/update_work",methods=['post'])
def member_work():
    status = request.form['status']
    workid = request.form['workid']

    qry = "update works set status=%s where workid=%s"
    val =(status,workid)
    iud(qry,val)
    return jsonify({"status": "success"})


# send Feedback
@member.route("/send_feedback",methods=['post'])
def send_feedback():
    feedback = request.form['feedback']
    userid = request.form['userid']

    qry ="update feedbacks set feedback=%s,userid=%s" 
    val =(feedback,userid)
    iud(qry,val)
    return jsonify({"status":"success"})


# send complaint
@member.route("/send_complaint",methods=['post'])
def send_complaint():
    complaint = request.form['complaint']
    userid = request.form['userid']

    qry ="update complaints set complaint=%s,userid=%s" 
    val =(complaint,userid)
    iud(qry,val)
    return jsonify({"status":"success"})


# view complaint reply
@member.route("/view_creply",methods=['post'])
def view_creply():
    userid = request.form['userid']
    qry = "select * from complaints where userid=%s"
    res = selectall2(qry,userid)
    return jsonify({"data":res})


