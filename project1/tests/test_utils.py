import unittest

from project1.main.utils import Utils


class MyTestCase(unittest.TestCase):
    def test_load_config(self):
        configFilePath = './conf/config_test.txt'
        configSection = 'nw-config'

        SAME_AWARD, DIFFERENCE_PENALTY, GAP_PENALTY, MAX_SEQ_LENGTH = Utils.load_config(configFilePath, configSection)

        self.assertEqual(SAME_AWARD, 5)
        self.assertEqual(MAX_SEQ_LENGTH, 100)

    def test_load_config_error(self):
        configFilePath = './conf/config_test.txt'
        configSection = 'nw-config-error'

        with self.assertRaises(ValueError):
            Utils.load_config(configFilePath, configSection)

    def test_read_file(self):
        MAX_SEQ_LENGTH = 200
        filePath = './data/protein3.fasta'

        seq = Utils.readFromFile(filePath, MAX_SEQ_LENGTH)
        self.assertGreater(len(seq), 0)

    def test_read_long_seq(self):
        MAX_SEQ_LENGTH = 100
        filePath = './data/protein3.fasta'

        with self.assertRaisesRegex(AssertionError, 'The sequence should not longer than 100 characters'):
            Utils.readFromFile(filePath, MAX_SEQ_LENGTH)


if __name__ == '__main__':
    unittest.main()
