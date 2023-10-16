
#!/usr/bin/env python
# coding: utf-8

# In[ ]:



#defining function to define cosine similarity
from numpy import dot
from numpy.linalg import norm
import gensim
from gensim.models import Word2Vec
from gensim.models import FastText
import pandas as pd

import numpy as np
import gensim
from gensim.models import KeyedVectors
from gensim.models.fasttext import FastText  

from matplotlib import pyplot
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


from read_data import read_data
from preprocessing import preprocessing_input
from return_embed import get_mean_vector
import pickle

def cos_sim(a,b):

    return dot(a, b)/(norm(a)*norm(b)) 
#function to return top n similar results


def top_n(query,model_name,column_name):
    vector_size=100
    window_size=3
    df=read_data()
    if model_name=='Skipgram':
        
   
        word2vec_model=Word2Vec.load('https://medicalembeddings.blob.core.windows.net/testcontainer/data/output/model_Skipgram.bin?sp=racwdymeop&st=2021-09-27T18:07:07Z&se=2021-12-31T02:07:07Z&spr=https&sv=2020-08-04&sr=b&sig=HcNHttcKAJGP55xqqP%2B2mtv0%2BZDIOKDhz6utlRWZSlQ%3D')
        K=pd.read_csv('https://medicalembeddings.blob.core.windows.net/testcontainer/data/output/Skipgram_vec.csv?sp=racwdymeop&st=2021-09-27T18:08:05Z&se=2021-12-31T02:08:05Z&spr=https&sv=2020-08-04&sr=b&sig=YW0RNtb2VxQz6wnKmF2MPwBG%2BF8w%2FbddPmvBPmaXkNw%3D')
    else:
        
        import os
        filepath = os.path.join('https:', 'medicalembeddings.blob.core.windows.net', 'testcontainer', 'data', 'output', 'model_Fasttext1.bin?sp=racwdymeop&st=2021-10-07T19:22:25Z&se=2021-12-31T03:22:25Z&spr=https&sv=2020-08-04&sr=b&sig=yNtp524pRyC0QnYAUuJkpHUinHMPJ93Gxi5SwKnjyEs%3D')
        with open(filepath, 'rb') as file1:
            word2vec_model = pickle.load(file1)
            file1.close()
        # word2vec_model=Word2Vec.load('https://medicalembeddings.blob.core.windows.net/testcontainer/data/output/model_Fasttext1.bin?sp=racwdymeop&st=2021-10-06T17:30:46Z&se=2021-12-31T01:30:46Z&spr=https&sv=2020-08-04&sr=b&sig=h9KuNq9zLYgRxPYcjC%2F8pU6iGmHLJwiQ6UNC5q9wa3g%3D')
        K=pd.read_csv('https://medicalembeddings.blob.core.windows.net/testcontainer/data/output/Fasttext_vec.csv?sp=racwdymeop&st=2021-09-27T21:21:33Z&se=2021-12-31T05:21:33Z&spr=https&sv=2020-08-04&sr=b&sig=eFAAaZ5RTGhePIBaKc1z%2FvA7%2FMkLUNbBvdytJXGWLmk%3D')
    #input vectors
    query=preprocessing_input(query)
    
    query_vector=get_mean_vector(word2vec_model,query)
    #Model Vectors
      #Loading our pretrained vectors of each abstracts

    p=[]                          #transforming dataframe into required array like structure as we did in above step
    for i in range(df.shape[0]):
        p.append(K[str(i)].values)    
    x=[]
    #Converting cosine similarities of overall data set with input queries into LIST
    for i in range(len(p)):
        x.append(cos_sim(query_vector,p[i]))
    
    
 #store list in tmp to retrieve index
    tmp=list(x)
    
 #sort list so that largest elements are on the far right
    
    res = sorted(range(len(x)), key = lambda sub: x[sub])[-10:]
    sim=[tmp[i] for i in reversed(res)]
    
 #get index of the 10 or n largest element
    L=[]
    for i in reversed(res):
    
        L.append(i)
        
    df1=read_data()    
    return df1.iloc[L, [1,2,5,6]],sim     #returning dataframe (only id,title,abstract ,publication date)
