

GAP_PENALTY = -2
SAME_AWARD = 2
DIFFERENCE_PENALTY = -1
MAX_SEQ_LENGTH = 1000

gen1 = 'ACCAGG'
gen2 = 'GACCA'
# gen1 = 'CACGA'
# gen2 = 'CGA'

class Node:
    def __init__(self):
        self.score = 0
        self.origins = []


def printMat(mat):
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            print(mat[i][j].score, end="\t")
        print()


def maximum(a, b, c):
    list = [a, b, c]
    return max(list)


def recreateAlignment(gen1, gen2):
    col = len(gen2) + 1
    row = len(gen1) + 1
    
    mat = [[Node() for c in range(col)] for r in range(row)]

    for i in range(1, row):
        mat[i][0].score = mat[i-1][0].score + GAP_PENALTY

    for j in range(1, col):
        mat[0][j].score += mat[0][j-1].score + GAP_PENALTY

    for i in range(1, row):
        for j in  range(1, col):
            if gen1[i-1] == gen2[j-1]:
                diagonal = mat[i-1][j-1].score + SAME_AWARD
            else:
                diagonal = mat[i-1][j-1].score + DIFFERENCE_PENALTY

            up = mat[i-1][j].score + GAP_PENALTY
            left = mat[i][j-1].score + GAP_PENALTY

            max = maximum(up, left, diagonal)
            arrows = []

            if up == max:
                arrows.append((i-1, j))

            if left == max:
                arrows.append((i, j-1))

            if diagonal == max:
                arrows.append((i-1, j-1))

            mat[i][j].score = max
            mat[i][j].origins = arrows

    printMat(mat)



recreateAlignment(gen2, gen1)