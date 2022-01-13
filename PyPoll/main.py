import csv
import os

#variable to store given csv file path
csv_path = os.path.join('Resources', 'election_data.csv')

#variable to store output csv file path
ncsv_path = os.path.join('Analysis', 'nelection_data.csv')

total_vote = 0
unique_list = []
voter_id = []
candidate = []
vote_count = 0
vote_summary = []


# Read from existing csv file

with open(csv_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    
    #Read the header and proceed to following rows
    csv_header = next(csv_reader)
    
    #begin loop for reading
    for line in csv_reader:
        
        #counter for total number of votes
        total_vote = total_vote+1

        voter_id.append(line[0])
        candidate.append(line[2])

    #list of candidates

    unique_set = set(candidate)
    unique_list = list(unique_set)

#print to the terminal
print("Election Results")
print("___________________________________________")
print("Total number of votes: "+str(total_vote))
print("___________________________________________")

#loop for vote summary by candidate
for i in range(len(unique_list)):
    #counts number of occurances of each unique candidate
    vote_summary.append(candidate.count(unique_list[i]))
    print(unique_list[i]+": "+"{:.3%}".format(vote_summary[i]/total_vote)+" ("+str(vote_summary[i])+")")

#Write to csv file
with open(ncsv_path, 'w') as csvfile2:

    # Write the summary to csv file
    csvfile2.write("Election Results\n")
    csvfile2.write("___________________________________________\n")  
    csvfile2.write("Total number of votes: "+str(total_vote)+"\n")
    csvfile2.write("___________________________________________\n")

    # calculate number of votes for each candidate and write to csv file  
    for j in range(len(unique_list)):
        csvfile2.write(unique_list[j]+":"+"{:.3%}".format(vote_summary[j]/total_vote)+"("+str(vote_summary[j])+")\n")

