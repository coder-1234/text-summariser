#lsaSummariser
import nltk
nltk.download('punkt')
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
file="/content/sample_data/msft.txt"

LANGUAGE = "english"
summarizer = LsaSummarizer()
summarizer = LsaSummarizer(Stemmer(LANGUAGE))
summarizer.stop_words = get_stop_words(LANGUAGE)
def lsa(file=None, text=None):
  if text is None:
    parser=PlaintextParser.from_file(file,Tokenizer("english"))
  else:
    parser=PlaintextParser.from_string(text,Tokenizer("english"))
  for sentence in summarizer(parser.document, 4):
    print(sentence)
print("Summary ->")
lsa(file)