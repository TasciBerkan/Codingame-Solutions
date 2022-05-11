import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # the number of temperatures to analyse
temps=input()
result=""

if len(temps)==0:
    print("0")

else:
    temps_split=temps.split()
    result=temps_split[0]

    for temp in temps_split:
        if abs(int(temp)) < abs(int(result)):
            result = temp
        elif abs(int(temp)) == abs(int(result)):
            result = max(int(temp),int(result)) 

print(result)