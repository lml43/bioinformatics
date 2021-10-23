from needleman_wunsch import NeedlemanWunsch

from utils import Utils

configFilePath = '../config.txt'
configSection = 'nw-config'

seqFilePath1 = "../data/protein1.fasta"
seqFilePath2 = "../data/protein2.fasta"

SAME_AWARD, DIFFERENCE_PENALTY, GAP_PENALTY, MAX_SEQ_LENGTH = Utils.load_config(configFilePath, configSection)

seq1 = Utils.readGeneFromFile(seqFilePath1)
seq2 = Utils.readGeneFromFile(seqFilePath2)

needleman_wunsch = NeedlemanWunsch(seq1, seq2, SAME_AWARD, DIFFERENCE_PENALTY, GAP_PENALTY)
needleman_wunsch.calculateScoreMatrix()
sequences = needleman_wunsch.generateAlignments()

print(needleman_wunsch.scoreMat[len(seq1)][len(seq2)])
print(len(sequences))
# printMat(arrowMat)
