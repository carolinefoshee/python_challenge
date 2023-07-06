# import modules
import os
import csv
import datetime
import math

# open csv 
election_csv = os.path.join('Resources/election_data.csv')

# initialize some values 
numunique=0
numvotes=0
doane=0
stockham=0
degette=0
candidates=[]

#The total number of votes cast
with open(election_csv) as csvfile:
    for row in csv.reader(csvfile, delimiter=","):
        if row[0]!="Ballot ID":
            numvotes=numvotes+1

#A complete list of candidates who received votes
with open(election_csv) as csvfile:
    for row in csv.reader(csvfile, delimiter=","):
        if (row[2] not in candidates) & (row[2] != "Candidate"):
            candidates.append(row[2])

#The total and percentage of votes each candidate won

with open(election_csv) as csvfile:
    for row in csv.reader(csvfile, delimiter=","):
        if row[2]!="Candidate":
            if row[2]== "Raymon Anthony Doane":
                doane=doane+1
            if row[2]== "Diana DeGette":
                degette=degette+1
            if row[2]== "Charles Casper Stockham":
                stockham=stockham+1
stockhampc= round(stockham/numvotes*100, 3)
degettepc= round(degette/numvotes*100, 3)
doanepc= round(doane/numvotes*100, 3)
print("Election Results:") 
print(f"Total number of votes cast: {numvotes}")
print(f"Charles Casper Stockham: {stockhampc}% ({stockham})")
print(f"Diana DeGette: {degettepc}% ({degette})")
print(f"Raymon Anthony Doane= {doanepc}% ({doane})")

#The winner of the election based on popular vote
if (stockhampc > degettepc) & (stockhampc > doanepc):
    print("Stockham wins!")
if (degettepc > stockhampc) & (degettepc > doanepc):
    print("Degette wins!")
if (doanepc > stockhampc) & (doanepc > degettepc):
    print("Degette wins!")

# print to text document
text = open('Analysis/electionresults.txt')
with open('Analysis/electionresults.txt', 'w') as f:
    f.write("Election Results:")
    f.write(f"\nTotal number of votes cast: {numvotes}")
    f.write(f"\nCharles Casper Stockham: {stockhampc}% ({stockham})")
    f.write(f"\nDiana DeGette: {degettepc}% ({degette})")
    f.write(f"\nRaymon Anthony Doane= {doanepc}% ({doane})")
    if (stockhampc > degettepc) & (stockhampc > doanepc):
        f.write("\nStockham wins!")
    if (degettepc > stockhampc) & (degettepc > doanepc):
        f.write("\nDegette wins!")
    if (doanepc > stockhampc) & (doanepc > degettepc):
        f.write("\nDegette wins!")