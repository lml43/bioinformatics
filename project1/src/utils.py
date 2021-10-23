import configparser



class Utils:
    @staticmethod
    def load_config(configFilePath, configSection):
        configParser = configparser.RawConfigParser()
        configParser.read(configFilePath)
        GAP_PENALTY = int(configParser.get(configSection, 'GAP_PENALTY'))
        SAME_AWARD = int(configParser.get(configSection, 'SAME_AWARD'))
        DIFFERENCE_PENALTY = int(configParser.get(configSection, 'DIFFERENCE_PENALTY'))
        MAX_SEQ_LENGTH = int(configParser.get(configSection, 'MAX_SEQ_LENGTH'))
        return SAME_AWARD, DIFFERENCE_PENALTY, GAP_PENALTY, MAX_SEQ_LENGTH

    @staticmethod
    def readGeneFromFile(file_name):
        f = open(file_name)
        input_file = f.read()
        lst = input_file.split('\n')
        seq = ''
        for str in lst:
            if str[0] != '>':
                seq = seq + str
        return seq
