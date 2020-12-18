#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 18:45:07 2020

@author: jocelynragukonis
"""

# %% Import train data

import pandas as pd

trainData = pd.read_csv('./ee627ws-2020fall/trainIdx2_matrix.txt', 
                        sep='|',
                        names=['UserID','ItemID', 'Rating'],
                        engine='python', 
                        header=None)

# %% Import all track, album, artist, and genre data

albumData = pd.read_csv('./ee627ws-2020fall/albumData2.txt', 
                        sep='|',
                        names=['AlbumID', 'ArtistID', 'GenreID_1', 'GenreID_2', 'GenreID_3', 'GenreID_4', 'GenreID_5', 'GenreID_6', 'GenreID_7', 'GenreID_8', 'GenreID_9', 'GenreID_10', 'GenreID_11', 'GenreID_12', 'GenreID_13', 'GenreID_14', 'GenreID_15', 'GenreID_16', 'GenreID_17', 'GenreID_18', 'GenreID_19', 'GenreID_20', 'GenreID_21'],
                        engine='python', 
                        na_values=['None'],
                        header=None)

artistData = pd.read_csv('./ee627ws-2020fall/artistData2.txt',
                         names=['ArtistID'], 
                         engine='python')

genreData = pd.read_csv('./ee627ws-2020fall/genreData2.txt',
                         names=['GenreID'], 
                         engine='python')

trackData = pd.read_csv('./ee627ws-2020fall/trackData2.txt', 
                        sep='|',
                        names=['TrackID', 'AlbumID', 'ArtistID', 'GenreID_1', 'GenreID_2', 'GenreID_3', 'GenreID_4', 'GenreID_5', 'GenreID_6', 'GenreID_7', 'GenreID_8', 'GenreID_9', 'GenreID_10', 'GenreID_11', 'GenreID_12', 'GenreID_13', 'GenreID_14', 'GenreID_15', 'GenreID_16', 'GenreID_17', 'GenreID_18', 'GenreID_19', 'GenreID_20', 'GenreID_21'],
                        engine='python', 
                        na_values=['None'],
                        header=None)

# %% Classify each item within the training data

items = trainData.ItemID.tolist()
trackIDs = set(trackData.TrackID.tolist())
albumIDs = set(albumData.AlbumID.tolist())
artistIDs = set(artistData.ArtistID.tolist())
genreIDs = set(genreData.GenreID.tolist())

itemType = []

for element in items: 
    if element in trackIDs: 
        itemType.append('Track')
    elif element in albumIDs: 
        itemType.append('Album')
    elif element in artistIDs: 
        itemType.append('Artist')
    elif element in genreIDs: 
        itemType.append('Genre')
    else: 
        print('HELP')
        
# %% Find location of album, artist, and genre ratings within itemType array

albumLocation = [i for i, x in enumerate(itemType) if x == ('Album')]
artistLocation = [i for i, x in enumerate(itemType) if x == ('Artist')]
genreLocation = [i for i, x in enumerate(itemType) if x == ('Genre')]

# %% IDs for album, artists, and genres within the training dataset 

trainAlbumIDs = []
for location in albumLocation: 
    trainAlbumIDs.append(items[location])
    
    
trainArtistIDs = []
for location in artistLocation: 
    trainArtistIDs.append(items[location])
    
trainGenreIDs = []
for location in genreLocation: 
    trainGenreIDs.append(items[location])
    
# %% Find the tracks with each album, artist, and genre within the train set

trainAlbumTrackIDs = []
for ID in trainAlbumIDs:
    trainAlbumTrackIDs.append(trackData.loc[trackData['AlbumID'] == ID, 'TrackID'].to_list())

trainArtistTrackIDs = []
for ID in trainArtistIDs:
    trainArtistTrackIDs.append(trackData.loc[trackData['ArtistID'] == ID, 'TrackID'].to_list())

trainGenreTrackIDs = []
for ID in trainGenreIDs: 
    if trackData.loc[trackData['GenreID_1'] == ID, 'TrackID'].empty == False:
        trainGenreTrackIDs.append(trackData.loc[trackData['GenreID_1'] == ID, 'TrackID'].to_list())
    elif trackData.loc[trackData['GenreID_2'] == ID, 'TrackID'].empty == False:
        trainGenreTrackIDs.append(trackData.loc[trackData['GenreID_2'] == ID, 'TrackID'].to_list())
    elif trackData.loc[trackData['GenreID_3'] == ID, 'TrackID'].empty == False:
        trainGenreTrackIDs.append(trackData.loc[trackData['GenreID_3'] == ID, 'TrackID'].to_list())
    elif trackData.loc[trackData['GenreID_4'] == ID, 'TrackID'].empty == False:
        trainGenreTrackIDs.append(trackData.loc[trackData['GenreID_4'] == ID, 'TrackID'].to_list())
    elif trackData.loc[trackData['GenreID_5'] == ID, 'TrackID'].empty == False:
        trainGenreTrackIDs.append(trackData.loc[trackData['GenreID_5'] == ID, 'TrackID'].to_list())
    elif trackData.loc[trackData['GenreID_6'] == ID, 'TrackID'].empty == False:
        trainGenreTrackIDs.append(trackData.loc[trackData['GenreID_6'] == ID, 'TrackID'].to_list())
    elif trackData.loc[trackData['GenreID_7'] == ID, 'TrackID'].empty == False:
        trainGenreTrackIDs.append(trackData.loc[trackData['GenreID_7'] == ID, 'TrackID'].to_list())
    elif trackData.loc[trackData['GenreID_8'] == ID, 'TrackID'].empty == False:
        trainGenreTrackIDs.append(trackData.loc[trackData['GenreID_8'] == ID, 'TrackID'].to_list())
    elif trackData.loc[trackData['GenreID_9'] == ID, 'TrackID'].empty == False:
        trainGenreTrackIDs.append(trackData.loc[trackData['GenreID_9'] == ID, 'TrackID'].to_list())
    elif trackData.loc[trackData['GenreID_10'] == ID, 'TrackID'].empty == False:
        trainGenreTrackIDs.append(trackData.loc[trackData['GenreID_10'] == ID, 'TrackID'].to_list())
    elif trackData.loc[trackData['GenreID_11'] == ID, 'TrackID'].empty == False:
        trainGenreTrackIDs.append(trackData.loc[trackData['GenreID_11'] == ID, 'TrackID'].to_list())
    elif trackData.loc[trackData['GenreID_12'] == ID, 'TrackID'].empty == False:
        trainGenreTrackIDs.append(trackData.loc[trackData['GenreID_12'] == ID, 'TrackID'].to_list())
    elif trackData.loc[trackData['GenreID_13'] == ID, 'TrackID'].empty == False:
        trainGenreTrackIDs.append(trackData.loc[trackData['GenreID_13'] == ID, 'TrackID'].to_list())
    elif trackData.loc[trackData['GenreID_14'] == ID, 'TrackID'].empty == False:
        trainGenreTrackIDs.append(trackData.loc[trackData['GenreID_14'] == ID, 'TrackID'].to_list())
    elif trackData.loc[trackData['GenreID_15'] == ID, 'TrackID'].empty == False:
        trainGenreTrackIDs.append(trackData.loc[trackData['GenreID_15'] == ID, 'TrackID'].to_list())
    elif trackData.loc[trackData['GenreID_16'] == ID, 'TrackID'].empty == False:
        trainGenreTrackIDs.append(trackData.loc[trackData['GenreID_16'] == ID, 'TrackID'].to_list())
    elif trackData.loc[trackData['GenreID_17'] == ID, 'TrackID'].empty == False:
        trainGenreTrackIDs.append(trackData.loc[trackData['GenreID_17'] == ID, 'TrackID'].to_list())
    elif trackData.loc[trackData['GenreID_18'] == ID, 'TrackID'].empty == False:
        trainGenreTrackIDs.append(trackData.loc[trackData['GenreID_18'] == ID, 'TrackID'].to_list())
    elif trackData.loc[trackData['GenreID_19'] == ID, 'TrackID'].empty == False:
        trainGenreTrackIDs.append(trackData.loc[trackData['GenreID_19'] == ID, 'TrackID'].to_list())
    elif trackData.loc[trackData['GenreID_20'] == ID, 'TrackID'].empty == False:
        trainGenreTrackIDs.append(trackData.loc[trackData['GenreID_20'] == ID, 'TrackID'].to_list())
    elif trackData.loc[trackData['GenreID_21'] == ID, 'TrackID'].empty == False:
        trainGenreTrackIDs.append(trackData.loc[trackData['GenreID_21'] == ID, 'TrackID'].to_list())

# %% Find the ratings per track 

ratings = trainData.Rating.tolist()

# %%  Make new array with all the track ids in order

trainTracks = items

for i in range(len(albumLocation)): 
    trainTracks[albumLocation[i]] = trainAlbumTrackIDs[i]

for i in range(len(artistLocation)):
    trainTracks[artistLocation[i]] = trainArtistTrackIDs[i]
    
for i in range(len(genreLocation)): 
    trainTracks[genreLocation[i]] = trainGenreTrackIDs[i]
    print(i)

# %% sfdkla

data = []

newTrainData = pd.DataFrame(data, columns = ['UserID', 'TrackID', 'Rating'])









     
     
     
     