import os

# ask user for stuff
while True:
    filepath = input("Path to file you want analyzed: ")
    if os.path.isfile(filepath): break
    print("Invalid path!")
print(f"The code will attempt to open the file at {filepath}.")
char = input("Character you want to find in the file: ")

# figure out which line(s) are the best
charcount = 0
bestlinenum = None
multiplebests = []
with open(filepath, 'r') as file:
    for linenum, line in enumerate(file, 1): # taken from https://stackoverflow.com/questions/3961265/get-line-number-of-certain-phrase-in-text-file
        if line.count(char) == charcount: multiplebests.append(linenum)
        if line.count(char) > charcount:
            multiplebests = []
            charcount = line.count(char)
            bestlinenum = linenum

# tell user which line(s) are the best
if charcount == 0: print(f"There are no lines with '{char}' in them!")
elif multiplebests:
    print(f"In {os.path.basename(filepath)}, the (tied) lines with the most of '{char}' each contain {charcount}.")
    print("Those lines are as follows:")
    print(f"Line #{bestlinenum}")
    for bestsnum in multiplebests:
        print(f"Line #{bestsnum}")
else: print(f"In {os.path.basename(filepath)}, the line with the most of '{char}' is line #{bestlinenum}. It contains {charcount}.")