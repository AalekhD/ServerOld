#import libraries
from flask import Flask, render_template, request
#from Flask_MySQLdb import MySQL
#import MySQLdb.cursors
app = Flask(__name__)

#code for connection
# app.config['MYSQL_HOST'] = 'localhost'#hostname
# app.config['MYSQL_USER'] = 'root'#username
# app.config['MYSQL_PASSWORD'] = 'Samu2996..'#password
# app.config['MYSQL_DB'] = 'machine_details'#database name

#mysql = MySQL(app)
# @app.route('/')

@app.route('/',methods=['GET','POST'])
def NewMachineReg():
    return render_template('index.html',msg="Hello",form = form)
    
#     msg=''
#     #applying empty validation
#     if request.method == 'POST' and 'company' in request.form and 'equipmentnm' in request.form and 'Equiploc' in request.form and 'Ratedspeed' in request.form and 'power' in request.form and 'Equipmentclass' in request.form and 'Remark' in request.form:
#         #passing HTML form data into python variable
#         c = request.form['company']
#         e = request.form['equipmentnm']
#         l = request.form['Equiploc']
#         s = request.form['Ratedspeed']
#         p = request.form['power']
#         k = request.form['Equipmentclass']
#         r = request.form['Remark']
#         #creating variable for connection
# #        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
#         #query to check given data is present in database or no
#   #      cursor.execute('SELECT * FROM machines WHERE EquipmentName = % s', (e,))
#  #       #fetching data from MySQL
#    #     result = cursor.fetchone()
#     #        msg = 'You have successfully added machine details !'
#     elif request.method == 'POST':
#         msg = 'Please enter machine details !'
#     return render_template('NewMachineReg.html', msg=msg)

if __name__ == '__main__':
    app.debug = True
    app.run()