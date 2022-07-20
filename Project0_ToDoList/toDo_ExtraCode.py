# Extra class/module handler here

class input():
    def __init__(self, date, event, priority=""):
        self._date = str(date)
        self._event = str(event)
        self._priority = str(priority)

    def __str__(self):
        return "Date: " + self._date + ", Item" + self._event + ", Level of importance: " + self._priority
        
class Event(input):
    def run(self):
        print("A New input for the List!")

class LOW(input):
    def priority(self):
        print("LOW priority for this case!")

class MEDIUM(input):
    def priority(self):
        print("MEIDUM priority for this case!")

class HIGH(input):
    def priority(self):
        print("HIGH priority for this case!")
    