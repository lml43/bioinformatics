
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


def createScoreMatrix(gen1, gen2):
    col = len(gen2) + 1
    row = len(gen1) + 1
    
    mat = [[Node() for c in range(col)] for r in range(row)]

    for i in range(1, row):
        mat[i][0].score = mat[i-1][0].score + GAP_PENALTY
        mat[i][0].origins.append(('up', (i-1, 0)))

    for j in range(1, col):
        mat[0][j].score += mat[0][j-1].score + GAP_PENALTY
        mat[0][j].origins.append(('left', (0, j-1)))

    for i in range(1, row):
        for j in  range(1, col):
            if gen1[ i -1] == gen2[ j -1]:
                diagonal = mat[ i -1][ j -1].score + SAME_AWARD
            else:
                diagonal = mat[ i -1][ j -1].score + DIFFERENCE_PENALTY

            up = mat[ i -1][j].score + GAP_PENALTY
            left = mat[i][ j -1].score + GAP_PENALTY

            max = maximum(up, left, diagonal)
            arrows = []

            if up == max:
                arrows.append(("up", ( i -1, j)))

            if left == max:
                arrows.append(("left", (i, j- 1)))

            if diagonal == max:
                arrows.append(("diagonal", (i - 1, j - 1)))

            mat[i][j].score = max
            mat[i][j].origins = arrows

    return mat


lst = []


def generateAlignments(mat, gen1, gen2, currentGen1, currentGen2, currentI, currentJ):
    if currentI == 0 and currentJ == 0:
        lst.append((currentGen1, currentGen2))
        return

    for direction, coordinate in mat[currentI][currentJ].origins:
        newGen1 = currentGen1
        newGen2 = currentGen2

        if direction == 'diagonal':
            newGen1 = gen1[currentI-1] + currentGen1
            newGen2 = gen2[currentJ-1] + currentGen2

        if direction == 'left':
            newGen1 = '_' + currentGen1
            newGen2 = gen2[currentJ-1] + currentGen2

        if direction == 'up':
            newGen1 = gen1[currentI-1] + currentGen1
            newGen2 = '_' + currentGen2

        generateAlignments(mat, gen1, gen2, newGen1, newGen2, coordinate[0], coordinate[1])


mat = createScoreMatrix(gen2, gen1)
generateAlignments(mat, gen2, gen1, '', '', len(gen2), len(gen1))
print(lst)