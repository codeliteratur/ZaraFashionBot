# Simple Chatbot in Python (using NLTK)

History of chatbots dates back to 1966 when a computer program called ELIZA was invented by Weizenbaum. It imitated the language of a psychotherapist from only 200 lines of code.

On similar lines let's create a very basic chatbot utlising the Python's NLTK library.It's a very simple bot with hardly any cognitive skills,but still a good way to get into NLP and get to know about chatbots.

# Outline
* [Motivation](#motivation)
* [Pre-requisites](#pre-requisites)
* [How to run](#how-to-run)


## Motivation
The idea of this project was just to utilise and test my Python skills as a first step in developing chatbots. This is the first time I am learning about NLP and I thought of creating a simple chatbot just to make use of my newly acquired knowledge.

## Pre-requisites
**NLTK(Natural Language Toolkit)**

[Natural Language Processing with Python](http://www.nltk.org/book/) provides a practical introduction to programming for language processing.

For platform-specific instructions, read [here](https://www.nltk.org/install.html)

### Installation of NLTK
```
pip install nltk
```
### Installing required packages
After NLTK has been downloaded, install required packages
```
import nltk
import sklearn
from nltk.stem import WordNetLemmatizer
nltk.download('popular', quiet=True) # for downloading popular packages
nltk.download('punkt') 
nltk.download('wordnet') 
```

## How to run
* Jupyter Notebook [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/codeliteratur/ZaraFashionBot/d01ed44db192328f8c56594aacce86757e9794f8?filepath=ZaraBot.ipynb)

You can run the [ZaraBot.ipynb](https://github.com/codeliteratur/ZaraFashionBot/blob/master/ZaraBot.ipynb) which also includes step by step instructions.
* Through Terminal
```
python zara.py
```
Initiate the conversation with any greeting as hi, hey, Hi zara etc
You can ask the chatbot questions related to the content in https://en.wikipedia.org/wiki/Zara_(retailer).
