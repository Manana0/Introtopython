import argparse
import datetime
import time
import calendar
current = datetime.datetime.now()
print ("Current date:", current)
print 
parser = argparse.ArgumentParser()
parser.add_argument("--num_y", type=int)
parser.add_argument("--num_d", type=int)
args = parser.parse_args()
if args.num_y:
    print("Given years:",args.num_y)
else:
    print("Given years: not given")
if args.num_d:
    print("Given days:",args.num_d)
else:
    print("Given days: not given")
