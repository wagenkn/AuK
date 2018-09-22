import math
import random
import matplotlib.pyplot as plt

def nearestPair(points): # the initializing of the algorithm
    points = sort(points) # sort the points e.g. with Mergesort
    return nearestPairRec(points) # runs the recursive nearestPair algorithm

def nearestPairRec(points):
    # if their are only two points its trivial, just return the two points
    if len(points) == 2:
        return points[0], points[1]
    # if their are three its a bit more difficult, but it is possible two
    # just use the nearestPairOutOfThreePairs function
    if len(points) == 3:
        return nearestPairOutOfThreePairs((points[0],points[1]),(points[0],points[2]),(points[1],points[2]))
    # when their are more then three points
    # -> dividing the points in two halfs
    leftPoints = points[:int(len(points)/2)]
    rightPoints = points[int(len(points)/2):]
    # calculating the position of the midline L (barrier)
    # frp = first right point
    # llp = last left point
    # L = frp - ((frp - llp) / 2)
    barrier = rightPoints[0][0] - ((rightPoints[0][0] - leftPoints[len(leftPoints)-1][0]) / 2)
    # then merge the solved halfs
    return mergePoints(leftPoints, rightPoints, nearestPairRec(leftPoints), nearestPairRec(rightPoints), barrier)

def mergePoints(leftPoints, rightPoints, leftPairNearest, rightPairNearest, barrier):
    points_ = []
    delta = minDistance(leftPairNearest, rightPairNearest) # the maximal distance where points have to be checked during the merge process
    for i in range(0,len(leftPoints)): # checks for all points in the left half wether they are in the distance of delta
        if calcDistance(leftPoints[i], (barrier, leftPoints[i][1])) < delta:
            points_.append(leftPoints[i])
    for i in range(0,len(rightPoints)): # checks for all points in the right half wether they are in the distance of delta
        if calcDistance(rightPoints[i], (barrier, rightPoints[i][1])) < delta:
            points_.append(rightPoints[i])
    if len(points_) == 0: # when their are no points with distance delta or less to the barrier then just return the right or left minimal distance
        if calcDistance(leftPairNearest[0], leftPairNearest[1]) < calcDistance(rightPairNearest[0], rightPairNearest[1]):
            return leftPairNearest
        else:
            return rightPairNearest
    candidatePair = (points_[0], points_[len(points_)-1]) # choose a random candidate
    for i in range(0,len(points_)): # for each combination of points, without the combinations of a point to himself
        for j in range(0,len(points_)):
            if not i == j:
                if calcDistance(points_[i],points[j]) < calcDistance(candidatePair[0],candidatePair[1]): # set the candidate to the candidatePair if its distance is smaller then the actual
                    candidatePair = (points_[i], points_[j])
    return nearestPairOutOfThreePairs(candidatePair, leftPairNearest, rightPairNearest # in the end you have three possibilities of nearestPairs, so do the nearestPairOutOfThreePairs function

def minDistance(p1, p2): # minimal Distance of two pairs
    # if distance of the first pair is smaller then the second
    if calcDistance(p1[0], p1[1]) < calcDistance(p2[0],p2[1]):
        # return the distance of the first
        return calcDistance(p1[0],p1[1])
    else:
        # return the distance of the second
        return calcDistance(p2[0],p2[1])

def calcDistance(point1, point2): #calculate the distance of two points
    a = abs(point1[0] - point2[0])
    b = abs(point1[1] - point2[1])
    c_2 = a * a + b * b # theorem of Pythagoras
    return math.sqrt(c_2)

def nearestPairOutOfThreePairs(pair1, pair2, pair3):
    # first, calc the distance of the pairs
    dist1 = calcDistance(pair1[0], pair1[1])
    dist2 = calcDistance(pair2[0], pair2[1])
    dist3 = calcDistance(pair3[0], pair3[1])
    # figure out the pair with smallest disctance and return it
    if dist1 < dist2 and dist1 < dist3:
        return pair1
    else:
        if dist2 < dist1 and dist2 < dist3:
            return pair2
        else:
            return pair3

def sort(list): #Mergesort
    if len(list) < 2:
        return list
    else:
        lList = list[:int(len(list)/2)] # left List
        rList = list[int(len(list)/2):] # right list
        return merge(sort(lList), sort(rList))

def merge(lList, rList):
    if len(lList) == 0:
        return rList
    if len(rList) == 0:
        return lList
    if lList[0][0] < rList[0][0]:
        result = [lList[0]]
        return  result + merge(lList[1:],rList)
    else:
        result = [rList[0]]
        return result + merge(lList,rList[1:])

points = []
size = 100
numberOfPoints = 10
for i in range(0, numberOfPoints): #random generating points
    points.append((random.uniform(-size,size), random.uniform(-size,size)))

point1, point2 = nearestPair(points) #runs the algorithm

#-----------------------------------------------------
# all about the diagram
#-----------------------------------------------------

fig = plt.subplot()

pointsX = []
pointsY = []

for point in points:
    pointsX.append(point[0])
    pointsY.append(point[1])

fig.plot(pointsX, pointsY, 'bo')
fig.plot(point1[0], point1[1], 'ro')
fig.plot(point2[0], point2[1], 'go')

plt.show()
