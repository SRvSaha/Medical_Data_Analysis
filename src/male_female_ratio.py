"""
Male:Female Ratio Count in DataSet.

Description : The DataSet has Male and Female candidates.
They are labeled as 1 or 2.Assuming that 1 is Male and 2 is female,
the script helps in finding the Male:Female ratio which is useful
for making decisions in Association Rule Validation obtained by
Apriori Algorithm.

Requirements : 1. Python 3

Usage :

    $python3 male_female_ratio.py <DATASET.csv>

    DATASET.csv : The file where the Male/Female are searched for.
"""

import sys


def male_female_ratio(in_file):
    """
    The function finds the male:female ratio in the dataset.

    The duplicate values of Enroll ID are removed from it after
    that the value of the male:female is calculated.

    """
    with open(in_file) as f:
        data_items = {}
        for line in f:
            list = line.strip().split(',')
            if list[0] not in data_items.keys():
                data_items[list[0]] = list[1]

    count_male = count_female = 0
    for item in data_items.values():
        if(item == '1'):
            count_male += 1
        else:
            count_female += 1
    return count_male / count_female

if __name__ == '__main__':
    print(male_female_ratio(sys.argv[1]))
