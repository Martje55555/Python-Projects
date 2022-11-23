#Import the libraries
import nltk # pip install nltk
from newspaper import Article # pip install newspaper3
from gtts import gTTS # pip install gtts
import os

# url of article you want to convert to speech
url = 'https://hackr.io/blog/top-tech-companies-hiring-python-developers'

# download and parse article
article = Article(url)
article.download()
article.parse()

nltk.download('punkt')
# apply natural language processing
article.nlp()

# extract the text
myText = article.text

# english
language = 'en'

# pass the text and language to the engine to convert to speech
myobj = gTTS(text=myText, lang=language, slow=False)

# save the article
myobj.save("read_article.mp3")

# open the mp3 file
os.system('start read_article.mp3' if os.name=='nt' else 'afplay read_article.mp3')
