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
        atpos = words[1].find("@")
        domain = words[1][atpos + 1:]
        if domain not in ddays:
            ddays[domain] = 1
        else:
            ddays[domain] += 1
print(ddays)
