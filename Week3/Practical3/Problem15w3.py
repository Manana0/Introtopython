import argparse
my_dict = {'key1':'value1','key2':'value2'}
print(my_dict)
parser = argparse.ArgumentParser()
parser.add_argument("key3", type=str)
parser.add_argument("value3", type=str)
args = parser.parse_args()
key=args.key3
value=args.value3

my_dict.update({key:value})
print(my_dict)

