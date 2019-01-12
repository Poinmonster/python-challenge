import os
import csv
file = "election_data.csv"
csvpath = os.path.join(".", "election_data.csv")
with open(csvpath, newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    votes = []
    
    for line in csvreader:
        votes.append(line[2])
    candidates = list(set(votes))
    vote_total = len(votes)
results = {}
for candidate in candidates:
    results[candidate] = str("{:.0%}".format(votes.count(candidate)/vote_total)) + " Votes: " + str(votes.count(candidate))
candidate_totals = []
for candidate in candidates:
    candidate_totals.append(votes.count(candidate))
for candidate in candidates:
    if votes.count(candidate) == max(candidate_totals):
        Winner = candidate
print(f"Election Summary\nWinner: {Winner}\nVotes Cast: [total_votes]\nVote Totals\n")
print(results)
vote_file = open("election-summary", "w")
vote_file.write("Election Summary\n")
vote_file.write("Winner: ")
vote_file.write(Winner)
vote_file.write("\nTotal Votes Cast: ")
vote_file.write(str(vote_total))
vote_file.write("\nFull Results\n")
vote_file.write(str(results))
vote_file.close()