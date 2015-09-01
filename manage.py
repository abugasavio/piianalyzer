from manager import Manager
from piianalyzer.analyzer import PiiAnalyzer

manager = Manager()


@manager.command
def analyze(filepath):
    """pii analyze a file in a given path <path>. File must be csv file"""
    piianalyzer = PiiAnalyzer(filepath)
    return piianalyzer.analysis()

if __name__ == '__main__':
    manager.main()
