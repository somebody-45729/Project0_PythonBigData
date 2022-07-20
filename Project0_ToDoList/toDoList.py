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
    print("*** INSTRUCTIONS ON PROPER INPUT ***")
    print("*** DATES NEED NOT APPLY, AUTO-DETECTED ***")
    print()

def saveEvent(fname, lst_toDo):
    '''
    Have the following saved into a .csv file

    returns none . . . ?
    '''

def load_Event(fname) -> list:
    '''
    Return list of events
    '''

def insert_Event() -> input:
    # Prompting user for information
    # Date - Event - Level of Importance specifically
    
    print("*** Entering: TO-DO LIST ***")
    # Start with the item first
    print("\nPlease enter the item/event which you wish to save!")
    while True:
        try:
            item = input("\nEnter item/event:\n>>>")
            check = re.search("", item)

            print(item)
            print(check)
            if check == None:
                raise ValueError
        except ValueError as ve:
            print("\nWe're sorry, but please enter an event/item, your response was blank!")
            logging.error("Empty response, trying again")
        else:
            break

    # Then the date associated with above item/event
    print("\nPlease enter the date for the item/event to be remembered by:\n>>>")

    insertDate = input("Date: (in DD/MM/YYYY) ")
    day, month, year = insertDate.split('/')
    validDate = True
    while True:
        try:
            datetime.datetime(int(day), int(month), int(year))
        except ValueError:
            validDate = False
        if validDate == False:
            print("Date input is not valid, please try again")
        else:
            print()
            break

    chosenDate = datetime.datetime.strptime(insertDate, "%d/%m%Y").date()
    print(chosenDate.strftime('%d/%B/%Y'))
    

    # Lvel of importance (3 Different Priorities: Low, Medium, High)
    


    while True:
        priority = input("\nEnter the level of priority (LOW, MEDIUM, HIGH):\n>>>")

        if priority.upper() == "LOW":
            print(priority)
        elif priority.upper() == "MEDIUM":
            print(priority)
        elif priority.upper() == "HIGH":
            print(priority)
        else:
            print("Please enter one of the following: LOW MEDIUM or HIGH")

    

