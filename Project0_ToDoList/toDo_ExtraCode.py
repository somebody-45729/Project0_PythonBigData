# Extra class/module handler here

class input():
    def __init__(self, date, event, priority=""):
        self._date = str(date)
        self._event = str(event)
        self._priority = str(priority)

    def __str__(self):
        return "Date: " + self._date + ", Item" + self._event + ", Level of importance: " + self._priority
        