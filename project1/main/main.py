from needleman_wunsch import NeedlemanWunsch
from utils import Utils
import sys

# configFilePath = './conf/config.txt'
# configSection = 'nw-config'
#
# seqFilePath1 = "./data/protein1.fasta"
# seqFilePath2 = "./data/protein2.fasta"

configFilePath = sys.argv[1]
configSection = 'nw-config'

seqFilePath1 = sys.argv[2]
seqFilePath2 = sys.argv[3]


def print_result(scoreMat, sequences, row, col):
    f = open('out.txt', 'w')
    f.write('SCORE = {}'.format(scoreMat[row][col]))
    f.write('\n\nTOTAL = {}'.format(len(sequences)))
    for s1, s2 in sequences:
        line = '\n\n{}\n{}'.format(s1, s2)
        f.write(line)
    print()
    print('--- Generated sequence alignments in out.txt! ---')
    print()


def main():
    SAME_AWARD, DIFFERENCE_PENALTY, GAP_PENALTY, MAX_SEQ_LENGTH = Utils.load_config(configFilePath, configSection)

    seq1 = Utils.readFromFile(seqFilePath1, MAX_SEQ_LENGTH)
    seq2 = Utils.readFromFile(seqFilePath2, MAX_SEQ_LENGTH)

    needleman_wunsch = NeedlemanWunsch(seq1, seq2, SAME_AWARD, DIFFERENCE_PENALTY, GAP_PENALTY)
    needleman_wunsch.calculateScoreMatrix()
    sequences = needleman_wunsch.generateAlignments()

    print_result(needleman_wunsch.scoreMat, sequences, len(seq1), len(seq2))


main()
