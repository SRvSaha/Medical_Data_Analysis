#
#   @author      : SRvSaha
#   Filename     : duplicate_blank_space_removal.py
#   Timestamp    : 22:51 30-December-2016 (Friday)
#   Description  : Removal of Duplicate & Blank Entries from Butrans&Opana Dataset
#

"""
Removal of Duplicate & Blank Entries from Butrans & Opana Dataset.

The patients who consumed both butrans and opana are given in the input dataset.
Specifically, ENROLL_ID, SEX, DX and PX of those patients are given. This script removes
all the duplicated entries from the dataset. Also, it removes all the blank spaces
from the DX and PX codes and outputs records with the ENROLL_ID, SEX, DX, PX which are
unique.

Requirements : Python 3
Run : python3 duplicate_blank_space_removal.py <DATASET.csv>
DATASET : ENROLL_ID, SEX, DX, PX for patients who take butrans & opana both
"""
import sys

if len(sys.argv) == 2:
    output = set()
    with open(sys.argv[1]) as f:
        # for line in f.readlines()[1:]:
        for line in f.readlines():
            # line = [item for item in line.split(',') if item != '']
            # output.add(','.join(line))
            output.add(line)
        output = sorted(output, key=(lambda x: x.split(',')[0]))
    # with open("both_butrans_opana_apriori_full.csv", 'w') as f:
    with open("both_butrans_opana_without_duplicates.csv", 'w') as f:
        f.writelines(output)
        print("Output Successful :)")
else:
    print("Argument(s) Missing\nPlease run the code as : python3 duplicate_blank_space_removal.py <DATASET.csv>")
    sys.exit(1)
