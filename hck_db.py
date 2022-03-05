from flask import Flask, render_template, request
import pymysql
mydb=pymysql.connect(host="localhost",user="root",password="gate2022",database="dbs_hack")
cursor=mydb.cursor()
app = Flask(__name__)
@app.route('/')
def mainpage():
    return render_template('hni.html')
@app.route('/hni')
def hni():
    return render_template('hni.html')
def wm():
    return render_template('wm.html')
@app.route('/hni',methods=['POST','GET'])
def hni_user():
    if request.method == 'POST':
        cursor.execute("insert into hni(name,email,password) values(%s,%s,%s)",(request.form['username','Email','password'],))
        #result=cursor.fetchall()
        return render_template('temp.html',data=result)
def wm():
    return render_template('wm.html')
@app.route('/wm',methods=['POST','GET'])
def wm_user():
    if request.method == 'POST':
        cursor.execute("insert into wm(name,email,password) values(%s,%s,%s)",(request.form['email','password'],))
        result=cursor.fetchall()
        return render_template('wm_schedule.html',data=result)
app.run()
''''
@app.route('/hnischedule')
def hnischedule():
    return render_template('hnischedule.html')
@app.route('/hnidashboard')
def hnidashboard():
    return render_template('
@app.route('/hniaccept')
def hniaccept():
    return render_template('hniaccept.html')
@app.route('/hnireject')
def hnireject():
    return render_template('hnireject.html')
@app.route('/hnireschedule')
def hnireschedule():
    return render_template('hnireschedule.html')
@app.route('/hninotification')
def hninotification():
    return render_template('hninotification.html')
@app.route('/wm')
def wmschedule():
    return render_template('wmschedule.html')
@app.route('/wmdashboard')
def wmdashboard():
    return render_template('wmdashboard.html')
@app.route('/wmiaccept')
def wmccept():
    return render_template('wmaccept.html')
@app.route('/wmreject')
def wmreject():
    return render_template('wmreject.html')
@app.route('/wmreschedule')
def wmreschedule():
    return render_template('wmreschedule.html')
@app.route('/wmnotification')
def wmnotification():
    return render_template('wmnotification.html')
'''
