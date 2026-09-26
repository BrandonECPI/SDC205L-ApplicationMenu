from datetime import datetime

menu_options = ["Input Data", "View Current Data", "Generate Report"]


def convertData(value):
    # convertData takes the temperature in Fahrenheit and returns it converted to Celsius
    return (value - 32) * 5 / 9


def insertData(path, data):
    # insertData takes a file path and a comma-separated string of data, opens the file with
    # append-only permission (creating it if it does not already exist), and writes the data to it
    try:
        with open(path, "a") as file:
            file.write(data + "\n")
    except Exception as e:
        print("Error writing to file: " + str(e))
        raise


def viewData(path):
    # viewData takes a file path, opens it with read-only permission, and displays the file's
    # path along with its contents
    try:
        with open(path, "r") as file:
            print("The file " + path)
            for line in file:
                print(line.strip())
    except Exception as e:
        print("Error reading file: " + str(e))


def getInput():
    # getInput asks how many entries to add, then for each one collects a date and temperature,
    # converts it, and saves it to ZooData.csv using insertData
    num_entries = int(input("How many entries are you inputting? "))
    for i in range(num_entries):
        date = input("Enter a date: ")
        temp = int(input("Enter the highest temp for the inputted date: "))
        # convertData takes one argument, the temperature in Fahrenheit, and returns the temperature converted to Celsius
        converted = convertData(temp)
        data = date + "," + str(temp) + "," + str(converted)
        try:
            insertData("ZooData.csv", data)
            print("The following was saved at " + str(datetime.now()) + " : ")
            print(data)
        except Exception:
            pass


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
    elif choice == "2":
        viewData("ZooData.csv")
    else:
        print("Error: The chosen functionality is not implemented yet")
else:
    print("Error: Invalid choice selected.")
