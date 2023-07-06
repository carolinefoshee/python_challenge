# import modules
import os
import csv
import datetime
import math

# open csv file
budget_csv = os.path.join('Resources/budget_data.csv')

# initializing some variables
monthcount=0
netprofits=0
total=0
profits=[]
changes=[]
dates=[]
minmonth= ""
maxmonth=""

# print title for the output 
print("Financial Analysis")
print("-----------------------------------------------------")

# Loop through column 1 of excel sheet to identify number of months in the dataset
with open(budget_csv) as csvfile:
    for row in csv.reader(csvfile, delimiter=","):
       if row[1] != "Profit/Losses": # skip header row
            monthcount=monthcount+1
    print(f"Total Months= {monthcount}")    

# Loop through column 2 of csv to identify the net total amount of "Profit/Losses" over the entire period
with open(budget_csv) as csvfile:
    for row in csv.reader(csvfile, delimiter=","):
        if row[1] != "Profit/Losses":  # skip header row
            netprofits = int(row[1]) + int(netprofits)
    print(f"Net profits= {netprofits}")

# Use lists to find: 
# 1) The changes in "Profit/Losses" over the entire period, and then the average of those changes 
# 2) The greatest increase in profits (date and amount) over the entire period
# 3) The greatest decrease in profits (date and amount) over the entire period
with open(budget_csv) as csvfile:
    for row in csv.reader(csvfile, delimiter=","):
        if row[1] != "Profit/Losses":  # skip header row 
            profits.append(row[1]) # use a list to store values of profits and losses
            dates.append(row[0]) # use a list to store dates
    for x in range(0,len(profits)):
       chg=int(profits[x])-int(profits[x-1])
       changes.append(chg)
    avgchange=sum(changes)/len(changes)
    min=int(min(changes))
    max=int(max(changes))
    minindex=changes.index(min) #find the raw value associated with min/max changes 
    maxindex=changes.index(max)
    minmonth=dates[minindex]
    maxmonth=dates[maxindex]
print(f"Greatest Increase in Profits= {maxmonth} ({max})")
print(f"Greatest Decrease in Profits= {minmonth} ({min})")

# print results to text file
text = open('Analysis/profit analysis.txt')
with open('Analysis/profit analysis.txt', 'w') as f:
    f.write('Financial Analysis')
    f.write("\n-----------------------------------------------------")
    f.write(f"\nTotal Months= {monthcount}")
    f.write(f"\nNet profits= {netprofits}")
    f.write(f"\nGreatest Increase in Profits= {maxmonth} ({max})")
    f.write(f"\nGreatest Decrease in Profits= {minmonth} ({min})")
