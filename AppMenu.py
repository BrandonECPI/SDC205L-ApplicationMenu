from datetime import datetime

menu_options = ["Input Data", "View Current Data", "Generate Report"]


def convertData(value):
    # convertData takes the temperature in Fahrenheit and returns it converted to Celsius
    return (value - 32) * 5 / 9


def getInput():
    num_entries = int(input("How many entries are you inputting? "))
    for i in range(num_entries):
        date = input("Enter a date: ")
        temp = int(input("Enter the highest temp for the inputted date: "))
        # convertData takes one argument, the temperature in Fahrenheit, and returns the temperature converted to Celsius
        converted = convertData(temp)
        print("The following was saved at " + str(datetime.now()) + " : ")
        print(date + "," + str(temp) + "," + str(converted))


print("bralaz4151 Spreadsheet Automation Menu")
print("Choose a number from the following options")

# option represents each menu item as the loop prints it along with its number
for index, option in enumerate(menu_options, start=1):
    print(str(index) + ". " + option)

# The next line retrieves the inputted option and stores into the variable called choice.
choice = input()

if choice.isdigit() and 1 <= int(choice) <= len(menu_options):
    print("You selected " + choice + " at " + str(datetime.now()))
    if choice == "1":
        getInput()
    else:
        print("Error: The chosen functionality is not implemented yet")
else:
    print("Error: Invalid choice selected.")