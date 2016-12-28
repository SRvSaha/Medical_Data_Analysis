#
#   @author      : SRvSaha
#   Filename     : class_drug_separation.py
#   Timestamp    : 15:08 28-December-2016 (Wednesday)
#   Description  : Separation of Butrans and Opana drugs in 2 separate files
#

"""
Separation of Class Drugs into different files by removing duplicates and
spaces.

The script separates butrans and opana drug in two different files after
removing the duplicates based on ENROL_ID.
The output file consists of ENROL_ID SEX Dx and Px with all the spaces removed.

Requirements : Python3
Run : python3 class_drug_separation.py <DATASET.csv>
DATASET.csv : Dataset containing both opana and butrans class.
"""

import sys

if len(sys.argv) == 2:
    f_butrans = open("butrans_apriori.csv", 'w')
    butrans = set()
    opana = set()
    f_opana = open("opana_apriori.csv", 'w')
    with open(sys.argv[1]) as f:
        for line in f.readlines()[1:]:
            line_splitted = line.strip().split(',')
            if 'opana' in line_splitted[-1]:
                line = [item for item in line_splitted if item != '']
                opana.add(','.join(line[:2]) + ',' +
                          ','.join(line[6:-3]) + '\n')
            else:
                line = [item for item in line_splitted if item != '']
                butrans.add(','.join(line[:2]) + ',' +
                            ','.join(line[6:-3]) + '\n')
        butrans = sorted(butrans, key=lambda x: int(x.split(',')[0]))
        opana = sorted(opana, key=lambda x: int(x.split(',')[0]))
    f_butrans.writelines(butrans)
    f_opana.writelines(opana)
    f_butrans.close()
    f_opana.close()
    print("Operation Successful :)")
else:
    print("Argument(s) missing.\n\
Please run the code as python3 class_drug_separation.py DATASET.csv")
    sys.exit(1)
