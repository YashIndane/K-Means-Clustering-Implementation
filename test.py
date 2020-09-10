import math
import matplotlib.pyplot as plt

#centroid = (3.4 , 3.6)
points = [(3 , 9) , (4,4) , (3 , 11) , (10.5 , 11) ,  (6, 7.8) , (2,5) , (19 , 6) , (8 , 5.8), (16 , 4.4) , (21 , 7.2) , (17 , 8) , (20 , 5.2) , (9,11)]

centroid_A = (sum([x[0] for x in points])/len(points) , sum([x[1] for x in points]) / len(points))
centroid_B = (centroid_A[0] + 1 , centroid_A[1] + 1)

#trying to make two clusters
A , B = [] , []

def calculateCentroid() :
    
    global centroid_A , centroid_B 

    centroid_A = (sum([x[0] for x in A]) / len(A) , sum([x[1] for x in A]) / len(A))
    centroid_B = (sum([x[0] for x in B]) / len(B) , sum([x[1] for x in B]) / len(B))


#initial group forming
for p in points : 

    if math.dist(centroid_A , p) >= math.dist(centroid_B , p) : B.append(p)
    else : A.append(p)

calculateCentroid()

last_Bx = [(-1000,-1000)]

for x in range(len(points) * 2):
    
    for p in points : 

         if math.dist(centroid_A , p) >= math.dist(centroid_B , p) : B.append(p)
         else : A.append(p)
    if B == last_Bx :
         print('Clusters are : ')
         break
    last_Bx = B
   
    calculateCentroid()
    A , B = [] , []

print(A)
print(B)


plt.scatter([x[0] for x in points] , [y[1] for y in points])
plt.show()


plt.scatter([x[0] for x in A] , [y[1] for y in A] , c = 'red')
plt.scatter([x[0] for x in B] , [y[1] for y in B] , c = 'green')
plt.show()





