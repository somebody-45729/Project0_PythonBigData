# Extra class/module handler here

class input():
    def __init__(self, date, item, importance=""):
        self._date = str(date)
        self._item = str(item)
        self._importance = str(importance)

    def __str__(self):
        return ""