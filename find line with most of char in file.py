import os

# ask user for stuff
while True:
    filepath = input("Full path to file you want analyzed: ")
    if os.path.isfile(filepath): break
    print("Invalid path!")
print(f"The code will attempt to open the file at {filepath}.")
char = input("Character you want to find in the file: ")
# ask number of lines with default
while True:
    lineamount = input("How many lines should be shown? (options: all, best, <num>) ")
    if lineamount == '': lineamount = 'all' # defaults
    if lineamount == 'all' or lineamount == 'best': break # doesn't work for '1.0' *shrug*
    if lineamount and lineamount.isdigit:
        lineamount = int(lineamount)
        break
    print("answer must be a whole number or one of the options!")

# calculate lines in order
# 'best' option
charcount = 0
if lineamount == 'best':
    bestlinenum = None
    multiplebests = []
    with open(filepath, 'r') as file:
        for linenum, lineval in enumerate(file, 1): # taken from https://stackoverflow.com/questions/3961265/get-line-number-of-certain-phrase-in-text-file
            if lineval.count(char) == charcount: multiplebests.append(linenum)
            if lineval.count(char) > charcount:
                multiplebests = []
                charcount = lineval.count(char)
                bestlinenum = linenum
# 'all' option and <num> option
else:
    lines = {}
    with open(filepath, 'r') as file:
        for linenum, lineval in enumerate(file, 1): # see above comment
            if lineval.count(char): 
                lines[linenum] = lineval.count(char)
                charcount =+1
    sortedindex = sorted(lines,key=lines.get,reverse=True) # actual sorting
    if not lineamount == 'all': del sortedindex[lineamount:] # cut to size

# output
if charcount == 0: print(f"There are no lines with '{char}' in them!")
# 'best' option
if lineamount == 'best': 
    if multiplebests and charcount:
        print(f"In {os.path.basename(filepath)}, the (tied) lines with the most of '{char}' each contain {charcount}.")
        print("Those lines are as follows:")
        print(f"Line #{bestlinenum}")
        for bestsnum in multiplebests:
            print(f"Line #{bestsnum}")
    else: print(f"In {os.path.basename(filepath)}, the line with the most of '{char}' is line #{bestlinenum}. It contains {charcount}.")
# 'all' and <num> options
if not lineamount == 'all' and len(sortedindex) < lineamount: print(f'There were less than {lineamount} lines with the character found.')
print('In order, the best lines (and their number of characters) are:')
for index in sortedindex:
    print(f"Line #{index}, with {lines[index]}")
