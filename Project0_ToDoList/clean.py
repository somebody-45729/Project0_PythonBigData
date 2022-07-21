import re
import logging
import sys
import datetime

def main():
    logging.basicConfig(filename = "To_Do_List.log", level = logging.DEBUG, format='%(asctime)s :: %(message)s')

    print("******** TO-DO LIST ********")
    csvName = 'toDoList.csv'
    userIn = ' '
    complete = 'no'

    # Take into account 
    while complete == 'no': 
        # Cycle has to continue til user decides to close the program themselves
        while userChoice not in ("ADD TASKS", "DELETE TASKS", "QUIT"):
            userChoice = input("PLEASE SELECT FROM THE FOLLOWING: ADD TASKS, DELETE TASKS, or QUIT PROGRAM")
        
        # 3 choices: ADD, DELETE, and QUIT the program altogether
        # ALL THREE METHODS BELOW
        if userChoice == "ADD TASKS":
            addTask() 
            userChoice = input("CONTINUE OPERATIONS or QUIT PROGRAM?")
        elif userChoice = "DELETE TASKS":
            deleteTask()
            userChoice = input("CONTINUE OPERATIONS or QUIT PROGRAM?")
        else:
            print("HOPE THIS HELPS!")
            break # Assume that user has chosen to quit program

    def addTask():
        
            
