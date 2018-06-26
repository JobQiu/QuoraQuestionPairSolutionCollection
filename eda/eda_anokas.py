#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 16:53:20 2018

@author: xavier.qiu
"""

# https://www.kaggle.com/anokas/data-analysis-xgboost-starter-0-35460-lb
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import os
import gc
import matplotlib.pyplot as plt
import seaborn as sns

pal = sns.color_palette()

#%%

df_train = pd.read_csv('../input/train.csv')
df_train.head()

#%%
from nltk.corpus import stopwords
stops = set(stopwords.words("english"))

def word_match_share(row):
    q1words = {}
    q2words = {}
    for w in str(row['question1']).lower().split():
        if w not in stops:
            q1words[w] = 1
    for w in str(row['question2']).lower().split():
        if w not in stops:
            q2words[w] = 1
    if len(q1words) == 0 or len(q2words) == 0:
        return 0
    
    shared_w_in_q1 = [w for w in q1words.keys() if w in q2words]
    shared_w_in_q2 = [w for w in q2words.keys() if w in q1words]
    
    pass















