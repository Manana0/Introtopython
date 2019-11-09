import argparse
list4= [2,4,5,7,8,9,5,5,7]
print(list4)
parser = argparse.ArgumentParser()
parser.add_argument("number", type=int)
args = parser.parse_args()
args.number
list4.remove(args.number)
print(list4)