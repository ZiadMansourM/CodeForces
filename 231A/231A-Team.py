"""
PROBLEM_CODE: 231A - Team
This program calculate how many problems the team is going to solve
Author: Ziad Mansour Mohamed
Date: April 10, 2021
"""

def CheckSolution(contest):
    """
    return 1 if the team is going to solve it else 0
    > for example:
        @contest="1 1 1" > 1
        @contest="1 0 1" > 1
        @contest="0 0 1" > 0
    """
    return 0 if (sum(map(int, contest.split())) < 2) else 1


numberProblems = int(input())
contests = [input().strip() for _ in range(0, numberProblems)]
print(sum(list(map(CheckSolution, contests))))
