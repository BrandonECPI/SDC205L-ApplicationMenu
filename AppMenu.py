from datetime import datetime

menu_options = ["Input Data", "View Current Data", "Generate Report"]

print("bralaz4151 Spreadsheet Automation Menu")
print("Choose a number from the following options")

# option represents each menu item as the loop prints it along with its number
for index, option in enumerate(menu_options, start=1):
    print(str(index) + ". " + option)

# The next line retrieves the inputted option and stores into the variable called choice.
choice = input()

if choice.isdigit() and 1 <= int(choice) <= len(menu_options):
    print("You selected " + choice + " at " + str(datetime.now()))
else:
    print("Error: Invalid choice selected.")