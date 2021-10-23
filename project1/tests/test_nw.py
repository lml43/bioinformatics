import unittest

from project1.main.needleman_wunsch import NeedlemanWunsch


# def calScore(seq1, seq2, GAP_PENALTY, SAME_AWARD, DIFFERENCE_PENALTY):
#     total = 0
#     for i in range(len(seq1)):
#         if seq1[i] == '_' or seq2[i] == '_':
#             total += GAP_PENALTY
#             continue
#
#         if seq1[i] == seq2[i]:
#             total += SAME_AWARD
#         else:
#             total += DIFFERENCE_PENALTY
#     return total


class NeedlemanWunschTest(unittest.TestCase):
    def test_calculate_score_matrix_1(self):
        GAP_PENALTY = -1
        SAME_AWARD = 1
        DIFFERENCE_PENALTY = 0

        seq1 = 'CACGA'
        seq2 = 'CGA'

        needleman_wunsch = NeedlemanWunsch(seq1, seq2, SAME_AWARD, DIFFERENCE_PENALTY, GAP_PENALTY)
        needleman_wunsch.calculateScoreMatrix()

        self.assertEqual(needleman_wunsch.scoreMat[len(seq1)][len(seq2)], 1)

    def test_calculate_score_matrix_2(self):
        GAP_PENALTY = -2
        SAME_AWARD = 2
        DIFFERENCE_PENALTY = -1

        seq1 = 'ACCAGG'
        seq2 = 'GACCA'

        needleman_wunsch = NeedlemanWunsch(seq1, seq2, SAME_AWARD, DIFFERENCE_PENALTY, GAP_PENALTY)
        needleman_wunsch.calculateScoreMatrix()

        self.assertEqual(needleman_wunsch.scoreMat[len(seq1)][len(seq2)], 2)

    def test_calculate_score_matrix_3(self):
        GAP_PENALTY = -1
        SAME_AWARD = 1
        DIFFERENCE_PENALTY = 0

        seq1 = 'MAPWMHLLTVLALLALWGPNSVQAYSSQHLCGSNLVEALYMTCGRSGFYRPHDRRELEDLQVEQAELGLEAGGLQPSALEMILQKRGIVDQCCNNICTFNQLQNYCNVP'
        seq2 = 'MAVWLQAGALLVLLVVSSVSTNPGTPQHLCGSHLVDALYLVCGPTGFFYNPKRDVEPLLGFLPPKSAQETEVADFAFKDHAELIRKRGIVEQCCHKPCSIFELQNYCN'

        needleman_wunsch = NeedlemanWunsch(seq1, seq2, SAME_AWARD, DIFFERENCE_PENALTY, GAP_PENALTY)
        needleman_wunsch.calculateScoreMatrix()

        self.assertEqual(needleman_wunsch.scoreMat[len(seq1)][len(seq2)], 39)

    def test_generate_alignments(self):
        GAP_PENALTY = -1
        SAME_AWARD = 1
        DIFFERENCE_PENALTY = 0

        seq1 = 'MAPWMHLLTVLALLALWGPNSVQAYSSQHLCGSNLVEALYMTCGRSGFYRPHDRRELEDLQVEQAELGLEAGGLQPSALEMILQKRGIVDQCCNNICTFNQLQNYCNVP'
        seq2 = 'MAVWLQAGALLVLLVVSSVSTNPGTPQHLCGSHLVDALYLVCGPTGFFYNPKRDVEPLLGFLPPKSAQETEVADFAFKDHAELIRKRGIVEQCCHKPCSIFELQNYCN'

        needleman_wunsch = NeedlemanWunsch(seq1, seq2, SAME_AWARD, DIFFERENCE_PENALTY, GAP_PENALTY)
        needleman_wunsch.calculateScoreMatrix()
        needleman_wunsch.generateAlignments()

        self.assertEqual(len(needleman_wunsch.lst), 432)


if __name__ == '__main__':
    unittest.main()
