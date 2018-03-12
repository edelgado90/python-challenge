import os
import csv

#Import the data
budget_csv = "budget_data_1.csv"

#Read the data into two lists, one for the months and one for the revenues

months = []
revenues = []

with open(budget_csv, newline="") as csvfile:
    csvreader= csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        
        months.append(row[0])
        
        revenues.append(row[1])
                        
months.remove('Date')        

revenues.remove('Revenue')

#Convert the revenue list to int type to allow for calculations
revenues = [int(x) for x in revenues]
        
#Count the number of months in the list     
    
monthsnumber = len(months)

#Calculate revenue for the entire period

totalrevenue = int(0)

for x in revenues:

    totalrevenue = totalrevenue + x