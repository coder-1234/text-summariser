from flask import Flask, render_template, request, redirect
from flask_wtf import FlaskForm
from wtforms import TextField, TextAreaField, SubmitField, SelectField, IntegerField, validators, ValidationError
from flask_wtf.file import FileField, FileRequired, FileAllowed
from werkzeug import secure_filename
from summariser import select_algo
import os
app = Flask(__name__)
app.secret_key = 'A very long secret_key'
basedir = os.path.abspath(os.path.dirname(__file__))
UPLOADED_FILES_DEST = os.path.join(basedir,'static','uploads')

algo_choices = [('1','Textrank'),('2','KLSum'),('3','Latent Semantic analysis')]
class InputForm(FlaskForm):
	name = TextField("Enter your name",[validators.Required("Please enter your name")])
	select = SelectField("Select algorithm (Choose randomly if you are unaware of these)",choices=algo_choices)
	text = TextAreaField("Enter text here",render_kw={"rows": 20, "cols": 80})
	file = FileField("Choose desired txt file",validators=[FileAllowed(['txt'],'Only txt files are allowed')])
	sentences = IntegerField('Enter lines of summary')
	submit = SubmitField()

@app.route('/',methods=['POST','GET'])
def index():
	print('Server running')
	form = InputForm()
	if request.method == 'GET':
		return render_template('index.html',form=form,ans="")

	elif request.method == 'POST':
		if form.validate_on_submit():
			algo = dict(algo_choices).get(form.select.data)

			if form.file.data is None:
				ans = select_algo(algo,form.sentences.data,form.text.data)
			else:
				f = form.file.data
				f.save(os.path.join(UPLOADED_FILES_DEST, f.filename))
				ans = select_algo(algo,form.sentences.data,filename=f.filename)
				os.remove(os.path.join(UPLOADED_FILES_DEST, f.filename))

			return render_template('index.html',form=form,ans=ans)
		else: return render_template('index.html',form=form,ans="")


@app.route('/algos',methods=['GET'])
def algos():
	print('Function called')
	return render_template('algorithms.html')

if __name__ == '__main__':
	app.run(debug = True)