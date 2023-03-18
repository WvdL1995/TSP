from TSPfunctions.functions import *
import numpy as np

data = np.tril(np.random.randint(low=10,high=100,size=[10,10]),-1)
data = data+np.transpose(data)
print(data)
citynames = [line.strip() for line in open('data/citynames.txt','r')]
cities=citynames[0:10]
cities.append(citynames[0])
#print(cities)
print(totaltime(cities,data))