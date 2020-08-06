"""
__filename__ = "data_analysis.py"
__coursename__ = "SDEV 300 6380 - Building Secure Web Applications (2198)"
__author__ = "John Kucera"
__copyright__ = "None"
__credits__ = ["John Kucera"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "John Kucera"
__email__ = "johnkucera00@gmail.com"
__status__ = "Test"
"""
import statistics
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

class Popchange:
    """
    Class for reading PopChange.csv and constructing desired list
    """
    def __init__(self, line):
        """
        Extract data from PopChange.csv
        """
        self.data = line
        self.id = self.data[0]
        self.geography = self.data[1]
        self.targetgeoid = self.data[2]
        self.targetgeoid2 = self.data[3]
        self.popapr1 = self.data[4]
        self.popjul1 = self.data[5]
        self.changepop = self.data[6]

    def get_popapr1(self):
        """
        Get Pop Apr 1 element
        """
        return self.popapr1

    def get_popjul1(self):
        """
        Get Pop Jul 1 element
        """
        return self.popjul1

    def get_changepop(self):
        """
        Get Change Pop element
        """
        return self.changepop

def read_pop_data():
    """
    Read PopChange.csv file
    """
    popdata = []
    try:
        with open('Week5Deliverables/PopChange.csv', 'r') as file:
            popdf = pd.read_csv(file)
            reader = popdf.values.tolist()
            for line in reader:
                new_popchange_line = Popchange(line)
                popdata.append(new_popchange_line.get_popapr1())
                popdata.append(new_popchange_line.get_popjul1())
                popdata.append(new_popchange_line.get_changepop())
        return popdata
    except FileNotFoundError:
        print('File not found.')

class Housing:
    """
    Class for reading Housing.csv and constructing desired list
    """
    def __init__(self, line):
        """
        Extract data from Housing.csv
        """
        self.data = line
        self.age = self.data[0]
        self.bedrms = self.data[1]
        self.built = self.data[2]
        self.nunits = self.data[3]
        self.rooms = self.data[4]
        self.weight = self.data[5]
        self.utility = self.data[6]

    def get_age(self):
        """
        Get age element
        """
        return self.age

    def get_bedrms(self):
        """
        Get bedrms element
        """
        return self.bedrms

    def get_built(self):
        """
        Get built element
        """
        return self.built

    def get_rooms(self):
        """
        Get rooms element
        """
        return self.rooms

    def get_utility(self):
        """
        Get utility element
        """
        return self.utility

def read_housing_data():
    """
    Read Housing.csv file
    """
    housingdata = []
    try:
        with open('Week5Deliverables/Housing.csv', 'r') as file:
            housingdf = pd.read_csv(file)
            reader = housingdf.values.tolist()
            for line in reader:
                new_housing_line = Housing(line)
                housingdata.append(new_housing_line.get_age())
                housingdata.append(new_housing_line.get_bedrms())
                housingdata.append(new_housing_line.get_built())
                housingdata.append(new_housing_line.get_rooms())
                housingdata.append(new_housing_line.get_utility())
        return housingdata
    except FileNotFoundError:
        print('File not found.')

