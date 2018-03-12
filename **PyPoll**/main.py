import csv

#Import the data
vote_csv = "election_data_1.csv"

#Read the data into three lists 

voterid = []
county = []
candidate = []

with open(vote_csv, newline="") as csvfile:
    csvreader= csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        
        voterid.append(row[0])
        
        county.append(row[1])
        
        candidate.append(row[2])
        
voterid.remove('Voter ID')        

county.remove('County')

candidate.remove('Candidate')
                
#Calculate the total number of votes cast 

totalvotes = len(voterid)
        
#Create a complete list of candidates who received votes

candlist = []

for x in candidate:
    if x not in candlist:
        candlist.append(x)

#Create a list with the number of votes each candidate won        

votecount = []

for x in candlist :
    votecount.append(candidate.count(x))

#Create a list with the percent of votes each candidate won 

votepercent = []

for x in votecount :
    votepercent.append(x / totalvotes)

#Determine the winner of the election

winningnumber = max(votecount)

winner = candlist[votecount.index(winningnumber)]

#Print the results

print("Election Results")
print("---------------------------------")
print("Total Votes: " + str(totalvotes))
print("---------------------------------")

for x in candlist: 
    print(x + ": " + "{0:.2f}%".format(votepercent[candlist.index(x)]*100) + " (" + str(votecount[candlist.index(x)]) + ")")

print("---------------------------------")
print("Winner: " + winner)
print("---------------------------------")

#Write the results to a file

with open('results.csv', 'w') as csvfile:    
    results = csv.writer(csvfile, delimiter= ',')
    results.writerow("Election Results")
    results.writerow("---------------------------------")
    results.writerow("Total Votes: " + str(totalvotes))
    results.writerow("---------------------------------")
    
    for x in candlist: 
        results.writerow(x + ": " + "{0:.2f}%".format(votepercent[candlist.index(x)]*100) + " (" + str(votecount[candlist.index(x)]) + ")")

    results.writerow("---------------------------------")
    results.writerow("Winner: " + winner)
    results.writerow("---------------------------------")

    