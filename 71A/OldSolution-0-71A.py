"""
$ OldSolution :: latest @"71A-Way Too Long Words".py
PROBLEM_CODE: 71A - Way Too Long Words
"""
def AppreviateWords(string):
    return string[0] + str(len(string[1:-1])) + string[-1]

numberInputs = int(input())
WordsList = [input().strip() for _ in range(0, numberInputs)]
for i, x in enumerate(WordsList):
    if len(x) >= 10:
        WordsList[i] = AppreviateWords(x)

print(*WordsList)