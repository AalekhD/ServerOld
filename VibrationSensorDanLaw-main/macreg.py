from flask import Flask, render_template,redirect,url_for,session
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,RadioField,TextAreaField, IntegerField
from wtforms.validators import InputRequired

app=Flask(__name__)
app.config['SECRET_KEY']='some_random_secret'

class MachineRegForm(FlaskForm):
    company=StringField('Name of the company',validators=[InputRequired()])
    equipmentnm=StringField('Name of equipment',validators=[InputRequired()])
    Equiploc=StringField('Equipment location',validators=[InputRequired()])
    Ratedspeed=IntegerField('Speed in RPM',validators=[InputRequired()])
    power=IntegerField('Power in kw',validators=[InputRequired()])
    Equipmentclass=IntegerField('Enter class of equipment',validators=[InputRequired()])
    Remark=TextAreaField('Notes')
    submit=SubmitField('Submit')
    
@app.route('/',methods=['GET','POST'])
def formadd():
    form=MachineRegForm()
    if form.validate_on_submit():
        session['company']=form.company.data
        session['equipmentnm']=form.equipmentnm.data
        session['Equiploc']=form.Equiploc.data
        session['Ratedspeed']=form.Ratedspeed.data
        session['power']=form.power.data
        session['Equipmentclass']=form.Equipmentclass.data
        session['Remark']=form.Remark.data
        session['submit']=form.submit.data
        print(session['company'])
        return redirect(url_for("MachineAdd"))
    return render_template('index.html',form=form)

@app.route('/MachineAdd')
def MachineAdd():

    return render_template('MachineAdd.html')

if __name__=='__main__':
    app.run()
    