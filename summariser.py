import os
from textrank import generate_summary
from klSum import klSumSummarizer
from Lsa import lsa

basedir = os.path.abspath(os.path.dirname(__file__))
UPLOADED_FILES_DEST = os.path.join(basedir,'static','uploads')

def select_algo(algo,sentences,data=None,filename=None):
	filePath = None
	if filename is not None: filePath = os.path.join(UPLOADED_FILES_DEST,filename) 
	summary = ""
	if algo in 'Textrank':
		summary=generate_summary(filePath,data,sentences)
	elif algo in 'KLSum':
		summary=klSumSummarizer(filePath,data,sentences)
	elif algo in 'Latent Semantic analysis': 
		summary=lsa(filePath,data,sentences)

	return summary