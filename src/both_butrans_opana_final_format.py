#
#   @author      : SRvSaha
#   Filename     : class_drug_separation.py
#   Timestamp    : 05:04 29-December-2016 (Thursday)
#   Description  : Creation of final dataset for both_butrans_and_opana
#

#!/usr/bin/env python3
"""
Script to create final formatted dataset containing frequently used codes (DX/PX)

After cross-validation of rules obtained from Apriori Algorithm, the
PROC/DIAG Code is used as feature/attribute. So, if in a record the
PROC code is present we give 1 else 0. It is something like creating
vectors of the most frequently used PROC/DIAG codes.
Also, adding attributes obtained from cross-validated rules from Apriori
Algorithm.

The output file consists of all attributes which is required for input
for Machine Learning.

Requirements : Python3
Run : python3 class_drug_final_format.py <DATASET.csv> <RULES1.csv>
DATASET.csv : Dataset containing opana_and_butrans class with duplicates.
RULES1.csv : Unique Diag/Proc codes obtained by cross-validation of Apriori
for Butrans.
RULES2.csv : Unique Diag/Proc codes obtained by cross-validation of Apriori
for Opana.
"""

import sys

if len(sys.argv) == 3:
    f_out = open("both_butrans_opana_final_format.csv", 'w')
    output = set()
    with open(sys.argv[2], 'r') as f:
        codes_both = f.readline().strip().split(',')
    with open(sys.argv[1]) as f:
        for line in f.readlines()[1:]:
            line_splitted = line.strip().split(',')
            line = [item for item in line_splitted if item != '']
            output.add(','.join(line))
        output = sorted(output, key=lambda x: int(x.split(',')[0]))
    header = 'ENROLL_ID,SEX,AGEGRP,REGION,REFILL_COUNT,ADMTYP,'
    # header = 'SEX,AGEGRP,REGION,REFILL_COUNT,ADMTYP,'
    f_out.write(header + ','.join(codes_both) + ',Class_Drug\n')
    # print(header + ','.join(codes_both) + ',Class_Drug\n')
    for record in output:
        record = record.split(',')
        output = record[0] + ',' + ','.join(record[-3:-6:-1]) + ',' + record[-1] + ',' + record[-6]
        for code in codes_both:
            if code in record[1:-6]:
                output += ',1'
            else:
                output += ',0'
        f_out.write(output + ',both\n')
    f_out.close()
    print("Operation Successful :)")
else:
    print("Argument(s) missing.\n\
Please run the code as python3 class_drug_final_format.py DATASET.csv \
RULES.csv")
    sys.exit(1)
