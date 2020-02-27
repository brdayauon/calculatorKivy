import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config  #to change window size
Config.set('graphics', 'resizable', 1)

#Builder.load functions so that I can use .kv 
# string within your .py class without having to create a whole new kv file
Builder.load_string("""
<MyWidget>:# Custom button
<Button@Button>:
    font_size: 25

# Define id so I can refer to the CalcBoard
<CalcBoard>:
    id: calculator
    display: evaluationBox
    rows: 2
    padding: 5
    spacing: 3
 
    #Defining the text boxes
    BoxLayout:
        TextInput:
            id: entry
            font_size: 50
            multiline: False
        
        TextInput:
            id: entry1 
            font_size: 50
            multiline: False
        
        TextInput:
            text: "="
            id: evaluationBox
            font_size: 50 
            multiline: False 

    # Define the buttons after the two text field boxes are filled 
    BoxLayout:
        spacing: 15
        Button:                             #clear button
            text: "CLEAR"
            on_press: entry.text = ""
            on_press: entry1.text = ""
            on_press: evaluationBox = ""
        Button:                             # add button
            text: "+"
            on_press: calculator.add("+")
        Button:                             # subtract button
            text: "-"
            on_press: calculator.subtract("-")
        Button:                             # multiply button
            text: "*"
            on_press: calculator.multiply("*")
        Button:                             # divide button
            text: "/"
            on_press: calculator.divide("/")
        
""")

# Creating Layout class 
class CalcBoard(GridLayout):

    # add Function is invoked when + button is pressed 
    def add(self, text):
         entryBox1 = int(self.ids.entry.text)
         entryBox2 = int(self.ids.entry1.text)
         
         self.display.text = str(eval('entryBox1 + entryBox2'))

    # subtract Function is invoked when - button is pressed
    def subtract(self, text):
         entryBox1 = int(self.ids.entry.text)
         entryBox2 = int(self.ids.entry1.text)
        
         self.display.text = str(eval('entryBox1 - entryBox2'))

    # multiply Function is invoked when * button is pressed     
    def multiply(self, text):
         entryBox1 = int(self.ids.entry.text)
         entryBox2 = int(self.ids.entry1.text)
         
         self.display.text = str(eval('entryBox1 * entryBox2'))

    # divide Function is invoked when / button is pressed 
    def divide(self, text):
         entryBox1 = int(self.ids.entry.text)
         entryBox2 = int(self.ids.entry1.text)
         
         self.display.text = str(eval('entryBox1 / entryBox2'))



# Defining the calculator App class
class MyApp(App):
    def build(self):
        return CalcBoard()

calcApp = MyApp()
calcApp.run() 