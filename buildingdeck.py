base_values = {}
with open("file.txt") as f:
    for line in f:
       (key, val) = line.split()
       d[key] = int(val)

print(d)