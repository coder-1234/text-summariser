#kl sum algo
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
nltk.download('punkt')
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.kl import KLSummarizer

# For files and multi line string(text)
def klSumSummarizer(file=None, text=None, top_n=5):
  if file is not None:
    parser=PlaintextParser.from_file(file,Tokenizer("english"))
  else:
    parser=PlaintextParser.from_string(text,Tokenizer("english"))
  # Using KL
  summarizer = KLSummarizer()
  #Summarize the document with 4 sentences
  summary = summarizer(parser.document,top_n)
  #printing the summarized sentences
  ans = []
  for sentence in summarizer(parser.document, top_n):
    ans.append(str(sentence))

  return ' '.join(ans)
