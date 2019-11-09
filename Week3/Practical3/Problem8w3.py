import argparse
set1= set([1,3,4,5,6,7,"Ann"])
print(set1)
parser = argparse.ArgumentParser()
parser.add_argument("text")
args = parser.parse_args()
set1.update([args.text])
print(set1)
