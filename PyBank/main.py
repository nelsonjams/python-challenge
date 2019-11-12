import os
import csv

budget_csv = os.path.join(".", "Resources", "budget_data.csv")
    #set variables for calculations
total_pnl = 0
total_months = 0
max_pnl_increase = -float("inf")
max_pnl_decrease = float("inf")
max_pnl_increase_month = ""
max_pnl_decrease_month = ""
total_pnl_change = 0
   
with open(budget_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #skip the header using next
    csv_header = next(csvfile)
    print(f"Header: {csv_header}")

    #deal with the exception of the first row using next
    first_row_data = next(csvfile)
    first_month_pnl = int(first_row_data)
    total_months = total_months + 1
    total_pnl = total_pnl + first_month_pnl
    previous_month_pnl = first_month_pnl
      
    #loop through rows to find the number of months and 
    # the total of Profit/Losses column
    for row in csvreader:
        current_month = row[0]
        current_month_pnl = float(row[1]) 
        #find number of months count
        total_months = total_months + 1
        #find total of profit/losses column
        total_pnl = total_pnl + current_month_pnl
        #find increase or decrease of monthly profit/loss
        pnl_increase = current_month_pnl - previous_month_pnl
        #find total pnl change        
        total_pnl_change = total_pnl_change + pnl_increase
        #if statement to extract max and min monthly change in profit/losses
        if (pnl_increase > max_pnl_increase):
            max_pnl_increase = pnl_increase
            max_pnl_increase_month = current_month
        if (pnl_increase < max_pnl_decrease):
            max_pnl_decrease = pnl_increase
            max_pnl_decrease_month = current_month

        #reset loop and calculate the average change in profit/losses
        avg_change_pnl = round(((total_pnl_change)/total_months - 1), 2)

    #print out analysis           
    print("Financial Analysis")   
    print("---------------------------") 
    print("Total Months:", total_months)
    print("Total: $", total_pnl)
    print("Average Change:", avg_change_pnl)
    print("Greatest Increase in Profits:", max_pnl_increase_month, max_pnl_increase)
    print("Greatest Decrease in Profits", max_pnl_decrease_month, max_pnl_decrease)

     
           


    

              
    
  






