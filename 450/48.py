'''
spirally traverse a matrix
'''

from unittest import result


def spiral(arr):
    dirs = [(0,1), (1,0), (0,-1), (-1, 0)]
    steps = [len(arr[0]), len(arr)-1]

    dir = 0
    x, y = 0, -1
    result = []

    while steps[dir%2]>0:
        for _ in range(steps[dir%2]):
            x += dirs[dir][0]
            y += dirs[dir][1]
            result.append(arr[x][y])
        steps[dir%2] -= 1
        dir = (dir+1)%4
    return result

