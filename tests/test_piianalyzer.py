import os
from piianalyzer.analyzer import PiiAnalyzer


class TestPiiAnalyzer:
    def test_analysis(self):
        analysis = PiiAnalyzer(os.path.abspath('tests/files/titanic_data.csv')).analysis()
        assert ('Nelson' in analysis['people']) == True
