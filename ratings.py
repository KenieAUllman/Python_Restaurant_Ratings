"""Restaurant rating lister."""


dicts_from_file = {}
with open("scores.txt", 'r') as inf:
    for line in inf:
        key, val = line.split(":")
        dicts_from_file[key] = int(val)


new_resturant = input("What resturant name would you like to add? ")

while True:
    try:
        new_resturant_score = int(input("O a scale of 1-5, what score would you give this resturant? "))
        if 1 <= new_resturant_score <= 5:
            break
        raise ValueError()
    except ValueError:
        print("Your answer must be a number between 1-5")
            

dicts_from_file[new_resturant] = new_resturant_score


sorted_keys = sorted(dicts_from_file.keys())
for key in sorted_keys:
    print(key, dicts_from_file[key])