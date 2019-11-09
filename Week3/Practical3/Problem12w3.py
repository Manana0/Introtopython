import argparse
set2= set([1,3,4,5,6,7,15,11])
print(set2)
parser = argparse.ArgumentParser()
parser.add_argument("number", type=int)
args = parser.parse_args()
min = min(set2)
max = max(set2)
if args.number >= min and args.number <= max:

    print(True)

else:

    print(False)