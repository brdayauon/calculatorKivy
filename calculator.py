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
    display: entry
    rows: 6
    padding: 10
    spacing: 10
 
    # Where input is displayed
    BoxLayout:
        TextInput:
            id: entry
            font_size: 40
            multiline: False

    # When buttons are pressed update the entry
    BoxLayout:
        spacing: 10
        Button:
            text: "+"
            on_press: entry.text += self.text
        Button:
            text: "-"
            on_press: entry.text += self.text
        Button:
            text: "*"
            on_press: entry.text += self.text
        Button:
            text: "/"
            on_press: entry.text += self.text

    # When equals is pressed pass text in the entry
    # to the calculate function
    BoxLayout:
        spacing: 10
        Button:
            text: "Clear"
            on_press: entry.text = ""
       
        Button:
            text: "="
            on_press: calculator.calculate(entry.text)
        
    BoxLayout:
        Button:
            font_size: 15
            text: "Scientific calculator"
            on_press: entry.text = ""

""")

# Creating Layout class 
class CalcGridLayout(GridLayout):

    # Function called when equals is pressed 
    def calculate(self, calculation):
        if calculation:
            try:
                # Solve formula and display it in entry 
                # which is pointed at by display 
                self.display.text = str(eval(calculation))
            except Exception:
                self.display.text = "Error"


# Creating App class
class MyApp(App):
    def build(self):
        return CalcGridLayout()

    # creating object and running it


calcApp = MyApp()
calcApp.run() 