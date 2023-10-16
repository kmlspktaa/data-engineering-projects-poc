#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import string # used for preprocessing
import re # used for preprocessing
import nltk # the Natural Language Toolkit, used for preprocessing
import numpy as np # used for managing NaNs
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords # used for preprocessing
from nltk.stem import WordNetLemmatizer # used for preprocessing
from sklearn.model_selection import train_test_split
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt')
import gensim
from gensim.models import Word2Vec


# In[ ]:



# In[4]:


#to get mean vectors
def get_mean_vector(word2vec_model, words):
    # remove out-of-vocabulary words
    
    words = [word for word in word_tokenize(words) if word in list(word2vec_model.wv.index_to_key)] #if word is in vocab 
    if len(words) >= 1:
        return np.mean(word2vec_model.wv[words], axis=0)
    else:
        return np.array([0]*100)


# In[3]:


def return_embed(word2vec_model,df,column_name):
    
    K1=[]                                     #defining empty list
    for i in df[column_name]:
        K1.append(list(get_mean_vector(word2vec_model, i)))   #appending array to the list
    return K1    

