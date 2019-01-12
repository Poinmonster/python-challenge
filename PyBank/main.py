import os
import csv

csvpath = os.path.join(".","budget_data.csv")

with open(csvpath, newline = '') as csvfile:
        # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)
    
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    #for row in csvreader:
     #   print(row[1])
    
    p_l = []
    # Read each row of data after the header
    for row in csvreader:
        p_l.append((int(row[1])))
    
    net = sum(p_l)
    num_months = len(p_l)
    
    changes = []
    for i in range(0, len(p_l) - 1):
        changes.append(p_l[i+1] - p_l[i])
    
    avg_change = sum(changes) / len(changes)
    
    min_change = min(changes)
    max_change = max(changes)
    
    for row in csvreader:
        if int(row[1]) == min_change:
            worst_month = row[0]
        if int(row[1]) == max_change:
            best_month = row[0]