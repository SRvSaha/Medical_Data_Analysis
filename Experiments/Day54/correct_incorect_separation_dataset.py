import sys

correct = []
incorrect = []
with open(sys.argv[1]) as f:
    for line in f.readlines()[1:]:
        line = line.strip().split(',')
        if(line[-1] == line[-2]):
            correct.append(','.join(line) + '\n')
        else:
            incorrect.append(','.join(line) + '\n')
    with open("correct_j48_from_test_set.csv", 'w') as f:
        f.writelines(correct)
    with open("incorrect_j48_from_test_set.csv", 'w') as f:
        f.writelines(incorrect)

