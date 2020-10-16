#!/usr/bin/env python
# coding: utf-8

# In[30]:


from __future__ import print_function
from operator import itemgetter
import time
import os


RESULTS = "prediction_weighted_sum.txt"
TEST_SCORES = "test_raw_score.txt"
none_value = 0
album_weight = 0.5
artist_weight = 0.4
genre_weight = 0.2

input_list="testTrack_hierarchy.txt"
def sort_list(input_list):
    sorted_list = []
    

for x in input_list:
    item_count = len(x)
    rat_sum = 0
    counter = 0
    genre_sum = 0
    genre_count = 0

if x[2] >= 0:
    rat_sum = rat_sum + x[2]*album_weight
    counter = counter + 1

if x[3] >= 0:
    rat_sum = rat_sum + x[3]*artist_weight
    counter = counter + 1

for i in range(4,len(x)):
    if x[i] >= 0:
        genre_sum = genre_sum + x[i]
        genre_count = genre_count + 1
    if genre_count > 0:
        genre_sum = genre_sum / genre_count

if genre_count > 0:
    rat_sum = rat_sum + genre_sum*genre_weight
    counter = counter + 1

if counter > 0:
    rat_sum = rat_sum/ counter
    ratings = int(rat_sum)
    sorted_list.append([x[1],ratings])
    sorted_list = sorted(sorted_list, key = itemgetter(1))
    i=0
    pred_dic = {}
for item in sorted_list:
    if i < 3:
        pred_dic[item[0]]=0
    else:
        pred_dic[item[0]]=1
    i += 1
return 	[pred_dic[item[1]] for item in input_list]

def read_lines(file, num):
    lines = []
    line = file.readline()
    lines.append(line)
if line:
    for i in range(1,num):
        lines.append(file.readline())
return lines


start_time = time.time()

with open(RESULTS, "w") as predictionFile:
    with open(TEST_SCORE) as testHierarchy:
        test_list = read_lines(testHierarchy, 6)
while test_list:
    test_list = [item.strip("\n").split("|") for item in test_list]
for i in range(6):
    test_list[i]=[int(item) if item!="None" else none_value for item in test_list[i]]
prediction_result = sort_list(test_list)
for item in prediction_result:
    predictionFile.write(str(item)+"\n")
test_list = read_lines(testHierarchy,6)

print("Finished, spend %.2f s"%(time.time()-start_time))






