#import packages
from flask import Flask, render_template, request, Response
import os
import random
from flask import request, jsonify
import requests
#creating an instance flask and storing in variable app
app=Flask(__name__)



'''
line_labels = [
    1, 2, 3, 4,
    5, 6, 7, 8,
    9, 10, 11,12
]
'''
'''
line_values = [
    1,2.5,3,5.2,
    2.3,3.4,2,4,
    3.4,5,2,5.3,2
]
'''

database={'mis':'123','danlaw':'123'}
path = os.getcwd()+r'\db.txt'

loginStatus = 0
storeMachData = 0
@app.route('/') #default url
def firstpage():
    return render_template("login.html")
    #return render_template("home.html",name="Aalekh")


@app.route('/form_login', methods=['POST','GET'])
def login():
    global loginStatus
    if(loginStatus == 0):
        loginStatus = 1 
        name=request.form['username']
        pwd=request.form['psw']
        #print(name,pwd)
        if name not in database:
            return render_template('login.html', info='invalid user')
        else:
            if database[name]!=pwd :
                return render_template('login.html', info='invalid password')
            else:
                file = open('data.txt','r')
                data = file.readlines()
                '''    
                t = random.randint(23, 50)
                c = random.randint(3, 9)
                x = random.randint(0, 3)
                y = random.randint(0, 3)
                z = random.randint(0, 3)
                ''' 
                value = data[len(data)-1].split(',')
                #print(value.split(','))
                t = int(value[0].strip())
                c = int(value[1].strip())
                x = float(int(value[2].strip())/100)
                y = float(int(value[3].strip())/100)
                z = float(int(value[4].strip())/100)

            file = open('fft_x_axis.txt','r')
            data = file.readlines()
            file.close()
            line_labels_x = [i+1 for i in range(len(data))]
            line_values_x = [d.strip() for d in data]
        
            file = open('fft_y_axis.txt','r')
            data = file.readlines()
            file.close()
            line_labels_y = [i+1 for i in range(len(data))]
            line_values_y = [d.strip() for d in data]

            file = open('fft_z_axis.txt','r')
            data = file.readlines()
            file.close()
            line_labels_z = [i+1 for i in range(len(data))]
            line_values_z = [d.strip() for d in data]
        
            return render_template('plotg.html',t1=t,c1=c,h1=x,v1=y,a1=z,max=10,labels_x=line_labels_x, values_x=line_values_x,labels_y=line_labels_y, values_y=line_values_y,labels_z=line_labels_z, values_z=line_values_z)

                #requests.post(url="http://127.0.0.1:5000/dataDisplay")
    else:
            file = open('data.txt','r')
            data = file.readlines()

            value = data[len(data)-1].split(',')
            #print(value.split(','))
            t = int(value[0].strip())
            c = int(value[1].strip())
            x = float(int(value[2].strip())/100)
            y = float(int(value[3].strip())/100)
            z = float(int(value[4].strip())/100)
            file.close()
            
            file = open('fft_x_axis.txt','r')
            data = file.readlines()
            file.close()
            line_labels_x = [i+1 for i in range(len(data))]
            line_values_x = [d.strip() for d in data]
        
            file = open('fft_y_axis.txt','r')
            data = file.readlines()
            file.close()
            line_labels_y = [i+1 for i in range(len(data))]
            line_values_y = [d.strip() for d in data]

            file = open('fft_z_axis.txt','r')
            data = file.readlines()
            file.close()
            line_labels_z = [i+1 for i in range(len(data))]
            line_values_z = [d.strip() for d in data]
        
            return render_template('plotg.html',t1=t,c1=c,h1=x,v1=y,a1=z,max=10,labels_x=line_labels_x, values_x=line_values_x,labels_y=line_labels_y, values_y=line_values_y,labels_z=line_labels_z, values_z=line_values_z)

@app.route('/data', methods=['GET'])
def getSensorData():
    query_parameters = request.args
    file = open('data.txt','a')
    
    temp = query_parameters.get('temp')
    current = query_parameters.get('current')
    x_axis = query_parameters.get('x')
    y_axis = query_parameters.get('y')
    z_axis = query_parameters.get('z')
    data = str(temp) + ',' + str(current) + ',' + str(x_axis) + ',' + str(y_axis) + ',' + str(z_axis)+'\n'
    #print(data)
    file.write(data)
    file.close()
    return jsonify(200)

