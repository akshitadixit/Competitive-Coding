import numpy

def result(mat, p):
    #rows
    for x in mat:
        if x == [p, p, p]:
            return 1
    #cols
    for x in numpy.transpose(mat).tolist():
        if x == [p, p, p]:
            return 1
    #diags
    if [mat[x][x] for x in range(3)] == [p, p, p] or [mat[0][2], mat[1][1], mat[2][0]] == [p, p, p]:
        return 1
    return 0

for _ in range(int(input())):
    mat = []
    for x in range(3):
        mat.append([y for y in input()])

    def count(ch):
        ctr = 0
        for x in mat:
            ctr = ctr + x.count(ch)
        return ctr
    
    def check():
        if count('X') > 5 or count('O') > 5:
            return 3
        x = result(mat, 'X')
        o = result(mat, 'O')
        if x == o:
            if x == 1:
            # both are same and both win
                return 3
            elif count('_')%2==1:
            # both are same but there are empty spots left that will make them unequal when the game proceeds
                return 2
            elif x == 0:
                return 2
            return 1
        elif x or o:
            return 1
        return 2

    print(check())