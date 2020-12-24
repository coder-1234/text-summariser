import os
import textrank
basedir = os.path.abspath(os.path.dirname(__file__))

def select_algo(data,algo,filename=""):
	if filename != "":
		f=open(os.path.join('basedir','static','uploads',filename),'r')
		data=f.read()

	if algo=='textrank':
		textrank.generate_summary(filename)
	elif algo=='bla':
		pass
	else: 
		pass
	return "summary"

# Text ranking algo's