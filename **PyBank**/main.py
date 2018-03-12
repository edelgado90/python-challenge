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
    

#Create a list that holds the differences bewteen months

deltas =[]

for x in range(1,len(revenues)):
    
     deltas.append(revenues[x] - revenues[x-1])

#Identify average, maximum and minimum values and associated months among the deltas

average = sum(deltas)/len(deltas)

maximum = max(deltas)

maxmonth = months[deltas.index(maximum)+1]

minimum = min(deltas)

minmonth = months[deltas.index(minimum)+1]

#Print the results

print("Financial Analysis")
print("Total Months: " + str(monthsnumber))
print("Total Revenue: $" + str(totalrevenue))
print("Average Revenue Change: $" + str(average))
print("Greatest Increase In Revenue: " + str(maxmonth) + " ($" + str(maximum) + ")")
print("Greatest Decrease In Revenue: " + str(minmonth) + " ($" + str(minimum) + ")")

#Write the results to a file

with open('results.csv', 'w') as csvfile:    
    results = csv.writer(csvfile, delimiter= ',')
    results.writerow('Financial Analysis')
    results.writerow("Total Months: " + str(monthsnumber))
    results.writerow("Total Revenue: $" + str(totalrevenue))
    results.writerow("Average Revenue Change: $" + str(average))
    results.writerow("Greatest Increase In Revenue: " + str(maxmonth) + " ($" + str(maximum) + ")")
    results.writerow("Greatest Decrease In Revenue: " + str(minmonth) + " ($" + str(minimum) + ")")
    
    
    