# -*- coding: utf-8 -*-
"""
Created on Sat May 20 11:23:22 2023

@author: parth
"""

import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randn(10,2),index= pd.date_range('1/1/2000',periods= 10),columns= list(['A','B']))
print(df)
df.plot()
df.plot.bar()
#.randn fuction gives negative values as well
import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.rand(10,4),columns= list(['A','B','C','D']))
print(df)
df.plot()
df.plot.bar()
#if we use np.random.randn() we will aslo get negative data while the .rand() function will give us the positve random data

import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.rand(10,4),columns= list(['A','B','C','D']))
print(df)
df.plot.bar(stacked= True)
my_color = ['Red','Orange','yellow','Purple']
#to represent data horizontally
df.plot.barh(stacked= True, color = my_color)

###histogram
df = pd.DataFrame({'a':np.random.randn(1000)+1,'b':np.random.rand(1000)+1,'c':np.random.randn(1000)-1},columns = ['a','b','c'])
print(df)
df.plot.hist(bins = 20)

###to make a box graph
df = pd.DataFrame(np.random.rand(10,5),columns = ['A','B','C','D','E'])
print(df)
df.plot.box()


# to make a area graph

df = pd.DataFrame(np.random.rand(10,5),columns = ['A','B','C','D','E'])
print(df)
df.plot.area()

#### to make a scatter plot
df = pd.DataFrame(np.random.rand(50,4),columns = ['a','b','c','d'])
print(df)
df.plot.scatter(x = 'a',y ='b')
