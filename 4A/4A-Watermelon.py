"""
PROBLEM_CODE: 4A-Watermelon
Problem_Defination:
    This program output if this WM can be splitted into two even parts
Author: Ziad Mansour Mohamed
Date: April 17, 2021
"""


def CheckWeight(Weight):
    """
    return True if Weight can be divided into two even parts
    """
    return "YES" if Weight%2==0 and Weight > 2 else "NO"


WatermelonWeight = int(input())
print(CheckWeight(WatermelonWeight))
