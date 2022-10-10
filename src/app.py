from flask import *
from src.dbconnection import *
from src.templates import *
from datetime import datetime

# bluprints
from src.admin.admin import admin
from src.leader.leader import leader
from src.member.member import member

app = Flask(__name__)
app.register_blueprint(admin, url_prefix='/admin')
app.register_blueprint(leader, url_prefix='/leader')
app.register_blueprint(member, url_prefix='/member')

app.secret_key = "anystringhere"

date = datetime.today()


@app.route('/')
def index():
    return render_template('login.html')


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
        id = res['id']
        session['lid'] = id
        return '''<script>alert("welcome to member");window.location="/member"</script>'''
    else:
        flash("incorrect username or password.")
        return '''<script>window.location="/";</script>'''


app.run(debug=True)
