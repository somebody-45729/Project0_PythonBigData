import re
import logging
import sys
import datetime


# NEED TO ASK HELP IN SETTING UP CONNECTION WITH .csv file read/write


def main():
    logging.basicConfig(filename = "To_Do_List.log", level = logging.DEBUG, format='%(asctime)s :: %(message)s')

    print("******** TO-DO LIST ********")
    csvName = 'toDoList.csv'
    userIn = ' '
    complete = 'CONTINUE'

    # Take into account 
    while complete == 'CONTINUE': 
        inToDo = addTask
        # Cycle has to continue til user decides to close the program themselves
        while userChoice not in ("ADD TASKS", "DELETE TASKS", "QUIT"):
            userChoice = input("PLEASE SELECT FROM THE FOLLOWING: ADD TASKS, DELETE TASKS, or QUIT PROGRAM")



        # 3 choices: ADD, DELETE, and QUIT the program altogether
        # ALL THREE METHODS BELOW
        if userChoice == "ADD TASKS":
            addTask() 
            userChoice = input("CONTINUE or QUIT?")
        elif userChoice == "DELETE TASKS":
            deleteTask()
            userChoice = input("CONTINUE or QUIT?")
        else:
            print("HOPE THIS HELPS!")
            break # Assume that user has chosen to quit program

    def addTask(): 
       # NEED TO A WAY TO HAVE THE CSV READ AND WRITE WHILE HAPPENING
        
            # focusing on the due date of task, with the task at hand, and finally the priority of said task
            date = input('Enter date which the task/event needs to be done: (ex: 11, 07, 2002)')
            day, month, year = map(int, date.split(','))
            try:
                dueDate = datetime(day, month, year)
            except ValueError:
                print("\n CANNOT EXCEPT STIRNG AS AGE, PLEASE FOLLOW FORMAT AS INDICATED ABOVE!\n")
                logging.error("Tried to enter string for date, retrying . . .")
            dueDate = str(dueDate)
            dueDate = dueDate[:10] # give the proper spacing (DD,MM,YYYY)

            # Actual item: exception hanlding not really needed?
            item = input("Enter the event/task/item that you wish to list: ")

            # Setting up actual priority levels
            priority = input("ENTER LOW, MEDIUM, or HIGH FOR PRIORITY LEVEL OF EVENT/TASK/ITEM: ")

            if priority.upper == "LOW" or priority.lower == "low":
                print(priority)
            elif priority.upper == "MEDIUM" or priority.lower == "medium":
                print(priority)
            elif priority.upper == "HIGH" or priority.lower == "high":
                print(priority)
            else:
                print("I'm sorry, please enter one of the following: low, medium, or high for priority choice")

            
     def deleteTask():
        deletion = input("Provie the index number in list to delete the associated item: ")
        deletion = int(deletion)
        # need to delete the object here?
        # - - -


if __name__ == "__main__":
    main()
