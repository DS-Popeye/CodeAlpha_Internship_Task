spaces = 0
lines = 0
words = 0
characters = 0
with open('text3.txt') as file:
    for line in file:
        wordslist = line.split()
        lines = lines + 1
        words = words + len(wordslist)
        for character in wordslist:
            characters += len(character)
        for letter in line:
            if (letter == ' '):
                spaces += 1
    print("Number Of Lines: ", lines)
    print("Number of Words: ", words)
    print("Number of charecters: ", characters)
    print("Number of Spaces: ", spaces)