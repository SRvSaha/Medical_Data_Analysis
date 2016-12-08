"""
Male:Female Ratio Count in DataSet.

Description : The DataSet has Male and Female candidates.
They are labelled as 1 or 2.Assuming that 1 is Male and 2 is female,
the script helps in finding the Male:Female ratio which is useful
for making decisions in Association Rule Validation obtained by
Apriori Algorithm.

Requirements : 1. Python 3
               2. NumPy
Usage :

    $python3 male_female_ratio.py <DATASET.csv>

    DATASET.csv : The file where the Male/Female are searched for.
"""

import sys
import numpy as np

if(len(sys.argv) > 1):
    in_data = sys.argv[1]
    with open(in_data) as f:
        data_items = []
        for line in f:
            data_items.append(line.strip().split(',')[:-1])
        data_items = np.array(data_items)
else:
    print("Please pass the dataset as argument :\
        $python3 male_female_ratio.py <DATASET.csv>")

count_male = count_female = 0
for item in data_items[:, 0]:
    if(item == '1'):
        count_male += 1
    else:
        count_female += 1
print(count_male / count_female)
