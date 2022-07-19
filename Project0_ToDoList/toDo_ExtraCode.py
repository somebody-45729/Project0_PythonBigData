# Extra class/module handler here

class input():
    def __init__(self, date, event, importance=""):
        self._date = str(date)
        self._event = str(event)
        self._importance = str(importance)

    def __str__(self):
        return "Date: " + self._date + ", Item" + self._event + ", Level of importance: " + self._importance
        