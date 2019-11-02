import argparse
parser = argparse.ArgumentParser()
parser.add_argument("text", type=str)
args = parser.parse_args()
if len(args.text)>7 and (len(args.text)-1)%2==0:
    print(args.text)
mid= int((len(args.text)-1)/2)
mid3= args.text[mid-1:mid+2]
print(mid3)
new = args.text[0:mid-1] + mid3.upper() + args.text[mid+2:]
print (new)

