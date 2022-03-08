with open("allwords.txt") as f:
    lines = f.readlines()

banned = ["e", "p"]
same = []
current = 0
longest = ""

for line in lines:
    current += 1
    line = line.lower()
    word_banned = False
    for letter in line:
        if letter in banned:
            word_banned = True
    if not word_banned:
        if len(line) > len(longest):
            longest = line
            print("INFO >>> New longest:", longest, end="")
            same = []
        if len(line) == len(longest):
            same.append(line)
    if current % 10000 == 0:
        print("INFO >>> Searched", current, "words")

for i in range(3):
    print("\n")

print("Words of the same length without banned letters:\n")
for i in range(len(same)):
    print(str(i+1) + ".", same[i], end="")
