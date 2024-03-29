import sys
import csv
import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor

# to store data
df1 = []

# to store predictions
r1  = []

# take the number of rows
N = int(input())

# build the dataframe
for i in range(N+1):
    df = sys.stdin.readline().strip().split('\t')
    # filter out the empty strings
    df = list(filter(None, df))
    df1.append([str(c) for c in df])

headers = df1.pop(0)
df1 = pd.DataFrame(df1, columns=headers)

# create two dataframes - missing max dataframe and missing min dataframe
df2 = df1[df1['tmax'].str.contains('Missing')]
miss_max = df2.loc[:,df2.columns!='tmax']
df2 = df2.append(df1[df1['tmin'].str.contains('Missing')], ignore_index=True)
miss_min = df1[df1['tmin'].str.contains('Missing')]

miss_min = miss_min.loc[:,miss_min.columns!='tmin']

# drop missing max and min rows
df1 = pd.merge(df1,df2, indicator=True, how='outer').query('_merge=="left_only"').drop('_merge', axis=1)
df1 = df1.reset_index(drop=True)

# convert text of months to digits to avoid error of string to float conversion
d = {'January':1, 'February':2, 'March':3, 'April':4, 'May':5, 'June':6,
     'July':7, 'August':8, 'September':9, 'October':10, 'November':11,'December':12}

df1.month = df1.month.map(d)
miss_max.month = miss_max.month.map(d)
miss_min.month = miss_min.month.map(d)

train = df1
test1 = miss_max
test2 = miss_min

# Linear Regression Model gave the score of 84.33
'''model1 = linear_model.LinearRegression(normalize=True)
model1.fit(train.loc[:,train.columns != 'tmax'],train.loc[:,'tmax'])

for i,j in enumerate(model1.predict(test1)):
    r1.append((test1.index[i],round(j,1)))

model2 = linear_model.LinearRegression(normalize=True)
model2.fit(train.loc[:,train.columns != 'tmin'],train.loc[:,'tmin'])

for i,j in enumerate(model2.predict(test2)):
    r1.append((test2.index[i],round(j,1)))'''

# Random Forest Regression Model gave the score of 86.62
'''rf1 = RandomForestRegressor(n_estimators=100, oob_score=True, random_state=0)
rf1.fit(train.loc[:,train.columns != 'tmax'],train.loc[:,'tmax'])

for i,j in enumerate(rf1.predict(test1)):
    r1.append((test1.index[i],round(j,1)))

rf2 = RandomForestRegressor(n_estimators=100, oob_score=True, random_state=0)
rf2.fit(train.loc[:,train.columns != 'tmin'],train.loc[:,'tmin'])

for i,j in enumerate(rf2.predict(test2)):
    r1.append((test2.index[i],round(j,1)))'''

# Gradient Boosting Regression Model gave the score of 87.42
clf1 = GradientBoostingRegressor(n_estimators=100, learning_rate=0.5, max_depth=2)
clf1.fit(train.loc[:,train.columns != 'tmax'],train.loc[:,'tmax'])

for i,j in enumerate(clf1.predict(test1)):
    r1.append((test1.index[i],round(j,1)))

clf2 = GradientBoostingRegressor(n_estimators=100, learning_rate=0.5, max_depth=2)
clf2.fit(train.loc[:,train.columns != 'tmin'],train.loc[:,'tmin'])

for i,j in enumerate(clf2.predict(test2)):
    r1.append((test2.index[i],round(j,1)))

r1.sort()
for k in range(len(r1)):
    print(r1[k][1])
