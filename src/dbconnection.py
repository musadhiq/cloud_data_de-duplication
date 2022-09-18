import pymysql


def iud(qry, val):
    con = pymysql.connect(host='sql8.freemysqlhosting.net', port=3306,
                          user='sql8520543', password='ejdFJsBzC7', db='sql8520543')
    cmd = con.cursor()
    cmd.execute(qry, val)
    id = cmd.lastrowid
    con.commit()
    con.close()

    return id


def selectone(qry, val):
    con = pymysql.connect(host='sql8.freemysqlhosting.net', port=3306, user='sql8520543',
                          password='ejdFJsBzC7', db='sql8520543', cursorclass=pymysql.cursors.DictCursor)
    cmd = con.cursor()
    cmd.execute(qry, val)
    res = cmd.fetchone()

    return res


def selectall(qry):
    con = pymysql.connect(host='sql8.freemysqlhosting.net', port=3306, user='sql8520543',
                          password='ejdFJsBzC7', db='sql8520543', cursorclass=pymysql.cursors.DictCursor)
    cmd = con.cursor()
    cmd.execute(qry)
    res = cmd.fetchall()
    return res


def selectall2(qry, val):
    con = pymysql.connect(host='sql8.freemysqlhosting.net', port=3306, user='sql8520543',
                          password='ejdFJsBzC7', db='sql8520543', cursorclass=pymysql.cursors.DictCursor)
    cmd = con.cursor()
    cmd.execute(qry, val)
    res = cmd.fetchall()
    return res
