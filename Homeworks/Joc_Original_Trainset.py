#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 21:54:26 2020

@author: jocelynragukonis
"""
# %% Importing Data

import pandas as pd

trainData = pd.read_csv('./ee627ws-2020fall/trainIdx2_matrix.txt', 
                        sep='|',
                        names=['UserID','ItemID', 'Rating'],
                        engine='python', 
                        header=None)

from surprise import Dataset
from surprise import Reader


trainData.columns = ['user', 'item', 'rating']

reader = Reader(rating_scale=(trainData.rating.min(), trainData.rating.max()))

import pickle

filename = 'Reader.pickle'
pickle.dump(reader, open(filename, 'wb'))

data = Dataset.load_from_df(trainData[['user', 'item', 'rating']], reader)

del trainData 

# %% Fit CoClustering Model 

from surprise import CoClustering

algo = CoClustering()
algo.fit(data.build_full_trainset())

# %% Fit BaselineOnly Model

from surprise import BaselineOnly

algo = BaselineOnly()
algo.fit(data.build_full_trainset())

# %% Fit KNNWithMeans Model

from surprise import KNNWithMeans 

sim_options = { 'name': 'pearson_baseline', 
               'user_based': True,
              }

algo = KNNWithMeans(k=20, sim_options=sim_options)
algo.fit(data.build_full_trainset())

# %% Fit SVD Model 

from surprise import SVD

algo = SVD()
algo.fit(data.build_full_trainset())

# %% Save model 

filename = 'SVD.pickle'
pickle.dump(algo, open(filename, 'wb'))
