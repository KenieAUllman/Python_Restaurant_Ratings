"""Restaurant rating lister."""


dicts_from_file = {}
with open("scores.txt", 'r') as inf:
    for line in inf:
        key, val = line.split(":")
        dicts_from_file[key] = int(val)


new_resturant = input("What resturant name would you like to add? ")
new_resturant_score = input("What score would you give this resturant? ")

dicts_from_file[new_resturant] = new_resturant_score


sorted_keys = sorted(dicts_from_file.keys())
for key in sorted_keys:
    print(key, dicts_from_file[key])