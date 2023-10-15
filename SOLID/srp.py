#before refactoring
class DataProcessor:
    def __init__(self, filename):
        self.filename = filename

    def read_data(self):
        # Code to read data from the file
        pass

    def analyze_data(self):
        # Code to perform data analysis
        pass

#after refactoring
class DataReader:
    def __init__(self, filename):
        self.filename = filename

    def read_data(self):
        # Code to read data from the file
        pass

class DataAnalyzer:
    def __init__(self, data):
        self.data = data

    def analyze_data(self):
        # Code to perform data analysis
        pass
