fname = input("Enter File Name:")
ddays = dict()
try:
    fhand = open(fname)
except FileNotFoundError:
    print("File Not Found")
    exit()
for line in fhand :
    words = line.split()
    if len(words) < 2 or words[0] != "From":
        continue
    else:
        if words[1] not in ddays:
            ddays[words[1]] = 1
        else:
            ddays[words[1]] += 1
print(ddays)