@app.route('/getdata', methods=['GET','POST'])
def sendSensorData():
        file = open('data.txt','r')
        data = file.readlines()
        ret_data=[]
        file.close()
        '''    
        t = random.randint(23, 50)
        c = random.randint(3, 9)
        x = random.randint(0, 3)
        y = random.randint(0, 3)
        z = random.randint(0, 3)
        ''' 
        value = data[len(data)-1].split(',')
        #print(value.split(','))
        t = int(value[0].strip())
        c = int(value[1].strip())
        x = int(value[2].strip())
        y = int(value[3].strip())
        z = int(value[4].strip())
        ret_data.append(t)
        ret_data.append(c)
        ret_data.append(x)
        ret_data.append(y)
        ret_data.append(z)
        
        return jsonify(ret_data)

@app.route('/FFT_Data_x_axis', methods=['POST','GET'])
def FFT_Data_x():
    file = open('fft_x_axis.txt','w')
    fft_data = ''
    data = request.get_json()
    for x in data:
        fft_data += str(data[x]) + '\n'
    file.write(fft_data)
    file.close()
    
    return jsonify(200)

@app.route('/FFT_Data_y_axis', methods=['POST','GET'])
def FFT_Data_y():
    file = open('fft_y_axis.txt','w')
    fft_data = ''
    data = request.get_json()

    for x in data:
        fft_data += str(data[x]) + '\n'
    file.write(fft_data)
    file.close()
    
    return jsonify(200)

@app.route('/FFT_Data_z_axis', methods=['POST','GET'])
def FFT_Data_z():
    file = open('fft_z_axis.txt','w')
    fft_data = ''
    data = request.get_json()
    for x in data:
        fft_data += str(data[x]) + '\n'
    file.write(fft_data)
    file.close()
    
    return jsonify(200)

@app.route('/machineRegData', methods=['POST','GET'])
def machRegData():
    global storeMachData
    storeMachData = 0
    return render_template('NewMachineReg.html')
    
@app.route('/home', methods=['POST','GET'])
def homepg():
    return render_template('home.html')

@app.route('/logout', methods=['POST','GET'])
def logoutpg():
    loginStatus = 0
    return render_template('login.html')
    
@app.route("/get_csv")
def get_csv():
    #csv = '1,2,3\n4,5,6\n'
    file = open('data.txt','r')
    csv = 'temperature,current,RMS_x,RMS_y,RMS_z\n'
    data = file.readlines()
    for d in data:
        csv+=d
        
    file.close()
    return Response(
        csv,
        mimetype="text/csv",
        headers={"Content-disposition":
                 "attachment; filename=data.csv"})


@app.route('/dashboard', methods=['POST','GET'])
def dashboardpg():
    file = open('data.txt','r')
    data = file.readlines()

    value = data[len(data)-1].split(',')
    #print(value.split(','))
    t = int(value[0].strip())
    c = int(value[1].strip())
    x = float(int(value[2].strip())/100)
    y = float(int(value[3].strip())/100)
    z = float(int(value[4].strip())/100)
    file.close()
    
    file = open('fft_x_axis.txt','r')
    data = file.readlines()
    file.close()
    line_labels_x = [i+1 for i in range(len(data))]
    line_values_x = [d.strip() for d in data]

    file = open('fft_y_axis.txt','r')
    data = file.readlines()
    file.close()
    line_labels_y = [i+1 for i in range(len(data))]
    line_values_y = [d.strip() for d in data]

    file = open('fft_z_axis.txt','r')
    data = file.readlines()
    file.close()
    line_labels_z = [i+1 for i in range(len(data))]
    line_values_z = [d.strip() for d in data]

    return render_template('plotg.html',t1=t,c1=c,h1=x,v1=y,a1=z,max=10,labels_x=line_labels_x, values_x=line_values_x,labels_y=line_labels_y, values_y=line_values_y,labels_z=line_labels_z, values_z=line_values_z)


if __name__=='__main__':
#     app.debug = True
    app.run()

