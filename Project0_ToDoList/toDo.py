import re
import logging
import sys
import datetime
import csv

from toDo_ExtraCode import toDo_Task, user

# NEED TO ASK HELP IN SETTING UP CONNECTION WITH .csv file read/write


def main():
    logging.basicConfig(filename = "To_Do_List.log", level = logging.DEBUG, format='%(asctime)s :: %(message)s')

    print("******** TO-DO LIST ********")
    
    csvName = "toDoList.csv"
    lst_toDo = []
    lst_toDo = load_Task(csvName)
    logging.info("Loading tasks into the list....")

    while(True):
        toDo = insert_Task()
        if toDo == None:
            break
        logging.info("Inserted new task!")
        lst_toDo.append(toDo)

    for list in lst_toDo:
        print(list)
    
    save_Task(csvName, lst_toDo)
    logging.info("Saving Task to " + csvName)
    print("\n\n")

def save_Task(csvName, lst_toDo):
    '''
    Save all submitted tasks to the csv file

    No return for this case
    '''
    with open(csvName, "w") as f:
        for toDo in lst_toDo:
            if type(toDo) == user:
                f.write("Task, " + toDo._task + "," + str(toDo._date) + "," + toDo._priority + ",\n")
            else:
                pass


def load_Task(csvName):
    '''
    Load into the list, return the list
    '''
    lst_toDo = []

    with open(csvName, "r") as f:
        for row in f:
            infoLine = row.split(',')
            if infoLine[0] == "user":
                toDo = user(infoLine[1], infoLine[2], infoLine[3])
            else:
                toDo = None

            if toDo != None:
                lst_toDo.append(toDo)
    return lst_toDo

def insert_Task() -> toDo_Task:
    
