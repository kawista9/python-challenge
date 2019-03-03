import os
import csv
#pathway to file
csvpath = os.path.join("budget_data.csv")
file=os.path.join("input.txt")

date=[]
revenue=[]
diff=[]
firstrow=[]
nextrow=[]
row_count=0
col_sum=0

#print headers
print("Financial Analysis")
print("-----------------------------")

#open and read file
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    
    #loop through rows 
    for row in csvreader:
        date.append(row[0])
        revenue.append(int(row[1]))

        row_count=row_count+1
        col_sum=col_sum +int(row[1])
    
    diff= [y-x for x,y in zip(revenue,revenue[1:])]

    max_value=max(diff)
    min_value=min(diff)
    avgchange=round((sum(diff)/row_count), 2)        
    
    print(f"Total Months:  {row_count}")
    print(f"Total: ${col_sum}")
    print(f"Average Change: ${avgchange}")
    print(f"Greatest Increase in Profits: (${max_value})")
    print(f"Greatest Decrease in Profit:  (${min_value})")

 

with open(file, "r") as text:
    print(text)

    lines=text.read()
    print(lines)
    
    
    
    


