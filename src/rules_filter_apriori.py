#
#   @author      : SRvSaha
#   Filename     : rules_filter_apriori.py
#   Timestamp    : 14:43 11-December-2016 (Sunday)
#   Description  : Cross Validation of Rules obtained by Apriori Algorithm
#

#! /usr/bin/env python3
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

    $python3 rules_filter_apriori.py <DATASET.csv> <QUERY.csv> <DataSetForMaleFemaleRatio.csv>

    DATASET.csv : The file where the rules are searched for.
    QUERY.csv : The file containing all the rules.
    DataSetForMaleFemaleRatio.csv: The file containing ENROLL_ID and SEX to
    remove duplicates and to calculate unique Male : Female Ratio.
"""

import sys
import numpy as np
import male_female_ratio as r

if(len(sys.argv) > 2):
    in_data = sys.argv[1]
    in_query = sys.argv[2]
    with open(in_data) as f:
        data_items = []
        for line in f:
            data_items.append(line.strip().split(',')[:-1])
        data_items = np.array(data_items)
    with open(in_query) as f:
        queries = []
        for line in f:
            queries.append(line.strip().split(','))
        queries = np.array(queries)
else:
    print("Please pass the files as argument :\
             python <filename>.py datafile queryfile enrol_id_sex_file")
valid = []
dic = []
out_file = open("filtered_dataset.csv", 'w')
for query in queries:
    count_male = 0
    count_female = 0
    count = 0
    for item in data_items:
        # print(query, [1 if i in item[1:] else 0 for i in query])
        if all([1 if i in item[1:] else 0 for i in query]):
            count += 1
            if(item[0] == '1'):
                count_male += 1
            else:
                count_female += 1
        # print(count_male, count_female)
    if(count_male != 0 and count_female != 0):
        ratio = count_male / count_female
        if(abs(ratio - r.male_female_ratio(sys.argv[3])) * 100 <= 6):
            valid.append(("True", query, ratio * 100, count))
            for item in data_items:
                if all(1 if i in item[1:] else 0 for i in query):
                    out_file.write(",".join(item) + "\n")

out_file.close()
print("Operation successful :)")
