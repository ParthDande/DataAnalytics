# -*- coding: utf-8 -*-
"""
Created on Fri May 19 15:04:44 2023

@author: parth
"""

#working in pandas dataframe
#data frmae consists of rows and columns
'''
each column stores a specific type of data
pandas.DataFrame(data,index,column,dtype,copy)
'''
import pandas as pd
df = pd.DataFrame()
print(df)

'''
data = [1,2,3,4,5]
df= pd.DataFrame(data,)
sf = pd.Series(data)
print(df)
print(sf)
'''

##################
'''
data = [['alex',10],['Bob',12],['Clarke',13]]
df = pd.DataFrame(data,columns=['name','age'])
print(df)
'''
'''
df= pd.read_csv("IPL_Matches_2008_2022.csv")
pd.dropna(df)
print(df)
'''
'''
#we can combine 2 series in the dataframe and make them one
d = {'one':pd.Series([1,2,3],index = ['a','b','c']),'two':pd.Series([1,2,3,4],index=['a','b','c','d'])}
df = pd.DataFrame(d)
print(df)


#we can print only one specific column form the dataframe
d = {'one':pd.Series([1,2,3],index = ['a','b','c']),'two':pd.Series([1,2,3,4],index=['a','b','c','d'])}
df = pd.DataFrame(d)
print(df['one'])

#importing a new column to a existing dataframe
d = {'one':pd.Series([1,2,3],index = ['a','b','c']),'two':pd.Series([1,2,3,4],index=['a','b','c','d'])}
df = pd.DataFrame(d)
df['three']=pd.Series([10,20,30],index=['a','b','c'])
df['four']=df['one']+df['three']
print(df)

'''


####
'''
#importing a new column to a existing dataframe
d = {'one':pd.Series([1,2,3],index = ['a','b','c']),'two':pd.Series([1,2,3,4],index=['a','b','c','d'])}
df = pd.DataFrame(d)
df['three']=pd.Series([10,20,30],index=['a','b','c'])
df['four']=df['one']+df['three']
print("the series Representation is: ")
print(df)

#to delete a column we can use a del keyword
print("The dataFrame after deleteing using the del object")
del df['one']
print(df)

#deleting using the pop function 
print("THe dataframe after deleting using the pop function")
df.pop('two')
print(df)

'''