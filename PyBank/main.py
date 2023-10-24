import csv
import os

dirname = os.path.dirname(__file__)
file = os.path.join("Resources", "budget_data.csv")
outfile = os.path.join("analysis.txt")

# Total Month Counter
total_months = 0
# Total Profit/Loss
net_profit = 0
# Change in monthly totals
previous_profit = 0
profit_changes = []
months = []
profit = 0

# open and read the csv
with open(file) as budget_data:
	reader = csv.reader(budget_data)

	# Read the header
	header = next(reader)

	# Loop the rows
	for row in reader:
		# Add the total month count
		total_months = total_months + 1
		
		# Get the monthly profit
		month = row[0]
		net_profit += int(row[1])
		profit = int(row[1])

	# Calculate profit changes
		if previous_profit != 0:
			profit_changes.append(profit - previous_profit)
			months.append(month)
		previous_profit = profit

# Calc average change
average_change = sum(profit_changes) / len(profit_changes)

# Calc greatest increase in profit (date and amount) over the entire period
max_increase = max(profit_changes)
max_increase_month = months[profit_changes.index(max_increase)]
# Calc greatest decreate in profit (date and amount) over the entire period
min_increase = min(profit_changes)
min_increase_month = months[profit_changes.index(min_increase)]

# Print results on txt file
with open(outfile, "w") as txt_file:
	summary = (f"Financial Analysis \n"
		   f"-----------------------------\n")
	month_count = f"Total Months: {total_months}"
	net_total = f"Total: ${net_profit}"
	average_month = f"Average change: ${round(average_change,2)}"
	greatest_increase = f"Greatest increase in profits: {max_increase_month}, (${max_increase})"
	greatest_decrease = f"Greatest decrease in profits: {min_increase_month}, (${min_increase})"

	txt_file.write(summary + "\n" + month_count + "\n" + net_total + "\n" + average_month + "\n" + greatest_increase + "\n" + greatest_decrease)