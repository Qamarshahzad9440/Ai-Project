# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NDgAqr2rJ0LV0YNrVR4K49_O-zuWsvOQ
"""

!git clone https://github.com/krishnaik06/Ineuron-ANN.git

import tensorflow

from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.models import Sequential
from tensorflow import keras
# from tensorflow.keras.optimizers import Adam

model=Sequential()

model.add(Dense(units=10,activation='relu',input_dim=2))
model.add(Dropout(0.5))
model.add(Dense(units=62,activation='relu'))
model.add(Dropout(0.6))
model.add(Dense(units=12,activation='relu'))
model.add(Dropout(0.7))
model.add(Dense(units=1,activation='sigmoid'))

model.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

model.summary()

import numpy as np
import pandas as pd

df=pd.DataFrame(data={'col1': [1, 2,3,4,5,6], 'col2': [3, 4,5,6,7,8],'output':[0,0,0,1,1,1]})

x=df.drop(labels=['output'],axis=1)
# y=np.array([1,0,1,1,1,0])
y=df['output']

model.fit(x=x,y=y,epochs=100)

