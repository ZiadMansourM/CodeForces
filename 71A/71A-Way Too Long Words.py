"""
PROBLEM_CODE: 71A - Way Too Long Words
This program replace strings whose len > 10 with ex:a9k if input:="abcdefghijk"
Author: Ziad Mansour Mohamed
Date: April 10, 2021
"""

def CheckLength(string):
    """
    return appreviate(string) if length of input string > 10 else pass
    """
    return string if len(string) <= 10 else AppreviateWords(string)

def AppreviateWords(string):
    """
    @string = "abcdefghijk"
    return a9k
    """
    return string[0] + str(len(string[1:-1])) + string[-1]

numberInputs = int(input())
WordsList = [input().strip() for _ in range(0, numberInputs)]
print(*list(map(CheckLength, WordsList)))
