#
#   @author      : SRvSaha
#   Filename     : accuracy_simple_ensemble.py
#   Timestamp    : 18:26 24-January-2017 (Tuesday)
#   Description  : Calculate % accurate for simple ensembled model on Test Set.
#

"""
To calculate to accuracy obtained by simple ensemble model
when compared with the golden test set of Class Drug Ternary.

INPUT : CSV file with 2 columns : ACTUAL LABELS , ENSEMBLED PREDICTED LABELS
OUTPUT : Accuracy Percentage

To Run : python3 accuracy_simple_ensemble.py <INPUT.csv>
"""

import sys

count_match = total = 0

with open(sys.argv[1]) as f:
    for line in f.readlines()[1:]:
        total += 1
        line = line.strip().split(',')
        if(line[0] == line[1]):
            count_match += 1
    accuracy = count_match / total
    print("Accuracy : ", round(accuracy * 100, 2), "%")
