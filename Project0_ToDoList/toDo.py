import re
import logging
import sys
import datetime
import csv

# NEED TO ASK HELP IN SETTING UP CONNECTION WITH .csv file read/write


def main():
    logging.basicConfig(filename = "To_Do_List.log", level = logging.DEBUG, format='%(asctime)s :: %(message)s')

    print("******** TO-DO LIST ********")
    
    fname = "toDoList.csv"
    lst_toDo = []
    lst_toDo = load_Tasks(fname)
    logging.info("Loading tasks into the list....")

    
    
