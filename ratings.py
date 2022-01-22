"""Restaurant rating lister."""


dicts_from_file = {}
with open("scores.txt", 'r') as inf:
    for line in inf:
        key, val = line.split(":")
        dicts_from_file[key] = int(val)


sorted_keys = sorted(dicts_from_file.keys())
for key in sorted_keys:
    print(key, dicts_from_file[key])