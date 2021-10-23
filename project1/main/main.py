from needleman_wunsch import NeedlemanWunsch
from utils import Utils

configFilePath = '../conf/config.txt'
configSection = 'nw-config'

seqFilePath1 = "../data/protein1.fasta"
seqFilePath2 = "../data/protein2.fasta"


def print_result(scoreMat, sequences, row, col):
    print('SCORE = {}'.format(scoreMat[row][col]))
    for s1, s2 in sequences:
        print()
        print(s1)
        print(s2)


def main():
    SAME_AWARD, DIFFERENCE_PENALTY, GAP_PENALTY, MAX_SEQ_LENGTH = Utils.load_config(configFilePath, configSection)

    seq1 = Utils.readFromFile(seqFilePath1, MAX_SEQ_LENGTH)
    seq2 = Utils.readFromFile(seqFilePath2, MAX_SEQ_LENGTH)

    needleman_wunsch = NeedlemanWunsch(seq1, seq2, SAME_AWARD, DIFFERENCE_PENALTY, GAP_PENALTY)
    needleman_wunsch.calculateScoreMatrix()
    sequences = needleman_wunsch.generateAlignments()

    print_result(needleman_wunsch.scoreMat, sequences, len(seq1), len(seq2))


main()
