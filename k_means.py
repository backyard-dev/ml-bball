import pandas as pd
import numpy as np
import scipy as sc
from scipy import spatial as sp
import matplotlib.pyplot as plt

MALE = 0
FEMALE = 1
CLUSTERS = 2


def change_string(gender):
    if (gender == 'Male'):
        return MALE
    return FEMALE


def distance(point_one, point_two):
    return sp.distance.cityblock(point_one,point_two)
    

def update_clusters(k_means, num_clusters):
    to_return = []
    for i in range(num_clusters):
        to_return.append(mean_points(k_means[i]))



    return to_return

def mean_points(tuple_list):
    total = len(tuple_list)
    
    if (len(tuple_list) != 0):    
        temp = list(tuple_list[0])
        temp_list = tuple_list
        temp_list.pop(0)

        for tup in temp_list:
            for i in range(len(tup)):
                temp[i] += tup[i]
        for i in range(len(temp)):
            temp[i] = temp[i]/total
        return tuple(temp)
    return ()



df = pd.read_csv('Mall_Customers.csv')
df_poke = pd.read_csv('Pokemon.csv')

df['Gender'] = df['Gender'].apply(change_string)




clust = []

for i in range(CLUSTERS):
    temp = np.random.rand(2,1)*10
    temp = tuple(map(tuple, temp))
    clust.append(temp)


    


k_means  = {0:[],1:[]}


print(clust)
for iter in range(100):
    k_means  = {0:[],1:[]}
    for (age,score) in zip(df_poke['V1'], df_poke['V2']):
        tup = (age,score)
        
        temp = []
        for i in range(CLUSTERS):
            
            temp.append(distance(tup,clust[i]))

        minpos = temp.index(max(temp))

        k_means[minpos].append(tup)
    
    clust = update_clusters(k_means,CLUSTERS)





print(k_means)
print(clust)


    

    











#print(k_means)



plt.scatter(df_poke['V1'], df_poke['V2'])
plt.show()


