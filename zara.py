
#I'm Zara. Your virtual fashion consultant!

#import required packages & libraries
import io
import random
import string 		# to process standard python strings
import warnings
import numpy as np
#machine learning library to extract words according to stop word
from sklearn.feature_extraction.text import TfidfVectorizer    
from sklearn.metrics.pairwise import cosine_similarity
import warnings
warnings.filterwarnings('ignore')

import nltk
from nltk.stem import WordNetLemmatizer
nltk.download('popular', quiet=True) # for downloading packages

# uncomment the following only the first time
#nltk.download('punkt') # first-time use only
#nltk.download('wordnet') # first-time use only


#Reading in the corpus text file chatbot
with open('aboutfashion.txt','r', encoding='utf8', errors ='ignore') as fin:
    raw = fin.read().lower()

#TOkenisation
sent_tokens = nltk.sent_tokenize(raw)# converts to list of sentences 
word_tokens = nltk.word_tokenize(raw)# converts to list of words

# Preprocessing
lemmer = WordNetLemmatizer()
def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))


# Keyword Matching
GREETING_INPUTS = ("hello", "hi","Hey,Zara!","hey","hello,there!", )
GREETING_RESPONSES = ["hi", "hey", "hi there", "hello", "Hi,I am here!"]

def greeting(sentence):
    """If user's input is a greeting, return a greeting response"""
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)


# Generating response
def response(user_response):
    bot_response=''
    sent_tokens.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx=vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if(req_tfidf==0):
        bot_response=bot_response+"I am sorry! I don't understand you."
        return bot_response
    else:
        bot_response = bot_response+sent_tokens[idx]
        return bot_response


flag=True
print("Zara: My name is Zara. I can answer your fashion queries. If you want to exit, type Bye!")
while(flag==True):
    user_response = input().lower()
    
    if(user_response!='bye'):
        if(user_response=='thanks' or user_response=='thank you' or user_response=='Great! You just made my day' or user_response=='thanks a lot' ):
            flag=False
            print("ZARA: You are welcome.Glad to help you.")
        else:
            if(greeting(user_response)!=None):
                print("ZARA: "+greeting(user_response))
            else:
                print("ZARA: ",end="")
                print(response(user_response))
                sent_tokens.remove(user_response)
    else:
        flag=False
        print("ZARA: Bye for now! Ping me again if you want to know something fashion..")    
        
        

