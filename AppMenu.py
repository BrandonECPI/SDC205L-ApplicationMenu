from datetime import datetime

print("bralaz4151 Spreadsheet Automation Menu")
print("Choose a number from the following options")
print("1. Input Data")
print("2. View Current Data")
print("3. Generate Report")

# The next line retrieves the inputted option and stores into the variable called choice.
choice = input()

print("You selected " + choice + " at " + str(datetime.now()))