# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.



import pandas as pd
import numpy as np

df = pd.read_csv("football.csv")

#Goals column_name
t = df["Goals"] #
#Goals Allowed column_name

s = df["Goals Allowed"]

# z = the difference
z = t - s

#Sorted list
z.sort

closetozero = min((abs(x), x) for x in z)[1]

print closetozero
