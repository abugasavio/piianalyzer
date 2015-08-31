import os
from piianalyzer.analyzer import PiiAnalyzer


class TestPiiAnalyzer:
    def test_analysis(self):
        analysis = PiiAnalyzer(os.path.abspath('tests/files/titanic_data.csv')).analysis()
        assert ('Nelson' in analysis['people']) == True
        assert ('William' in analysis['people']) == True

    def test_analysis_csv_with_unicode(self):
        analysis = PiiAnalyzer(os.path.abspath('tests/files/titanic_data_with_unicode.csv')).analysis()
        assert ('Nelson' in analysis['people']) == True

    def test_phone_numbers_with_spaces(self):
        # now works with phone numbers with a spaces, e.g., 0796 477 389
        analysis = PiiAnalyzer(os.path.abspath('tests/files/pii.csv')).analysis()
        assert ('0796477389' in analysis['phone_numbers']) == True

