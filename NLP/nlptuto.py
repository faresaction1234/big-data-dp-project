import pandas as pd
import nltk
from bs4 import BeautifulSoup
import string 
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer
dt = pd.read_csv('C:/Users/MFBA/Documents1/big data dp project/NLP/amazon_co-ecommerce_sample.csv')

reviews = dt['customer_reviews'].str.split("//",
                                           n=4,
                                           expand=True)
dt['review_title'] = reviews[0]
dt['rating'] = reviews[1]
dt['review_date'] = reviews[2]
dt['customer_name'] = reviews[3]
dt['review'] = reviews[4]

dt.drop(columns='customer_reviews', inplace=True)
def remove_punctuation(text):
    no_punct = "".join([c for c in text if c not in string.punctuation])
    return no_punct
#def Remove_stopwords(text):
#    words = [w for w in text if w not in stopwords.words('english')]
#    return words

dt['review'] = dt['review'].apply(lambda x: remove_punctuation(str(x)))
tokenizer = RegexpTokenizer(r'\w+')
from nltk.tokenize import WhitespaceTokenizer
w_tokenizer = WhitespaceTokenizer()
from nltk.stem.snowball import SnowballStemmer
englishStemmer=SnowballStemmer("english") 
def stemm_texts(text):
   return [englishStemmer.stem(w) for w in w_tokenizer.tokenize(str(text))]   
dt = dt['review'].apply(lambda y: stemm_texts(y))
from sklearn.feature_extraction.text import TfidfVectorizer
lemmas = dt.apply(lambda x: ' '.join(x))
vect =TfidfVectorizer()
features = vect.fit_transform(lemmas)