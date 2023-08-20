import string

text = str(input("Text: "))
textl = text.lower()
ascii = string.ascii_lowercase
lcount = 0
wcount = 1
scount = 0

for i in range(len(text)):
    for letter in ascii:
        if letter == textl[i]:
            lcount += 1


for i in range(len(text)):
    if textl[i] == " ":
        wcount += 1

for i in range(len(text)):
    if textl[i] == "." or textl[i] == "!" or textl[i] == "?":
        scount += 1

L = lcount * 100 / wcount
S = scount * 100 / wcount
grade = round(0.0588 * L - 0.296 * S - 15.8)

if grade < 1:
    print("Before Grade 1")
    quit(0)

if grade >= 16:
    print("Grade 16+")
    quit(0)

print(f"Grade {grade}")