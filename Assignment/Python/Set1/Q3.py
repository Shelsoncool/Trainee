class Stest:
    def __init__(self):
        self.text=""
        
    def getString(self):
        self.text=input("Enter the String:")
        
    def printString(self):
        print(self.text.upper())
obj=Stest()
obj.getString()
obj.printString()

        
