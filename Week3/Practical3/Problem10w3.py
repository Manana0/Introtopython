import argparse
set2= set([1,3,4,5,6,7,"Ann"])
print(set2)
parser = argparse.ArgumentParser()
parser.add_argument("text")
args = parser.parse_args()
set2.discard(args.text)
print(set2)