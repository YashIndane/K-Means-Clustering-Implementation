import math
import matplotlib.pyplot as plt

points =  [(1,3) , (2.3 , 3) , (1.5 , 4.2) , (2.6 , 3.9) , (3,3) , (4,2) , (1.4 , 1.4) , (2,2) , (3.5 , 4),
           (7 , 12) , (7,18) , (8.4 , 12.44) , (7.7 , 10) , (10 , 9.4) , (8.8  ,8.8) , (9.2 , 14) , (10,9.8),
           (24.6 , 4) , (25 , 5) , (24.9 , 2.39) , (27,4) , (26.66 , 4.01) , (27,5) , (23.59 , 3.3) , (26.02 , 5.08)]

K = 3 #No. of clusters
X , Y = sum([x[0] for x in points])/len(points) , sum([y[1] for y in points])/len(points)
centroid_array , clusters_array = [] , []

for i in range(K) : 
    centroid_array.append([X + i + 2, Y + i])
    clusters_array.append([])

def updateCentroid() : 
     
     global centroid_array
     for idx in range(len(centroid_array)) : 
        
          try : 
             centroid_array[idx] = [sum([x_[0] for x_ in clusters_array[idx]])/len(clusters_array[idx]) , 
                                   sum([y_[1] for y_ in clusters_array[idx]])/len(clusters_array[idx])]
          except : pass 

def updateClusters() : 

    global clusters_array

    for p in points : 

        temp = []
        for c in centroid_array : temp.append(math.dist(c , p))
        clusters_array[temp.index(min(temp))].append(p)

updateClusters()
updateCentroid()

last_array = []

for i in range(K) : clusters_array[i] = [] 

for w in range(len(points) * 2) : 

      print(centroid_array)

      updateClusters()
      
      if last_array == clusters_array :

           print('Clusters are : ')
           for c_ in clusters_array : print(c_)
           print(w)
           break

      last_array = clusters_array
      updateCentroid()
      clusters_array = []
      for i_ in range(K) : clusters_array.append([]) 

colors = ['green' , 'red' , 'purple' , 'black' , 'yellow']
for v , cl in enumerate(clusters_array) : 
    plt.scatter([n[0] for n in cl] , [n[1] for n in cl] , c = colors[v])

plt.show()

           






