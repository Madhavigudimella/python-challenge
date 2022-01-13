import csv
import os

#variable to store given csv file path
csv_path = os.path.join('Resources', 'budget_data.csv')

#variable to store output csv file path
ncsv_path = os.path.join('Analysis', 'nbudget_data.csv')

speriod = []
period = []
month = []
net_profit = 0
change = 0
changelist = []
sum_change = 0
output = []


# Read from existing csv file

with open(csv_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    
    #Read the header and proceed to following rows
    csv_header = next(csv_reader)
    
    #begin loop for reading
    for line in csv_reader:

        #split month and year of the date into different lists
        speriod = line[0].split("-")

        #append list to count total number of months
        month.append(speriod[0])
        #year.append(speriod[1])

        #append list to find period for greatest increase and decrease in net profit change
        period.append(line[0])
       
        net_profit = net_profit+int(line[1])

        change = int(line[1])-change
        changelist.append(change)

        sum_change = sum_change+int(change)
    
    #find location of greatest increase and decrease in changes
    index1 = changelist.index(max(changelist))
    index2 = changelist.index(min(changelist))
    
    avg_change = sum_change / len(changelist)
    
    #calculate number of months in the dataset
    Mnum = len(month)

 #Begin print statements to terminal   
    print("Financial Analysis")
    print("__________________________________________________________________")
    print("Total number of months: "+str(Mnum))
    print("Total Net Profit/Loss: $"+format(net_profit, ",.0f"))
    print("Average change over the entire period is: $"+format(avg_change, ",.0f"))
    print("Greatest Increase in Profits: "+str(period[index1])+" ($"+format(max(changelist), ",.0f")+")")
    print("Greatest Decrease in Profits: "+str(period[index2])+" ($"+format(min(changelist), ",.0f")+")")


#Write to csv file
with open(ncsv_path, 'w') as csvfile2:

        # Initialize csv.writer
    #csvwriter = csv.writer(csvfile2, delimiter=' ')

    # Write the summary to csv file
    csvfile2.write("Financial Analysis\n")
    csvfile2.write('______________________________________________________\n')  
    csvfile2.write("Total number of months: "+str(Mnum)+"\n")
    csvfile2.write('Total Net Profit/Loss: $'+format(net_profit, ",.0f")+"\n")
    csvfile2.write('Average change over the entire period is: $'+format(avg_change, ",.0f")+"\n")
    csvfile2.write('Greatest Increase in Profits: '+str(period[index1])+' ($'+format(max(changelist), ",.0f")+')\n')
    csvfile2.write('Greatest Decrease in Profits: '+str(period[index2])+' ($'+format(min(changelist), ",.0f")+')\n')
    
    
   




        


