class Day:
    def __init__(self, date):
        self.date = date
        self.morning = ""
        self.afternoon = ""

    def isEmpty(self):
        return self.morning == "" and self.afternoon == ""
            

    def toString(self):
        string = str(self.date) + " - "
        if self.isEmpty():
            string += "Rien"
        if (self.morning != ""):
            string += "Matin: " + self.morning + "  "
        if (self.afternoon != ""):
            string += "Apres-Midi: " + self.afternoon
        
        return string