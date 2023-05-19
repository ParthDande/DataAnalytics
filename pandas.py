# -*- coding: utf-8 -*-
"""
Created on Fri May 19 12:01:12 2023

@author: parth
"""
import pandas as pd
import numpy as np
'''
list1=['a','b','c','d','e']
data = np.array(list1)
print("numpy representation is :",data)
s = pd.Series(list1)

print("Pandas representation is :\n",s)
s = pd.Series(data,index = [100,101,102,103,105])
print(s)'''

#import the pandas library and aliasing as pd
'''
syntax for series
pandas.DataFrame(data,index,dtype,copy)
'''
f = np.array(['a','b','c','d','e'])
data = {'a':0,'b':1,'c':2}
s = pd.Series(data)
print(s)

###############
'''
data={'a':0,'b':1,'c':2}
s = pd.Series(data,index = ['b','c','d','e'])
print(s)'''

#Index order is persisted and the msising element 
#is filled with NaN (Not a Number)

##########
'''
s = pd.Series(5,index = [0,1,2,3,4])
print(s)
'''
#If data is a scalar value , an index must be provided
#the value will be repeated to match the length of index