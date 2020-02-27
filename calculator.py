import kivy
from kivy.app import App
from kivy.lang import Builder


# for making multiple bttons to arranging 
# them we are using this 
from kivy.uix.gridlayout import GridLayout

# for the size of window 
from kivy.config import Config

# Setting size to resizable 
Config.set('graphics', 'resizable', 1)

#Builder.load functions so that I can use .kv 
# string within your .py class without having to create a whole new kv file
Builder.load_string("""
<MyWidget>:# Custom button
<Button@Button>:
    font_size: 32

# Define id so I can refer to the CalcGridLayout
# class functions
# Display points to the entry widget
<CalcGridLayout>:
    id: calculator
    display: evaluationBox
    rows: 2
    padding: 5
    spacing: 3
 
    # Where input is displayed
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

    # When buttons are pressed update the entry
    BoxLayout:
        spacing: 15
        Button: 
            text: "CLEAR"
            on_press: entry.text = ""
            on_press: entry1.text = ""
            on_press: evaluationBox = ""
        Button:
            text: "+"
            on_press: calculator.add("+")
        Button:
            text: "-"
            on_press: calculator.subtract("-")
        Button:
            text: "*"
            on_press: calculator.multiply("*")
        Button:
            text: "/"
            on_press: calculator.divide("/")
        
""")

# Creating Layout class 
class CalcGridLayout(GridLayout):

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
        return CalcGridLayout()

calcApp = MyApp()
calcApp.run() 