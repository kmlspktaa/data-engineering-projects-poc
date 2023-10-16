#!/usr/bin/env python
# coding: utf-8

# #  Importing Libraries

# In[1]:

import sys
sys.path.append("..")
import streamlit as st  #importing streamlit liabrary


# In[2]:


import pandas as pd

import numpy as np
import gensim
from gensim.models import Word2Vec
from gensim.models import FastText
from sklearn.decomposition import PCA
from matplotlib import pyplot


# In[3]:


import matplotlib.pyplot as plt
import plotly.graph_objects as go     # our main display package
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



def cos_sim(a,b):

    return dot(a, b)/(norm(a)*norm(b)) 






pd.set_option("display.max_colwidth", -1)       #this function will display full text from each column

import sys
# insert at 1, 0 is the script path (or '' in REPL)


from top_n import top_n
#streamlit function 
def main():
    # Load data and models
    
      
    

    st.title("Medical Search engine")      #title of our app
    st.write('Select Model')       #text below title

    
    model_name = st.selectbox("Model",options=['Skipgram' , 'Fasttext'])
    

    st.write('Type your query here')

    query = st.text_input("Search box")#getting input from user
    column_name='Abstract'

    
    if query:
        
        P,sim =top_n(query,model_name,column_name)     #storing our output dataframe in P
        #Plotly function to display our dataframe in form of plotly table
        fig = go.Figure(data=[go.Table(header=dict(values=['ID', 'Title','Abstract','Publication Date','Similarity']),cells=dict(values=[list(P['Trial ID'].values),list(P['Title'].values), list(P['Abstract'].values),list(P['Publication date'].values),list(np.around(sim,4))],align=['center','right']))])
        #displying our plotly table
        fig.update_layout(height=1700,width=1000,margin=dict(l=0, r=10, t=20, b=20))
        
        st.plotly_chart(fig) 
        # Get individual results
    

if __name__ == "__main__":
    main()

