# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RLupinski,02.12.22,Added code to complete assignment 5
# RLupinski,02.13.22,finish up write table to file section, updated the display table style
# RLupinski,02.14.22, clean up comments section
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"  # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""  # A menu of user options
strChoice = ""  # A Capture the user option selection

# -- Processing -- #
# Step 1 - When the program starts, load any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
try:  # try to load data from ToDoList.txt into a list of dictionary rows
    objFile = open('ToDoList.txt', 'r')  # open ToDoList.txt in read mode
    for row in objFile:  # for each row in objFile
        strData = row.split(",")  # assign comma separated data to strData, split by ","
        dicRow = {'Task': strData[0], 'Priority': strData[1].strip()}  # load each strData list element into a dicRow
        lstTable.append(dicRow)  # append lstTable with each dicRow
    objFile.close()  # close the file
except:  # if the ToDoList.txt file doesn't exist - make a txt file
    objFile = open("ToDoList.txt", 'w')
    objFile.close()
    print("ToDoList.txt not found. Creating a new ToDoList.txt file")

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while True:
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if strChoice.strip() == '1':
        for row in lstTable:  # for each row in lstTable
            strData1 = row['Task']  # Use 'Task' key to get task
            strData2 = row['Priority']  # Use 'Priority' key to get priority
            print(strData1 + " | " + strData2)  # print the row separated by a bar
        continue
    # Step 4 - Add a new item to the list/Table
    elif strChoice.strip() == '2':
        strTask = input("Enter a task: ")  # prompt user for the task
        strPriority = input("Enter the priority: ")  # prompt user for the priority
        dicRow = {'Task': strTask, 'Priority': strPriority}  # create a new dicRow with new task
        lstTable.append(dicRow)  # append the table w/ new dicRow
        continue
    # Step 5 - Remove a new item from the list/Table
    elif strChoice.strip() == '3':
        removeChoice = input("What task do you want to remove? ")  # prompt user for task to delete
        for row in range(len(lstTable)):  # look in each row of the lstTable
            if lstTable[row]['Task'] == removeChoice:  # check if task key equals the removeChoice
                del lstTable[row]  # delete the row
                break  # break the if loop
        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif strChoice.strip() == '4':
        objFile = open('ToDoList.txt', 'w')  # open connection to file in write mode
        for row in lstTable:  # for each row lstTable
            strData1 = row['Task']  # pull task value from lstTable
            strData2 = row['Priority']  # pull priority value from lstTable
            objFile.write(strData1 + ',' + strData2 + '\n')  # write task/priority values to file
        objFile.close()
        continue
    # Step 7 - Exit program
    elif strChoice.strip() == '5':
        print("Goodbye")
        break  # and Exit the program
