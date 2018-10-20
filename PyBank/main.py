import os
import csv

# Path to collect data from the  folder
budgetCSV = os.path.join('budget_data.csv')
      
with open(budgetCSV, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    total_profit_loss = 0
    total_months = 0
    profit_loss = []
    months = []
    max_profit_loss = 0
    max_month = 0
    min_profit_loss = 0

      # Loop through the data
    for row in csvreader:
        profit_loss.append(int(row[1]))
        months.append(row[0])
        total_profit_loss += int(row[1])
        total_months += 1
    max_profit_loss = max(profit_loss)
    max = profit_loss.index(max_profit_loss)
    max_month = months[int(max)]
    min_profit_loss = min(profit_loss)
    min = profit_loss.index(min_profit_loss)
    min_month = months[int(min)]
        
print("Financial Analysis")  
print("--------------------------------------------------------")      
print (f"Total Months: {total_months}") 
print (f"Total: ${total_profit_loss}")
print (f"Greatest Increase in Profits: {max_month} (${max_profit_loss})")            
print (f"Greatest Decrease in Profits: {min_month} (${min_profit_loss})") 
f = open('output.txt','w')
f.write('Financial Analysis')
f.write("\n")
f.write('--------------------------------------------------------')
f.write("\n")
f.write(f"Total Months: {total_months}")
f.write("\n")
f.write(f"Total: ${total_profit_loss}")
f.write("\n")
f.write(f"Greatest Increase in Profits: {max_month} (${max_profit_loss})")
f.write("\n")
f.write(f"Greatest Decrease in Profits: {min_month} (${min_profit_loss})")
f.close()
