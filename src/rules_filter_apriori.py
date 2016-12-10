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

    $python3 rules_filter_apriori.py <DATASET.csv> <QUERY.csv> <supportvalue>

    DATASET.csv : The file where the rules are searched for.
    QUERY.csv : The file containing all the rules.
    supportvalue : The support value is the threshold support for the rules.
"""

import sys
import numpy as np
import male_female_ratio as r

if(len(sys.argv) > 2):
    in_data = sys.argv[1]
    in_query = sys.argv[2]
    # support = sys.argv[3]
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
             python <filename>.py datafile queryfile support")
valid = []
dic = []
out_file = open("filtered_dataset.csv", 'w')
for query in queries:
    count_male = 0
    count_female = 0
    count = 0
    # ratio = count_male / count_female
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
        # print(ratio)
        if(abs(count_male / count_female - r.male_female_ratio(sys.argv[3])) * 100 <= 6):
            valid.append(("True", query, ratio * 100, count))
            for item in data_items:
                if all(1 if i in item[1:] else 0 for i in query):
                    out_file.write(",".join(item) + "\n")
    #     else:
    #         valid.append("False")
    #     # print(count_male / count_female)
    #     # valid.append(count_male / count_female)
    # else:
    #     valid.append("False")

out_file.close()
# print(valid)
# print(queries)
print()
