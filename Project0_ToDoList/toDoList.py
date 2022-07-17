# This case will handle as being my main() class + other necessities
import re
import logging
import toDo_ExtraCode

# Need to import for case of date + time related items
import sys
import datetime

# Need to call methods(?)

def main():
    logging.basicConfig(filename = "To_Do_List.log", leve = logging.DEBUG, format='%(asctime)s :: %(message)s')
    
    print("*** TO-DO LIST ***")

    fname = "toDoList.csv"
    
    