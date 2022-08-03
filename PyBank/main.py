from datetime import date
from email.policy import default
import os
import csv


budget_bank = os.path.join('Resources', 'budget_data.csv')

with open(budget_bank) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    print(f"csv_header: {csv_header}")

    total_month = 0
    net_amo = 0
    Change = []
    avarage = []
    biggest_increase = str
    biggest_decrease = str
    number = []
    New_Change = []
    date_listed = []
    pl_listed = []
    max_amount = str
    min_amount = str

   
    #find total months
    for row in csvreader:
        total_month += 1
        date_listed.append(row[0])

        #find net total amount of profits/loss
        net_amo = net_amo + int(row[1])

        #put numbers of profit/loss in a list to find avg change
        number.append(int(row[1]))
    
      
    print(date_listed)    
    print(number)   

for i in range(1,len(number)):
    Change =  number[i] - number[i-1]
    pl_listed.append(Change)

      
print(pl_listed)

avarage = sum(pl_listed)/len(pl_listed)      
    
    

#testing print methods  for max print(pl_listed.index(max(pl_listed)))
##testing print methods  for min printprint(pl_listed.index(min(pl_listed)))

biggest_increase = (date_listed[pl_listed.index(max(pl_listed))+1])
biggest_decrease = (date_listed[pl_listed.index(min(pl_listed))+1])
max_amount = max(pl_listed)
min_amount = min(pl_listed)


#create .txt file
output_path = os.path.join('analysis', 'output.txt')
with open (output_path, 'w') as txt:
    txt.write("Financial Analysis")
    txt.write("---------------------")
    txt.write("\n")
    txt.write(f" Total Months: {len(date_listed)}")
    txt.write("\n")        
    txt.write(f" Total: $ {net_amo}")
    txt.write("\n")
    txt.write(f" Average: $ {avarage}")
    txt.write("\n")
    txt.write(f" Greatest Increase: {biggest_increase}, ($ {max_amount})")
    txt.write("\n")
    txt.write(f" Greatest Decrease: {biggest_decrease}, ($ {min_amount})")
