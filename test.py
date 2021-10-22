GAP_PENALTY = -1
SAME_AWARD = 1
DIFFERENCE_PENALTY = 0
MAX_SEQ_LENGTH = 1000

def calScore(gen1, gen2):
    total = 0
    for i in range(len(gen1)):
        if gen1[i] == '_' or gen2[i] == '_':
            total += GAP_PENALTY
            continue

        if gen1[i] == gen2[i]:
            total += SAME_AWARD
        else:
            total += DIFFERENCE_PENALTY
    return total


gen1 = 'MAVWLQAGALLVLLVVSSV_STNPGTPQHLCGSHLVDALYLVCGPTGFFYNPKRDVEPLLGFLPPKSAQETEVADFAFKDHAELIR_KRGIVEQCCHKPCSIFELQNYCN__'
gen2 = 'MAPWMHLLTVLALLALWGPNSVQAYSSQHLCGSNLVEALYMTCGRSGF_YRPHDRRE_LED_LQVEQAELGLEAGGLQPSALEMILQKRGIVDQCCNNICTFNQLQNYCNVP'
print(calScore(gen1, gen2))

import sys
print(sys.getrecursionlimit())