def main():
    """
    Data Analysis Application main
    """
    # Menu
    print('***** Welcome to the Python Data Analysis App *****')
    is_valid = False
    while not is_valid:
        try:
            selection1 = int(input('Select the file you want to analyze:\n'
                                   '\t1. Population Data\n'
                                   '\t2. Housing Data\n'
                                   '\t3. Exit the Program\n').strip())
        except ValueError:
            print('You must enter 1, 2, or 3. Please try again.')
        else:
            if selection1 >= 1 and selection1 <= 3:
                is_valid = True
                break
            else:
                print('You must enter 1, 2, or 3. Please try again.')

    # Sentinel While loop 1
    while selection1 != 3:

        # File 1
        if selection1 == 1:
            print('You have entered Population Data.')
            is_valid = False
            while not is_valid:
                selection2 = str(input('Select the column you want to analyze:\n'
                                       '\ta. Pop Apr 1\n'
                                       '\tb. Pop Jul 1\n'
                                       '\tc. Change Pop\n'
                                       '\td. Exit Column\n')).lower().strip()
                if selection2 in ['a', 'b', 'c', 'd']:
                    is_valid = True
                    break
                else:
                    print('You must enter a, b, c, or d. Please try again.')

            # Selection a. Pop Apr 1
            if selection2 == 'a':
                new_popdata = read_pop_data()

                # Creating Pop apr 1 list
                popapr1_list = []
                i = 0
                while i < len(new_popdata):
                    popapr1_list.append(new_popdata[i])
                    i += 3

                # Print statistics
                count = len(popapr1_list)
                mean = statistics.mean(popapr1_list)
                sdev = statistics.stdev(popapr1_list)
                minimum = min(popapr1_list)
                maximum = max(popapr1_list)
                print('You selected Pop Apr 1.\n'
                      'The statistics for this column are:\n'
                      '\tCount =', count, '\n', '\tMean =', mean, '\n',
                      '\tStandard Deviation =', sdev, '\n',
                      '\tMin =', minimum, '\n', '\tMax =', maximum, '\n')
                print('Creating image of Histogram... Please wait...\n')

                # Histogram creation
                array = np.asarray(popapr1_list)
                plt.hist(x=array, bins=3000, facecolor='b')
                plt.grid(True)
                fig1 = plt
                fig1.savefig('PopApr1.svg')
                print('The Histogram of this column can be downloaded now.\n')

            # Selection b. Pop Jul 1
            elif selection2 == 'b':
                new_popdata = read_pop_data()

                # Creating Pop jul 1 list
                popjul1_list = []
                i = 1
                while i < len(new_popdata):
                    popjul1_list.append(new_popdata[i])
                    i += 3

                # Print statistics
                count = len(popjul1_list)
                mean = statistics.mean(popjul1_list)
                sdev = statistics.stdev(popjul1_list)
                minimum = min(popjul1_list)
                maximum = max(popjul1_list)
                print('You selected Pop Jul 1.\n'
                      'The statistics for this column are:\n'
                      '\tCount =', count, '\n', '\tMean =', mean, '\n',
                      '\tStandard Deviation =', sdev, '\n',
                      '\tMin =', minimum, '\n', '\tMax =', maximum, '\n')
                print('Creating image of Histogram... Please wait...\n')

                # Histogram creation
                array = np.asarray(popjul1_list)
                plt.hist(x=array, bins=3000, facecolor='b')
                plt.grid(True)
                fig1 = plt
                fig1.savefig('PopJul1.svg')
                print('The Histogram of this column can be downloaded now.\n')

            # Selection c. Change Pop
            elif selection2 == 'c':
                new_popdata = read_pop_data()

                # Creating Change Pop list
                changepop_list = []
                i = 2
                while i < len(new_popdata):
                    changepop_list.append(new_popdata[i])
                    i += 3

                # Print statistics
                count = len(changepop_list)
                mean = statistics.mean(changepop_list)
                sdev = statistics.stdev(changepop_list)
                minimum = min(changepop_list)
                maximum = max(changepop_list)
                print('You selected Change Pop.\n'
                      'The statistics for this column are:\n'
                      '\tCount =', count, '\n', '\tMean =', mean, '\n',
                      '\tStandard Deviation =', sdev, '\n',
                      '\tMin =', minimum, '\n', '\tMax =', maximum, '\n')
                print('Creating image of Histogram... Please wait...\n')

                # Histogram creation
                array = np.asarray(changepop_list)
                plt.hist(x=array, bins=500, facecolor='b')
                plt.grid(True)
                fig1 = plt
                fig1.savefig('ChangePop.svg')
                print('The Histogram of this column can be downloaded now.\n')

            # Selection d. Exit Column
            else:
                print('You selected to exit the column menu.')
                is_valid = False
                while not is_valid:
                    try:
                        selection1 = int(input('Select the file you want to analyze:\n'
                                               '\t1. Population Data\n'
                                               '\t2. Housing Data\n'
                                               '\t3. Exit the Program\n').strip())
                    except ValueError:
                        print('You must enter 1, 2, or 3. Please try again.')
                    else:
                        if selection1 >= 1 and selection1 <= 3:
                            is_valid = True
                            break
                        else:
                            print('You must enter 1, 2, or 3. Please try again.')

        # File 2
        elif selection1 == 2:
            print('You have entered Housing Data.')
            is_valid = False
            while not is_valid:
                selection2 = str(input('Select the column you want to analyze:\n'
                                       '\ta. Age\n'
                                       '\tb. Bedrooms\n'
                                       '\tc. Built Year\n'
                                       '\td. Rooms\n'
                                       '\te. Utility\n'
                                       '\tf. Exit Column\n')).lower().strip()
                if selection2 in ['a', 'b', 'c', 'd', 'e', 'f']:
                    is_valid = True
                    break
                else:
                    print('You must enter a, b, c, d, e, or f. Please try again.')

            # Selection a. Age
            if selection2 == 'a':
                new_housingdata = read_housing_data()

                # Creating Age list
                age_list = []
                i = 0
                while i < len(new_housingdata):
                    age_list.append(new_housingdata[i])
                    i += 5

                # Print statistics
                count = len(age_list)
                mean = statistics.mean(age_list)
                sdev = statistics.stdev(age_list)
                minimum = min(age_list)
                maximum = max(age_list)
                print('You selected Age.\n'
                      'The statistics for this column are:\n'
                      '\tCount =', count, '\n', '\tMean =', mean, '\n',
                      '\tStandard Deviation =', sdev, '\n',
                      '\tMin =', minimum, '\n', '\tMax =', maximum, '\n')
                print('Creating image of Histogram... Please wait...\n')

                # Histogram creation
                array = np.asarray(age_list)
                plt.hist(x=array, facecolor='b')
                plt.grid(True)
                fig1 = plt
                fig1.savefig('Age.svg')
                print('The Histogram of this column can be downloaded now.\n')

            # Selection b. Bedrooms
            elif selection2 == 'b':
                new_housingdata = read_housing_data()

                # Creating Bedrooms list
                bedrms_list = []
                i = 1
                while i < len(new_housingdata):
                    bedrms_list.append(new_housingdata[i])
                    i += 5

                # Print statistics
                count = len(bedrms_list)
                mean = statistics.mean(bedrms_list)
                sdev = statistics.stdev(bedrms_list)
                minimum = min(bedrms_list)
                maximum = max(bedrms_list)
                print('You selected Bedrooms.\n'
                      'The statistics for this column are:\n'
                      '\tCount =', count, '\n', '\tMean =', mean, '\n',
                      '\tStandard Deviation =', sdev, '\n',
                      '\tMin =', minimum, '\n', '\tMax =', maximum, '\n')
                print('Creating image of Histogram... Please wait...\n')

                # Histogram creation
                array = np.asarray(bedrms_list)
                plt.hist(x=array, facecolor='b')
                plt.grid(True)
                fig1 = plt
                fig1.savefig('Bedrooms.svg')
                print('The Histogram of this column can be downloaded now.\n')

            # Selection c. Built year
            elif selection2 == 'c':
                new_housingdata = read_housing_data()

                # Creating Built list
                built_list = []
                i = 2
                while i < len(new_housingdata):
                    built_list.append(new_housingdata[i])
                    i += 5

                # Print statistics
                count = len(built_list)
                mean = statistics.mean(built_list)
                sdev = statistics.stdev(built_list)
                minimum = min(built_list)
                maximum = max(built_list)
                print('You selected Built Year.\n'
                      'The statistics for this column are:\n'
                      '\tCount =', count, '\n', '\tMean =', mean, '\n',
                      '\tStandard Deviation =', sdev, '\n',
                      '\tMin =', minimum, '\n', '\tMax =', maximum, '\n')
                print('Creating image of Histogram... Please wait...\n')

                # Histogram creation
                array = np.asarray(built_list)
                plt.hist(x=array, facecolor='b')
                plt.grid(True)
                fig1 = plt
                fig1.savefig('BuiltYear.svg')
                print('The Histogram of this column can be downloaded now.\n')

            # Selection d. Rooms
            elif selection2 == 'd':
                new_housingdata = read_housing_data()

                # Creating Rooms list
                rooms_list = []
                i = 3
                while i < len(new_housingdata):
                    rooms_list.append(new_housingdata[i])
                    i += 5

                # Print statistics
                count = len(rooms_list)
                mean = statistics.mean(rooms_list)
                sdev = statistics.stdev(rooms_list)
                minimum = min(rooms_list)
                maximum = max(rooms_list)
                print('You selected Rooms.\n'
                      'The statistics for this column are:\n'
                      '\tCount =', count, '\n', '\tMean =', mean, '\n',
                      '\tStandard Deviation =', sdev, '\n',
                      '\tMin =', minimum, '\n', '\tMax =', maximum, '\n')
                print('Creating image of Histogram... Please wait...\n')

                # Histogram creation
                array = np.asarray(rooms_list)
                plt.hist(x=array, facecolor='b')
                plt.grid(True)
                fig1 = plt
                fig1.savefig('Rooms.svg')
                print('The Histogram of this column can be downloaded now.\n')

            # Selection e. Utility
            elif selection2 == 'e':
                new_housingdata = read_housing_data()

                # Creating Utility list
                utility_list = []
                i = 4
                while i < len(new_housingdata):
                    utility_list.append(new_housingdata[i])
                    i += 5

                # Print statistics
                count = len(utility_list)
                mean = statistics.mean(utility_list)
                sdev = statistics.stdev(utility_list)
                minimum = min(utility_list)
                maximum = max(utility_list)
                print('You selected Utility.\n'
                      'The statistics for this column are:\n'
                      '\tCount =', count, '\n', '\tMean =', mean, '\n',
                      '\tStandard Deviation =', sdev, '\n',
                      '\tMin =', minimum, '\n', '\tMax =', maximum, '\n')
                print('Creating image of Histogram... Please wait...\n')

                # Histogram creation
                array = np.asarray(utility_list)
                plt.hist(x=array, facecolor='b')
                plt.grid(True)
                fig1 = plt
                fig1.savefig('Utility.svg')
                print('The Histogram of this column can be downloaded now.\n')

            # Selection f. Exit Column
            else:
                print('You selected to exit the column menu.')
                is_valid = False
                while not is_valid:
                    try:
                        selection1 = int(input('Select the file you want to analyze:\n'
                                               '\t1. Population Data\n'
                                               '\t2. Housing Data\n'
                                               '\t3. Exit the Program\n').strip())
                    except ValueError:
                        print('You must enter 1, 2, or 3. Please try again.')
                    else:
                        if selection1 >= 1 and selection1 <= 3:
                            is_valid = True
                            break
                        else:
                            print('You must enter 1, 2, or 3. Please try again.')

    # Exit program
    print('You selected 3.')
    print('***** Thanks for using the Python Data Analysis App *****')
    return

if __name__ == "__main__":
    main()
