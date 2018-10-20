import os
import csv

# Path to collect data from the  folder
electionCSV = os.path.join('election_data.csv')
      
with open(electionCSV, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    total_votes = 0
    candidates_list = []
    voted_candidates = []
    Correy = 0
    Khan = 0
    Tooley = 0
    Li = 0
    
      # Loop through the data
    for row in csvreader:
       
        total_votes += 1
        candidates_list.append(row[2])

    voted_candidates = set(candidates_list)
    total_Correy = candidates_list.count('Correy')
    total_Khan = candidates_list.count('Khan')
    total_Tooley = candidates_list.count("O'Tooley")
    total_Li = candidates_list.count('Li')
    percent_Correy = (total_Correy/total_votes)*100
    percent_Khan = (total_Khan/total_votes)*100
    percent_Tooley = (total_Tooley/total_votes)*100      
    percent_Li = (total_Li/total_votes)*100
    list = [percent_Correy,percent_Khan,percent_Tooley,percent_Li]
    list = [round(x,3) for x in list]
    names = ["Correy","Khan","O' Tooley","Li"]
    max = max(list)
    maximum = list.index(max)
    winner = names[int(maximum)]

print("Election Results")  
print("--------------------------------------------------------")      
print (f"Total Votes: {total_votes}") 
print("--------------------------------------------------------")
print (f"Correy: {percent_Correy}% ({total_Correy})")
print (f"Khan: {percent_Khan}% ({total_Khan})")          
print (f"O'Tooley: {percent_Tooley}% ({total_Tooley})")
print (f"Li: {percent_Li}% ({total_Li})") 
print("--------------------------------------------------------")
print (f"Winner: {winner}")
print("--------------------------------------------------------")
f = open('poll.txt','w')
f.write('Election Results')
f.write("\n")
f.write('--------------------------------------------------------')
f.write("\n")
f.write(f"Total Votes: {total_votes}")
f.write("\n")
f.write('--------------------------------------------------------')
f.write("\n")
f.write(f"Correy: {percent_Correy}% ({total_Correy})")
f.write("\n")
f.write(f"Khan: {percent_Khan}% ({total_Khan})")
f.write("\n")
f.write(f"O'Tooley: {percent_Tooley}% ({total_Tooley})")
f.write("\n")
f.write(f"Li: {percent_Li}% ({total_Li})")
f.write("\n")
f.write('--------------------------------------------------------')
f.write("\n")
f.write(f"Winner: {winner}")
f.write("\n")
f.write('--------------------------------------------------------')
f.close()