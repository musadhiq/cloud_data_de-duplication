import pymysql

hostname = "localhost"
username = "root"
portnum = 3306
password = ""
dbname = "cloud"


def iud(qry, val):
    con = pymysql.connect(
        host=hostname, port=portnum, user=username, password=password, db=dbname
    )
    cmd = con.cursor()
    cmd.execute(qry, val)
    id = cmd.lastrowid
    con.commit()
    con.close()

    return id


def selectone(qry, val):
    con = pymysql.connect(
        host=hostname,
        port=portnum,
        user=username,
        password=password,
        db=dbname,
        cursorclass=pymysql.cursors.DictCursor,
    )
    cmd = con.cursor()
    cmd.execute(qry, val)
    res = cmd.fetchone()

    return res


def selectall(qry):
    con = pymysql.connect(
        host=hostname,
        port=portnum,
        user=username,
        password=password,
        db=dbname,
        cursorclass=pymysql.cursors.DictCursor,
    )
    cmd = con.cursor()
    cmd.execute(qry)
    res = cmd.fetchall()
    return res


def selectall2(qry, val):
    con = pymysql.connect(
        host=hostname,
        port=portnum,
        user=username,
        password=password,
        db=dbname,
        cursorclass=pymysql.cursors.DictCursor,
    )
    cmd = con.cursor()
    cmd.execute(qry, val)
    res = cmd.fetchall()
    return res
