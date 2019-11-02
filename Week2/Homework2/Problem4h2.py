import argparse

parser = argparse.ArgumentParser()

parser.add_argument("text", type=str)
args = parser.parse_args()
print ("The given string:", args.text)
lower=args.text.lower()
print("The USA/usa count is:", lower.count('usa'))
print("The new string: " + args.text.replace("USA", "Armenia").replace("usa", "Armenia"))