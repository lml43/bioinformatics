DIAG = -1, -1
LEFT = 0, -1
UP = -1, 0


class NeedlemanWunsch:
    def __init__(self, gen1, gen2, SAME_AWARD, DIFF_PENALTY, GAP_PENALTY):
        self.gen1 = gen1
        self.gen2 = gen2
        self.row = len(gen1) + 1
        self.col = len(gen2) + 1
        self.lst = []
        self.SAME_AWARD = SAME_AWARD
        self.DIFF_PENALTY = DIFF_PENALTY
        self.GAP_PENALTY = GAP_PENALTY
        self.scoreMat, self.arrowMat = self.__initMatrix(self.row, self.col)

    def __maximum(self, a, b, c):
        list_el = [a, b, c]
        return max(list_el)

    def __initMatrix(self, row, col):
        scoreMat = [[0 for c in range(col)] for r in range(row)]
        arrowMat = [[[] for c in range(col)] for r in range(row)]
        for i in range(row):
            scoreMat[i][0] = self.GAP_PENALTY * i
            arrowMat[i][0].append(UP)
        for j in range(col):
            scoreMat[0][j] = self.GAP_PENALTY * j
            arrowMat[0][j].append(LEFT)

        arrowMat[0][0] = []

        return scoreMat, arrowMat

    def __calculateScores(self, gen1, gen2, i, j, scoreMat):
        if gen1[i - 1] == gen2[j - 1]:
            diagonal = scoreMat[i - 1][j - 1] + self.SAME_AWARD
        else:
            diagonal = scoreMat[i - 1][j - 1] + self.DIFF_PENALTY
        up = scoreMat[i - 1][j] + self.GAP_PENALTY
        left = scoreMat[i][j - 1] + self.GAP_PENALTY
        return diagonal, left, up

    def __generateArrows(self, diagonal, left, up, max_el):
        arrows = []
        if up == max_el:
            arrows.append(UP)
        if left == max_el:
            arrows.append(LEFT)
        if diagonal == max_el:
            arrows.append(DIAG)
        return arrows

    def __printMat(self, matToPrint):
        for i in range(len(matToPrint)):
            for j in range(len(matToPrint[i])):
                print(matToPrint[i][j], end="\t")
            print()

    def __generateAlignments(self, currentGen1, currentGen2, i, j):
        if i == 0 and j == 0:
            self.lst.append((currentGen1, currentGen2))
            return

        for direction in self.arrowMat[i][j]:
            newGen1 = currentGen1
            newGen2 = currentGen2

            if direction == DIAG:
                newGen1 = self.gen1[i - 1] + currentGen1
                newGen2 = self.gen2[j - 1] + currentGen2

            if direction == LEFT:
                newGen1 = '_' + currentGen1
                newGen2 = self.gen2[j - 1] + currentGen2

            if direction == UP:
                newGen1 = self.gen1[i - 1] + currentGen1
                newGen2 = '_' + currentGen2

            self.__generateAlignments(newGen1, newGen2, i + direction[0], j + direction[1])

    def calculateScoreMatrix(self):
        for i in range(1, self.row):
            for j in range(1, self.col):
                diagonal, left, up = self.__calculateScores(self.gen1, self.gen2, i, j, self.scoreMat)

                max_score = self.__maximum(up, left, diagonal)
                arrows = self.__generateArrows(diagonal, left, up, max_score)

                self.scoreMat[i][j] = max_score
                self.arrowMat[i][j] = arrows

    def generateAlignments(self):
        self.__generateAlignments('', '', self.row - 1, self.col - 1)
        return self.lst
