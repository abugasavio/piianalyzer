import pandas as pd
from commonregex import CommonRegex
from nltk.tag.stanford import StanfordNERTagger

# setup parsers
standford_ner = StanfordNERTagger('classifiers/english.conll.4class.distsim.crf.ser.gz')
parser = CommonRegex()


class PiiAnalyzer(object):
    def __init__(self, filepath):
        self.filepath = filepath

    def analysis(self):
        # read and prep the data
        df = pd.read_csv(self.filepath, parse_dates=True).fillna('').to_string(index=False, header=False)
        df2 = ' '.join(df.split())
        s = list(set(i.title() for i in df.split('\n')))

        people = []
        organizations = []
        locations = []

        for title, tag in standford_ner.tag(s):
            if tag == 'PERSON':
                people.append(title)
            if tag == 'LOCATION':
                locations.append(title)
            if tag == 'ORGANIZATION':
                organizations.append(title)

        # TODO: returning dictionary instead of printing

        print '======================================='
        print 'NAMES: COUNT ' + str(len(people))
        print '======================================='
        print list(set(people))
        print '======================================='
        print 'ORGANIZATIONS COUNT ' + str(len(organizations))
        print '======================================='
        print organizations
        print '======================================='
        print 'LOCATIONS COUNT ' + str(len(organizations))
        print '======================================='
        print organizations
        print '======================================='
        print 'EMAILS'
        print '======================================='
        print parser.emails(df2)
        print '======================================='
        print 'PHONE NUMBERS'
        print '======================================='
        print parser.phones(df2)
        print '======================================='
        print 'STREET ADDRESSES'
        print '======================================='
        print parser.street_addresses(df2)
        print '======================================='
        print 'CCs'
        print '======================================='
        print parser.credit_cards(df2)
