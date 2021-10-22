from needleman_wunsch import NeedlemanWunsch
import configparser

# Load config
configFilePath = './config.txt'
configSection = 'nw-config.txt'

configParser = configparser.RawConfigParser()
configParser.read(configFilePath)

GAP_PENALTY = int(configParser.get(configSection, 'GAP_PENALTY'))
SAME_AWARD = int(configParser.get(configSection, 'SAME_AWARD'))
DIFFERENCE_PENALTY = int(configParser.get(configSection, 'DIFFERENCE_PENALTY'))
MAX_SEQ_LENGTH = int(configParser.get(configSection, 'MAX_SEQ_LENGTH'))


def readGeneFromFile(file_name):
    f = open(file_name)
    input = f.read()
    lst = input.split('\n')
    gene = ''
    for str in lst:
        if str[0] != '>':
            gene = gene + str
    return gene

gen1 = readGeneFromFile("./data/protein3.fasta")
gen2 = readGeneFromFile("./data/protein2.fasta")

needleman_wunsch = NeedlemanWunsch(gen1, gen2, SAME_AWARD, DIFFERENCE_PENALTY, GAP_PENALTY)
needleman_wunsch.calculateScoreMatrix()
sequences = needleman_wunsch.generateAlignments()

print(needleman_wunsch.scoreMat[len(gen1)][len(gen2)])
print(len(sequences))
# printMat(arrowMat)
