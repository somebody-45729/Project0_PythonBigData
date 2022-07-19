# This case will handle as being my main() class + other necessities
import re
import logging
import toDo_ExtraCode

# Need to import for case of date + time related items
import sys
import datetime

# Need to call methods(?)

def main():
    logging.basicConfig(filename = "To_Do_List.log", level = logging.DEBUG, format='%(asctime)s :: %(message)s')
    
    print("*** TO-DO LIST ***")
    fname = "toDoList.csv"
    lst_toDo = []
    lst_toDo = load_Event(fname)
    
def instruct():
    '''
    This function will appear first to remind user what the proper inputs are
    '''

def saveEvent():
    '''
    Have the following saved into a .csv file

    returns none . . . ?
    '''
    with open(fname)

def load_Event(fname) -> list:
    '''
    Return list of events
    '''

def insert_Event() -> input:
    '''
    Load into selection
    '''

