#
#   @author      : SRvSaha
#   Filename     : class_drug_separation.py
#   Timestamp    : 05:04 29-December-2016 (Thursday)
#   Description  : Creation of final dataset for drug
#

#!/usr/bin/env python3
"""
Script to create final dataset after removing all duplicate values.

After cross-validation of rules obtained from Apriori Algorithm, the
PROC/DIAG Code is used as feature/attribute. So, if in a record the
PROC code is present we give 1 else 0. It is something like creating
vectors of the most frequently used PROC/DIAG codes.
Also, adding attributes obtained from cross-validated rules from Apriori
Algorithm.

The output file consists of all attributes which is required for input
for Machine Learning.

Requirements : Python3
Run : python3 class_drug_final_format.py <DATASET.csv> <RULES1.csv> <RULES2.csv>
DATASET.csv : Dataset containing opana or butrans class with duplicates.
RULES1.csv : Unique Diag/Proc codes obtained by cross-validation of Apriori
for Butrans.
RULES2.csv : Unique Diag/Proc codes obtained by cross-validation of Apriori
for Opana.
"""

import sys

if len(sys.argv) == 4:
    f_butrans = open("butrans_final_format.csv", 'w')
    butrans = set()
    opana = set()
    f_opana = open("opana_final_format.csv", 'w')
    with open(sys.argv[3], 'r') as f:
        codes_opana = f.readline().strip().split(',')
    with open(sys.argv[2], 'r') as f:
        codes_butrans = f.readline().strip().split(',')
    with open(sys.argv[1]) as f:
        for line in f.readlines()[1:]:
            line_splitted = line.strip().split(',')
            if 'opana' in line_splitted[-1]:
                line = [item for item in line_splitted if item != '']
                # opana.add(','.join(line[:2]) + ',' +
                #           ','.join(line[6:-3]) + '\n')
                opana.add(','.join(line))
            else:
                line = [item for item in line_splitted if item != '']
                # butrans.add(','.join(line[:2]) + ',' +
                #             ','.join(line[6:-3]) + '\n')
                butrans.add(','.join(line))
        butrans = sorted(butrans, key=lambda x: int(x.split(',')[0]))
        opana = sorted(opana, key=lambda x: int(x.split(',')[0]))
    header = 'ENROLL_ID,SEX,AGEGRP,REGION,REFILL_COUNT,ADMTYP,'
    f_butrans.write(header + ','.join(codes_butrans) + ',Class_Drug\n')
    f_opana.write(header + ','.join(codes_opana) + ',Class_Drug\n')
    for record in butrans:
        record = record.split(',')
        # if int(record[-3]) > 5:
        #     print(record[0],record[-3])
        # Adding ENROLL_ID and removing CATAGORY
        output = ','.join(record[:4]) + ',' + record[5] + ',' + record[-3]
        for code in codes_butrans:
            if code in record[6:-3]:
                output += ',1'
            else:
                output += ',0'
        f_butrans.write(output + ',butrans\n')
    for record in opana:
        record = record.split(',')
        # if int(record[-3]) > 5:
        #     print(record[-3])
        output = ','.join(record[:4]) + ',' + record[5] + ',' + record[-3]
        for code in codes_opana:
            if code in record[6:-3]:
                output += ',1'
            else:
                output += ',0'
        f_opana.write(output + ',opana\n')
    f_butrans.close()
    f_opana.close()
    print("Operation Successful :)")
else:
    print("Argument(s) missing.\n\
Please run the code as python3 class_drug_final_format.py DATASET.csv \
RULES.csv")
    sys.exit(1)
