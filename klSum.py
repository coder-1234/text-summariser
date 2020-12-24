#kl sum algo
!pip install sumy
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
nltk.download('punkt')
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.kl import KLSummarizer

# For files and multi line string(text)
file="/content/sample_data/msft.txt"
def klSumSummarizer(file=None, text=None):
  if text is None:
    parser=PlaintextParser.from_file(file,Tokenizer("english"))
  else:
    parser=PlaintextParser.from_string(text,Tokenizer("english"))
  # Using KL
  summarizer = KLSummarizer()
  #Summarize the document with 4 sentences
  summary = summarizer(parser.document,4)
  #printing the summarized sentences
  for sentence in summary:
      print(sentence)
print("Summary ->")
klSumSummarizer(file)
