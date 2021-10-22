GAP_PENALTY = -2
SAME_AWARD = 2
DIFFERENCE_PENALTY = -1
MAX_SEQ_LENGTH = 200


import queue


def readGeneFromFile(file_name):
    f = open(file_name)
    input = f.read()
    lst = input.split('\n')
    gene = ''
    for str in lst:
        if str[0] != '>':
            gene = gene + str
    return gene


# gen1 = readGeneFromFile("./data/M157571.fasta")
# gen2 = readGeneFromFile("./data/M327241.fasta")




class Node:
    def __init__(self):
        self.score = 0
        self.origins = []


def printMat(matToPrint):
    for i in range(len(matToPrint)):
        for j in range(len(matToPrint[i])):
            print(matToPrint[i][j].score, end="\t")
        print()


def maximum(a, b, c):
    list_el = [a, b, c]
    return max(list_el)


def initMatrix(row, col):
    mat = [[Node() for c in range(col)] for r in range(row)]
    for i in range(1, row):
        mat[i][0].score = mat[i - 1][0].score + GAP_PENALTY
        mat[i][0].origins.append(('up', (i - 1, 0)))
    for j in range(1, col):
        mat[0][j].score += mat[0][j - 1].score + GAP_PENALTY
        mat[0][j].origins.append(('left', (0, j - 1)))
    return mat


def generateArrows(i, j, diagonal, left, up, max):
    arrows = []
    if up == max:
        arrows.append(("up", (i - 1, j)))
    if left == max:
        arrows.append(("left", (i, j - 1)))
    if diagonal == max:
        arrows.append(("diagonal", (i - 1, j - 1)))
    return arrows


def calculateScores(gen1, gen2, i, j, mat):
    if gen1[i - 1] == gen2[j - 1]:
        diagonal = mat[i - 1][j - 1].score + SAME_AWARD
    else:
        diagonal = mat[i - 1][j - 1].score + DIFFERENCE_PENALTY
    up = mat[i - 1][j].score + GAP_PENALTY
    left = mat[i][j - 1].score + GAP_PENALTY
    return diagonal, left, up


def createScoreMatrix(gen1, gen2):
    col = len(gen2) + 1
    row = len(gen1) + 1

    matrix = initMatrix(row, col)

    for i in range(1, row):
        for j in range(1, col):
            diagonal, left, up = calculateScores(gen1, gen2, i, j, matrix)

            max_score = maximum(up, left, diagonal)
            arrows = generateArrows(i, j, diagonal, left, up, max_score)

            matrix[i][j].score = max_score
            matrix[i][j].origins = arrows

    return matrix


def generateAlignments(mat, gen1, gen2, currentGen1, currentGen2, currentI, currentJ):
    if currentI == 0 and currentJ == 0:
        lst.append((currentGen1, currentGen2))
        return

    for direction, coordinate in mat[currentI][currentJ].origins:
        newGen1 = currentGen1
        newGen2 = currentGen2

        if direction == 'diagonal':
            newGen1 = gen1[currentI - 1] + currentGen1
            newGen2 = gen2[currentJ - 1] + currentGen2

        if direction == 'left':
            newGen1 = '_' + currentGen1
            newGen2 = gen2[currentJ - 1] + currentGen2

        if direction == 'up':
            newGen1 = gen1[currentI - 1] + currentGen1
            newGen2 = '_' + currentGen2

        generateAlignments(mat, gen1, gen2, newGen1, newGen2, coordinate[0], coordinate[1])


def generateAlignmentsNonRecur(mat, gen1, gen2):
    listGene = []
    qGene = queue.Queue()
    qCoor = queue.Queue()

    qCoor.put((len(gen1), len(gen2)))
    qGene.put(('', ''))

    while not qGene.empty():

        currentGen1, currentGen2 = qGene.get()
        currentI, currentJ = qCoor.get()

        if currentI == 0 and currentJ == 0:
            listGene.append((currentGen1, currentGen2))
            continue

        for direction, coordinate in mat[currentI][currentJ].origins:
            newGen1 = currentGen1
            newGen2 = currentGen2

            if direction == 'diagonal':
                newGen1 = gen1[currentI - 1] + currentGen1
                newGen2 = gen2[currentJ - 1] + currentGen2

            if direction == 'left':
                newGen1 = '_' + currentGen1
                newGen2 = gen2[currentJ - 1] + currentGen2

            if direction == 'up':
                newGen1 = gen1[currentI - 1] + currentGen1
                newGen2 = '_' + currentGen2

            qGene.put((newGen1, newGen2))
            qCoor.put(coordinate)

    return listGene


gen1 = readGeneFromFile("./data/protein1.fasta")
gen2 = readGeneFromFile("./data/protein2.fasta")

# gen1 = 'ACCAGG'
# gen2 = 'GACCA'
# gen1 = 'CACGA'
# gen2 = 'CGA'

subGen1 = gen1[:MAX_SEQ_LENGTH]
subGen2 = gen2[:MAX_SEQ_LENGTH]

lst = []
mat = createScoreMatrix(subGen2, subGen1)
generateAlignments(mat, subGen2, subGen1, '', '', len(subGen2), len(subGen1))

print(mat[len(subGen2)][len(subGen1)].score)
print(len(lst))

#
# list2 = generateAlignmentsNonRecur(mat, gen2, gen1)
# print(len(list2))
# print(len(subGen1), len(subGen2))
