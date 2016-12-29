#
#   @author      : SRvSaha
#   Filename     : join_tables_opana_butrans.py
#   Timestamp    : 16:28 29-December-2016 (Thursday)
#   Description  : Joining of the databases of opana and butrans. [FULL JOIN]
#

#!/usr/bin/env python3
"""
The script can automatically work as FULL-OUTER-JOIN in SQL for 2 tables.

Here we're joining OPANA table and BUTANS table based on the attributes that
are common to both and also those which are unique. This is the implementation
of somewhat like FULL OUTER JOIN in SQL.

Requirements: Python 3
RUN : python3 join_tables_opana_butrans.py <OPANA_table.csv> <BUTRANS_table.csv>
OPANA_table.csv : Consists of ENROL_ID, SEX, AGEGRP, REGION, REFILL_COUNT, DX/PX CODES, CLASS_DRUG
BUTRANS_table.csv : Consists of ENROL_ID, SEX, AGEGRP, REGION, REFILL_COUNT, DX/PX CODES, CLASS_DRUG

OUTPUT : Final table consists of SEX, AGEGRP, REGION, REFILL_COUNTT, COMMON & UNCOMMON CODES, CLASS DRUG
"""

import sys

if len(sys.argv) == 3:
    records = []
    f_out = open('join_opana_butrans.csv', 'w')
    with open(sys.argv[1]) as f_opana:
        records = f_opana.readlines()[1:]
    with open(sys.argv[2]) as f_butrans:
        records += f_butrans.readlines()[1:]
    records.sort(key=lambda x: x.split(',')[0])
    print(records)
    # Uncomment for file without ENROLL ID ready for ML
    # header = 'SEX,AGEGRP,REGION,REFILL_COUNT,ADMTYP,'
    # ENROLL ID to check out manually if order is sorted and table is correct/not
    header = 'ENROLL_ID,SEX,AGEGRP,REGION,REFILL_COUNT,ADMTYP,'
    f_out.write(header + '27447,71536,1402,8154,71516,71596' + ',Class_Drug\n')
    for record in records:
        output = ''
        record = record.split(',')
        if 'butrans' in record[-1]:
            # Uncomment for file without ENROLL ID ready for ML
            # output = ','.join(record[1:11]) + ',0,' + record[-1]
            output = ','.join(record[:11]) + ',0,' + record[-1]
        else:
            # Uncomment for file without ENROLL ID ready for ML
            # output = ','.join(record[1:10]) + ',0,' + ','.join(record[-2:])
            output = ','.join(record[:10]) + ',0,' + ','.join(record[-2:])
        f_out.write(output)
    f_out.close()
else:
    print("Argument(s) missing.\n\
Please run the code as python3 join_tables_opana_butrans.py OPANA_table.csv BUTRANS_table.csv")
    sys.exit(1)
