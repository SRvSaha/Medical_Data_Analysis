#
#   @author      : SRvSaha
#   Filename     : 3_model_ensemble.py
#   Timestamp    : 03:59 26-January-2017 (Thursday)
#   Description  :
#

"""

"""

import sys
# import random

with open(sys.argv[1]) as f:
    for line in f.readlines():
        # count_opana = 0
        # count_butrans = 0
        # count_both = 0
        count_F = 0
        count_NF = 0
        line = line.strip().split(',')
        # print(line)
        # for item in line:
        #     if item == "opana":
        #         count_opana += 1
        #     elif item == "butrans":
        #         count_butrans += 1
        #     elif item == "both":
        #         count_both += 1
        # output = [count_opana, count_butrans, count_both]
        # if(max(output) != 1):
        #     if(max(output) == count_opana):
        #             print("opana")
        #     elif (max(output) == count_butrans):
        #         print("butrans")
        #     else:
        #         print("both")
        # else:
        #     rand = random.randint(1, 3)
        #     if(rand == 1):
        #         print("opana")
        #     elif (rand == 2):
        #         print("butrans")
        #     else:
        #         print("both")
        for item in line:
            if item == "F":
                count_F += 1
            elif item == "NF":
                count_NF += 1
        if(count_F > count_NF):
            print("F")
        else:
            print("NF")
