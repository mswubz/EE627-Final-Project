#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 23:36:48 2020

@author: jocelynragukonis
"""

# %% Import Model 
import pickle 

filename = 'SVD.pickle'
algo = pickle.load(open(filename, 'rb'))

# %% Import Test Model

import pandas as pd 

data = pd.read_csv('./ee627ws-2020fall/testTrack_hierarchy.txt', 
                        sep='|',
                        names=['UserID', 'TrackID', 'AlbumID', 'ArtistID', 'GenreID_1', 'GenreID_2', 'GenreID_3', 'GenreID_4', 'GenreID_5', 'GenreID_6', 'GenreID_7', 'GenreID_8', 'GenreID_9', 'GenreID_10', 'GenreID_11', 'GenreID_12', 'GenreID_13', 'GenreID_14', 'GenreID_15', 'GenreID_16', 'GenreID_17', 'GenreID_18', 'GenreID_19', 'GenreID_20', 'GenreID_21'],
                        engine='python', 
                        na_values=['None'],
                        header=None)

testData = data[['UserID', 'TrackID']]
del data

from surprise import Dataset

filename = 'Reader.pickle'
reader = pickle.load(open(filename, 'rb'))

testData.columns = ['user', 'item']

testData['rating'] = 0

data = Dataset.load_from_df(testData[['user', 'item', 'rating']], reader)


# %% Build set

temp = data.build_full_trainset()

testset = temp.build_testset()

# %% Make Predictions

predictions = algo.test(testset)

# %% Make array of all ratings

ratings = []

for i in range(len(predictions)):
    ratings.append(predictions[i].est)

# %% Add ratings to dataframe

Ratings = pd.DataFrame(data=ratings, columns = ['ratings'])

testData['rating'] = Ratings['ratings']

del Ratings

# %% Group ratings by user

grouped_ratings = []

for i in range(0, len(ratings),6):
    grouped_ratings.append(ratings[i:i+6])
    
# %% Top three recommend 

from collections import defaultdict

def get_top_n(predictions, n=3):
    """Return the top-N recommendation for each user from a set of predictions.

    Args:
        predictions(list of Prediction objects): The list of predictions, as
            returned by the test method of an algorithm.
        n(int): The number of recommendation to output for each user. Default
            is 10.

    Returns:
    A dict where keys are user (raw) ids and values are lists of tuples:
        [(raw item id, rating estimation), ...] of size n.
    """

    # First map the predictions to each user.
    top_n = defaultdict(list)
    for uid, iid, true_r, est, _ in predictions:
        top_n[uid].append((iid, est))

    # Then sort the predictions for each user and retrieve the k highest ones.
    for uid, user_ratings in top_n.items():
        user_ratings.sort(key=lambda x: x[1], reverse=True)
        top_n[uid] = user_ratings[:n]

    return top_n

top_n = get_top_n(predictions, n=3)


# %% Assign 0 and 1 to reccomend 

unique_users = testData.user.unique()

testData['recommend'] = 0

recommend = []

for i in top_n:
    specific_user = testData[testData['user'] == i]
    for j in top_n[i]: 
        specific_user.loc[specific_user['item'] == j[0], 'recommend'] = 1
    recommend.append(specific_user.recommend.to_list())

# %% Add ratings to DataFrame

import numpy as np

testData['recommend'] = np.array(recommend).flatten()

            
# %% Create CSV

import csv 

users = testData['user'].to_list()
track = testData['item'].to_list()
recommend = testData['recommend'].to_list()

i=0
trackIDCSV = []
for i in range(len(users)): 
    temp = str(users[i]) + '_' + str(track[i])
    trackIDCSV.append(temp)

rows = zip(trackIDCSV, recommend)

with open('SVD.csv', 'w') as f:
    writer = csv.writer(f)
    for row in rows:
        writer.writerow(row)

    
    


