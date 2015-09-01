import unicodecsv as csv
from commonregex import CommonRegex
from nltk.tag.stanford import StanfordNERTagger


class PiiAnalyzer(object):
    def __init__(self, filepath):
        self.filepath = filepath
        self.parser = CommonRegex()
        self.standford_ner = StanfordNERTagger('classifiers/english.conll.4class.distsim.crf.ser.gz')

    def analysis(self):
        people = []
        organizations = []
        locations = []
        emails = []
        phone_numbers = []
        street_addresses = []
        credit_cards = []
        ips = []
        data = []

        with open(self.filepath, 'rU') as filedata:
            reader = csv.reader(filedata)

            for row in reader:
                data.extend(row)
                for text in row:
                    emails.extend(self.parser.emails(text))
                    phone_numbers.extend(self.parser.phones("".join(text.split())))
                    street_addresses.extend(self.parser.street_addresses(text))
                    credit_cards.extend(self.parser.credit_cards(text))
                    ips.extend(self.parser.ips(text))

        for title, tag in self.standford_ner.tag(set(data)):
            if tag == 'PERSON':
                people.append(title)
            if tag == 'LOCATION':
                locations.append(title)
            if tag == 'ORGANIZATION':
                organizations.append(title)

        return {'people': people, 'locations': locations, 'organizations': organizations,
                'emails': emails, 'phone_numbers': phone_numbers, 'street_addresses': street_addresses,
                'credit_cards': credit_cards, 'ips': ips
                }
