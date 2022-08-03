import os
import csv
csvpath = os.path.join('Resoreces', 'election_data.csv')




# Initialize the 'Total Vote counter' and the 'Winning votes counter'. 
total_votes_counter= 0
Winning_Votes_counter = 0
# Initialize candidates list. 
List_Of_candidates = []
# Initialize dictionary of candidates and their votes. 
Votes_for_candidates = {}
with open(csvpath) as csv_file: 
    CSVreader = csv.reader(csv_file, delimiter=",")
    

# Skipping the header row. 
    header_row = next(csv_file)

#worked with Mauvonte Roberts and TA's to get the code working one i ran in to some issues 
# Iterating through the rows in the election data file. 
    for row in CSVreader:
        # Identifying the rows of candidates in the eletion data file. 
        candidate_name = row[2]

        # Incrementing the total vote count for each row in the election data file. 
        total_votes_counter = total_votes_counter + 1

        # Adding a new candidate name to a list for every row in the election data file. 
        if candidate_name not in List_Of_candidates:
            List_Of_candidates.append(candidate_name)

            # Initializing the vote count for each new candidate name. 
            Votes_for_candidates[candidate_name] = 0

        # Adding to the vote count of every candidate name if similar. 
        Votes_for_candidates[candidate_name] += 1


#worked with Mauvonte Roberts and TA's to get the code working one i ran in to some issues 
# Writing the first part of the results of the analysis. 
results_One = str(f"Election Results\n"
                    f"------------------\n"
                    f"Total Votes: {total_votes_counter}\n"
                    f"------------------"
                    )



# Initializing the add-on to the second part of the analysis results. 
all_results_Two = ""



# Initiating a for loop for the 'Candidate Votes' dictionary. 
for candidate_name, votes in Votes_for_candidates.items():
    # Calculating the percentage of votes cast for each candidate. 
    vote_percentage = votes / total_votes_counter
    # Formatting the vote percentage of each candidate to have three decimal places and a percentage sign. 
    vote_percentage_formatted = "{:.3%}".format(vote_percentage)
    # Writing the second part of the analysis results. 
    results_Two = str(f"{candidate_name}: {vote_percentage_formatted} ({votes})")
    # Adding a new line after each iteration of the second part of the analysis results. 
    all_results_Two += '\n'
    # Adding the second part of the analysis results to the add-on for the second part. 
    all_results_Two += results_Two
    # Calculating the winning candidate. 
    if votes > Winning_Votes_counter:
        Winning_Votes_counter = votes
        winner = candidate_name


# Writing the third part of the analysis results. 
results_Three = str(f"---------------------\n"
                    f"Winner: {winner}\n"
                    f"---------------------")


# Writing the final part of the analysis results which sums up the other three parts including the add-on. 
total_End_results = str(f"{results_One} \n {all_results_Two} \n {results_Three}")

# Saves the analysis results to a text file. 
output_path = os.path.join('analysis', 'output.txt')
with open (output_path, 'w') as textfile:
        textfile.write(total_End_results)

#worked with Mauvonte Roberts and TA's to get the code working one i ran in to some issues 
#tested the results for each results left in comments in needed later for future testing 
#print(f"{results_One}\n") #print(f"{results_Two}\n") #print(f"{results_Three}\n")


print(f"{total_End_results}\n")