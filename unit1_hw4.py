#!/usr/bin/env python2

colors = [['red', 'green', 'green', 'red' , 'red'],
          ['red', 'red', 'green', 'red', 'red'],
          ['red', 'red', 'green', 'green', 'red'],
          ['red', 'red', 'red', 'red', 'red']]

measurements = ['green', 'green', 'green' ,'green', 'green']


motions = [[0,0],[0,1],[1,0],[1,0],[0,1]]

sensor_right = 0.7

p_move = 0.8

def show(p):
    for i in range(len(p)):
        print p[i]

#DO NOT USE IMPORT
#ENTER CODE BELOW HERE
#ANY CODE ABOVE WILL CAUSE
#HOMEWORK TO BE GRADED
#INCORRECT

if (len(measurements) != len(motions)):
    raise ValueError, "Sizes of motion and measurement vectors should be the same!"

pinit = 1.0 / float(len(colors)) / float(len(colors[0]))
p = [[pinit]*len(colors[0])]*len(colors)

def normalize(p):
    q = []
    s = 0

    for i in range(len(p)):
        s += sum(p[i])

    for i in range(len(p)):
        q.append([])
        for j in range(len(p[i])):
            q[i].append(p[i][j]/s)

    return q


def sense(p, measurement):
    q = []
    for i in range(len(p)):
        q.append([])
        for j in range(len(p[i])):
            hit = (measurement == colors[i][j])
            q[i].append(p[i][j] * (hit * sensor_right + (1-hit) * (1-sensor_right)))

    q = normalize(q)

    return q


# This assumes all moves are of unit length in any direction!
def move(p, motion):
    q = []
    for i in range(len(p)):
        q.append([])
        for j in range(len(p[i])):
            s  = p[(i-motion[0])%len(p)][(j-motion[1])%len(p[i])] * p_move
            s += p[i][j] * (1-p_move)   # Didn't move.
            q[i].append(s)

    return q


for k in range(len(motions)):
    p = move(p, motions[k])
    p = sense(p, measurements[k])


#Your probability array must be printed 
#with the following code.

show(p)

