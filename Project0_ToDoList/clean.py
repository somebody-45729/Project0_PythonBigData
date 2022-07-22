import re
import logging
import sys
import datetime
import csv

# NEED TO ASK HELP IN SETTING UP CONNECTION WITH .csv file read/write


def main():
    logging.basicConfig(filename = "To_Do_List.log", level = logging.DEBUG, format='%(asctime)s :: %(message)s')

    print("******** TO-DO LIST ********")
    csvName = 'toDoList.csv'
    userChoice = ' '
    complete = 'CONTINUE'

    # Take into account 
    while complete == 'CONTINUE': 
        # Cycle has to continue til user decides to close the program themselves
        while userChoice not in ("ADD TASKS", "DELETE TASKS", "QUIT"):
            userChoice = input("PLEASE SELECT FROM THE FOLLOWING: ADD TASKS, DELETE TASKS, or QUIT PROGRAM")

        # 3 choices: ADD, DELETE, and QUIT the program altogether
        # ALL THREE METHODS BELOW
        if userChoice.upper() == "ADD TASKS":
            addTask() 
            userChoice = input("CONTINUE or QUIT?")
        elif userChoice.upper() == "DELETE TASKS":
            deleteTask()
            userChoice = input("CONTINUE or QUIT?")
        elif userChoice.upper() == "QUIT":
            print("THANK YOU")
            break
        else:
            print("HOPE THIS HELPS!")
            break # Assume that user has chosen to quit program

    def addTask(): 
       # NEED TO A WAY TO HAVE THE CSV READ AND WRITE WHILE HAPPENING
       # focusing on the due date of task, with the task at hand, and finally the priority of said task
    
    
    def deleteTask():
