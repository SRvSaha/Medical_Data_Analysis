#
#   @author      : SRvSaha
#   Filename     : rules_filter_apriori.py
#   Timestamp    : 14:43 11-December-2016 (Sunday)
#   Description  : Cross Validation of Rules obtained by Apriori Algorithm
#

"""
Frequent Item Set Rule cross-checking.

Description : The rules obtained using Apriori Algorithm and Association Rules
by suitable support and confidence score are then cross-checked with
the dataset using the M:F ratio from the dataset where the rule is followed.
This cross-validation is helps in checking whether the rule actually reflects
our dataset or not.

Requirements : 1. Python 3
               2. NumPy
Usage :

    $python3 rules_filter_apriori.py <DATASET.csv> <QUERY.csv>
     <DataSetForMaleFemaleRatio.csv>

    DATASET.csv : The file where the rules are searched for. This file contains
    SEX, DX, PX
    QUERY.csv : The file containing all the rules.
    DataSetForMaleFemaleRatio.csv: The file containing ENROLL_ID and SEX to
    remove duplicates and to calculate unique Male : Female Ratio.
"""

import sys
import numpy as np
import male_female_ratio as r   # The module created for male:female ratio

if(len(sys.argv) > 3):
    # DATASET as the first argument : SEX<tab>DX1-DX15<tab>PROC1-PROC15
    in_data = sys.argv[1]
    # RULES obtained from Apriori Algorithm as second argument
    in_query = sys.argv[2]
    # Opening and the DATASET for reading and the closing it once done.
    with open(in_data) as f:
        # As it is computationally expensive to append into numpy array, so
        # temporary list called data_items is used to store the values read
        # from file and then convert it to numpy array finally.
        data_items = []
        for line in f:
            # Till last element as the last element is ''
            # which is of no use for us.
            # data_items will be list of list.
            data_items.append(line.strip().split(',')[:-1])
        # Converting list to numpy array and assigning name data_items to it.
        data_items = np.array(data_items)
    with open(in_query) as f:
        queries = []
        for line in f:
            # All the rules are appended one-by-one to queries
            queries.append(line.strip().split(','))
        # Converting list to numpy array for faster access.
        queries = np.array(queries)
# If some arguments are missing then exit
else:
    print("Please pass the files as argument :\
        python <filename>.py datafile queryfile enrol_id_sex_file")
    sys.exit(1)
# Lists for storing temporary data
valid = []
dic = []
# out_file is the output file.
out_file = open("both_butrans_opana_frequent_dataset.csv", 'w')
for query in queries:
    # For every rule/query, male and female count are resetted to 0
    count_male = 0
    count_female = 0
    # Count is to check how many results are retrieved.
    count = 0
    for item in data_items:
        # print(query, [1 if i in item[1:] else 0 for i in query])
        # For every value in query if the value is also present in the
        # item i.e in the current row of the numpy 2D array, then we increment
        # count by 1 as the rule is found in the dataset. If a single value
        # from query is not there in the row, the all() gets false.
        if all([1 if i in item[1:] else 0 for i in query]):
            count += 1
            # Considering SEX = '1' as MALE, increment if male is found
            if(item[0] == '1'):
                count_male += 1
            else:
                count_female += 1
        # print(count_male, count_female)
    # Checking if both non-zero is important as there are many cases where
    # rule is not found in dataset.
    if(count_male != 0 and count_female != 0):
        ratio = count_male / count_female
        # query = ','.join(query[:-1]) + \
        # ' => ' + str(query[-1])
        # valid.append((query, ratio * 100))
        # 3rd argument is sex_enrol_id file to calculate male_female_ratio
        # through the module imported as r
        # 8.5% is the overall error acceptable
        if(abs(ratio - r.male_female_ratio(sys.argv[3])) * 100 <= 10):
            valid.append((query, ratio * 100))
            for item in data_items:
                # For creating csv file from numpy array for which rule matched
                # the original male:female ratio in dataset.
                if all(1 if i in item[1:] else 0 for i in query):
                    out_file.write(",".join(item) + "\n")
# Closing output file
out_file.close()
# Uncomment the next line to check the resulting rules.
# print(valid)
for item in valid:
    print(item)
print("Operation successful :)")
