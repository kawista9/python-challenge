import os
import csv

csvpath=os.path.join("election_data.csv")

voter_id=[]
county=[]
candidate=[]
li_count=0
print("Election Results")
print("------------------------------")
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)

    for row in csvreader:
        voter_id.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

        per_li= ((candidate.count("Li"))/len(voter_id))*100
        per_khan= ((candidate.count("Khan"))/len(voter_id))*100
        per_correy=((candidate.count("Correy"))/len(voter_id))*100
        per_otooley=((candidate.count("O'Tooley"))/len(voter_id))*100




    
    



    print(f"Total Votes: {len(voter_id)}")
    print("--------------------------")
    print(f"{per_li}% ({candidate.count("Li")})")
    print(f"{per_khan}% {candidate.count("Khan")})")
    print(f"{per_correy}% ({candidate.count("Correy")})")
    print(f"{per_otooley}% ({candidate.count("O'Tooley")})")