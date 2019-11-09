
import argparse
list2= [2,4,5,7,8,9,5,5,7]
parser = argparse.ArgumentParser()
parser.add_argument("number", type=int)
args = parser.parse_args()

print ("list2=",list2)
print("Number of", args.number,"s=",list2.count(args.number))
