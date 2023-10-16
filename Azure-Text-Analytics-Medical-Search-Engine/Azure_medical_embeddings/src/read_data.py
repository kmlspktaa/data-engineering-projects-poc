#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np


# In[ ]:


def read_data():
    df=pd.read_csv('https://medicalembeddings.blob.core.windows.net/testcontainer/data/input/Dimension-covid.csv?sp=racwdymeop&st=2021-09-27T18:00:51Z&se=2021-12-31T02:00:51Z&spr=https&sv=2020-08-04&sr=b&sig=auFUb%2B%2FoZUgjlhq74wZwk394V6%2FqPrPGVG5koxSj9vQ%3D')   #for preprocessing
    df1=pd.read_csv('https://medicalembeddings.blob.core.windows.net/testcontainer/data/input/Dimension-covid.csv?sp=racwdymeop&st=2021-09-27T18:00:51Z&se=2021-12-31T02:00:51Z&spr=https&sv=2020-08-04&sr=b&sig=auFUb%2B%2FoZUgjlhq74wZwk394V6%2FqPrPGVG5koxSj9vQ%3D')  #for returning results
    return df.iloc[:100,:]

