# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PSz70Izp815jhVlmDOooU5Q2ktXSpZ0z
"""

import numpy as np
import seaborn as sns
import pandas as pd

my_lst=[1,2,3,4,5]
arr=np.array(my_lst)

type(arr)

arr

arr.shape

my_lst1=[2,3,4,5,6]
my_lst2=[3,4,5,6,7]
my_lst3=[5,6,7,8,9]

arr=np.array([my_lst1,my_lst2,my_lst3])

arr

arr.shape

arr.reshape(5,3)

arr.shape



"""# ***Indexing***"""

# arr=np.array([1,2,3,4,5,6,7,8,9])

# arr[5]

arr

arr[:,:]

arr[:,3:]

arr[0:2,0:2]

arr[1:,3:]

arr[1:,2:4]

arr[1::3,1:4]

arr=np.arange(0,10)

arr

np.linspace(1,10,50)

arr[3:]=500

arr

arr1=arr

arr

arr1=arr.copy()

print(arr)
arr1[3:0]=1000
print(arr1)

arr1

val=2

arr<val

np.arange(0,10).reshape(5,2)

np.ones((4),dtype=int)

np.ones((2,5),dtype=float)

np.random.rand(3,3)

arr_ex=np.random.rand(4,4)

arr_ex

sns.distplot(pd.DataFrame(arr_ex.reshape(16,1)))

np.random.randint(0,100,9).reshape(3,3)

np.random.random_sample((1,5))

