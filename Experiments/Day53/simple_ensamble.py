    #
#   @author      : SRvSaha
#   Filename     : simple_ensamble.py
#   Timestamp    : 17:33 24-January-2017 (Tuesday)
#   Description  :
#

"""

"""

import sys
import random

with open(sys.argv[1]) as f:
    for line in f.readlines():
        count_opana = 0
        count_butrans = 0
        count_both = 0
        line = line.strip().split(',')
        # print(line)
        for item in line:
            if item == "opana":
                count_opana += 1
            elif item == "butrans":
                count_butrans += 1
            elif item == "both":
                count_both += 1
        output = [count_opana, count_butrans, count_both]
        if max(output) != 2:
                if(max(output) == count_opana):
                    print("opana")
                elif (max(output) == count_butrans):
                    print("butrans")
                else:
                    print("both")
        else:
            if (count_opana == 2 and count_butrans == 2):
                rand = random.randint(1, 2)
                if(rand == 1):
                    print("opana")
                else:
                    print("butrans")
            elif(count_opana == 2 and count_both == 2):
                rand = random.randint(1, 2)
                if(rand == 1):
                    print("opana")
                else:
                    print("both")
            elif(count_butrans == 2 and count_both == 2):
                rand = random.randint(1, 2)
                if(rand == 1):
                    print("butrans")
                else:
                    print("both")

