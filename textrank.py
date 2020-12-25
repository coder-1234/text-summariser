#kl sum algo
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.text_rank import TextRankSummarizer

# For files and multi line string(text)
def generate_summary(file=None, text=None, top_n=5):
  if file is not None:
    parser=PlaintextParser.from_file(file,Tokenizer("english"))
  else:
    parser=PlaintextParser.from_string(text,Tokenizer("english"))
  # Using KL
  summarizer = TextRankSummarizer()
  #Summarize the document with 4 sentences
  summary = summarizer(parser.document,top_n)
  #printing the summarized sentences
  ans = []
  for sentence in summarizer(parser.document, top_n):
    ans.append(str(sentence))

  return ' '.join(ans)
