import math
import matplotlib.pyplot as plt

points =  [(1,3) , (2.3 , 3) , (1.5 , 4.2) , (2.6 , 3.9) , (3,3) , (4,2) , (1.4 , 1.4) , (2,2) , (3.5 , 4),
           (7 , 12) , (7,18) , (8.4 , 12.44) , (7.7 , 10) , (10 , 9.4) , (8.8  ,8.8) , (9.2 , 14) , (10,9.8),
           (24.6 , 4) , (25 , 5) , (24.9 , 2.39) , (27,4) , (26.66 , 4.01) , (27,5) , (23.59 , 3.3) , (26.02 , 5.08),
           (5,34) , (5,7.7) , (8,99) , (6,2) , (45,65) , (9,21) ,(9,9.77) ,(45,88) ,(11.5,20),(25,26),(8,0.77),(1,4),
           (23,6) , (6,5.55) , (10.23,0) , (5,8) , (7.7,3.33) , (2,33) , (45,50) , (13,17.8) , (8.8,8.8), (1,85)]

MSE_array = []
k_values = [1,2,3,4,5]

for K in k_values :

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

            updateClusters()
            
            if last_array == clusters_array :

                MSE = 0
                for i , centroid in enumerate(centroid_array) : 
                        MSE += sum([math.dist(centroid , p) for p in clusters_array[i]])

                MSE_array.append(MSE)
                break

            last_array = clusters_array
            updateCentroid()
            clusters_array = []
            for i_ in range(K) : clusters_array.append([]) 

plt.style.use('ggplot')        
plt.plot(k_values , MSE_array , marker = 'o')
plt.xlabel('K')
plt.ylabel('MSE')
plt.show()