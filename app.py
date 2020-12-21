from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import TextField, TextAreaField, SubmitField, SelectField, validators, ValidationError
from flask_wtf.file import FileField, FileRequired, FileAllowed
from werkzeug import secure_filename
from summariser import select_algo
import os
app = Flask(__name__)
app.secret_key = 'A very long secret_key'
basedir = os.path.abspath(os.path.dirname(__file__))
UPLOADED_FILES_DEST = os.path.join('basedir','static','uploads')

algo_choices = [('1','testrank'),('2','algo2'),('3','algo3')]
class InputForm(FlaskForm):
	name = TextField("Enter your name",[validators.Required("Please enter your name")])
	algo = SelectField("Select desired algorithm",choices=algo_choices)
	text = TextAreaField("Enter text here",render_kw={"rows": 20, "cols": 80})
	file = FileField("Choose desired txt file",validators=[FileAllowed(['txt'],'txt files only')])
	submit = SubmitField()

@app.route('/',methods=['POST','GET'])
def index():
	print('Server running')
	form = InputForm()
	if request.method == 'GET':
		return render_template('index.html',form=form)
	elif request.method == 'POST':
		ans = select_algo(form.text.data,form.select.data,form.file.data.filename)
		return render_template('index.html',form=form,ans=ans)

@app.route('/algos',methods=['GET'])
def algos():
	print('Function called')
	return render_template('algorithms.html')

if __name__ == '__main__':
	app.run(debug = True)