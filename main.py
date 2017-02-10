import kivy
kivy.require("1.9.1") #replace with current kivy version

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.properties import NumericProperty, ReferenceListProperty, \
                            ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock

def gcd(a,b):
    #Compute the greatest common divisor of a and b
    while b > 0:
        a, b = b, a % b
    return a
    
def lcm(a, b):
    #Compute the lowest common multiple of a and b
    return a * b / gcd(a, b)

class CalculatorWidget(Widget):   
    buttons = []
    label = None
    dic = {"/":"/", "^": "**", }#"pi": pi, "e": e, "ln":"log(", "lg(":"log10(",}
    calc, display, ans = "", "", "0"
    buttons.append(Button(text="1", center_x=1100,  center_y=800, height=200, width=200))
    buttons.append(Button(text="2", center_x=1300, center_y=800, height=200, width=200))
    buttons.append(Button(text="3", center_x=1500, center_y=800, height=200, width=200))
    buttons.append(Button(text="/", center_x=1700,  center_y=800, height=200, width=200))
    buttons.append(Button(text="4", center_x=1100, center_y=600, height=200, width=200))
    buttons.append(Button(text="5", center_x=1300, center_y=600, height=200, width=200))
    buttons.append(Button(text="6", center_x=1500,  center_y=600, height=200, width=200))
    buttons.append(Button(text="-", center_x=1700, center_y=600, height=200, width=200))
    buttons.append(Button(text="7", center_x=1100, center_y=400, height=200, width=200))
    buttons.append(Button(text="8", center_x=1300, center_y=400, height=200, width=200))
    buttons.append(Button(text="9", center_x=1500, center_y=400, height=200, width=200))
    buttons.append(Button(text="+", center_x=1700, center_y=400, height=200, width=200))
    buttons.append(Button(text="*", center_x=1100,  center_y=200, height=200, width=200))
    buttons.append(Button(text="0", center_x=1300, center_y=200, height=200, width=200))
    buttons.append(Button(text="=", center_x=1600, center_y=200, height=200, width=400))

    """buttons.append(Button(text="%",    center_x=300, center_y=225, height=50, width=50))
    buttons.append(Button(text=".",    center_x=350, center_y=225, height=50, width=50))
    buttons.append(Button(text="(",    center_x=400, center_y=225, height=50, width=50))
    buttons.append(Button(text=")",    center_x=450, center_y=225, height=50, width=50))
    buttons.append(Button(text="^",    center_x=300, center_y=275, height=50, width=50))
    buttons.append(Button(text="pi",   center_x=350, center_y=275, height=50, width=50))
    buttons.append(Button(text="e",    center_x=400, center_y=275, height=50, width=50))
    buttons.append(Button(text="ln(",   center_x=450, center_y=275, height=50, width=50))
    buttons.append(Button(text="sin(",  center_x=300, center_y=325, height=50, width=50))
    buttons.append(Button(text="cos(",  center_x=350, center_y=325, height=50, width=50))
    buttons.append(Button(text="tan(",  center_x=400, center_y=325, height=50, width=50))
    buttons.append(Button(text="lg(",   center_x=450, center_y=325, height=50, width=50))
    buttons.append(Button(text="asin(", center_x=300, center_y=375, height=50, width=50))
    buttons.append(Button(text="acos(", center_x=350, center_y=375, height=50, width=50))
    buttons.append(Button(text="atan(", center_x=400, center_y=375, height=50, width=50))
    buttons.append(Button(text="exp(",  center_x=450, center_y=375, height=50, width=50))

    buttons.append(Button(text="ANS",    center_x=550, center_y=225, height=50, width=100))
    buttons.append(Button(text=",",    center_x=625, center_y=225, height=50, width=50))
    buttons.append(Button(text="1j",    center_x=675, center_y=225, height=50, width=50))
    buttons.append(Button(text="lcm(",    center_x=525, center_y=275, height=50, width=50))
    buttons.append(Button(text="gcd(",   center_x=575, center_y=275, height=50, width=50))
    buttons.append(Button(text="atan2(",    center_x=625, center_y=275, height=50, width=50))
    #buttons.append(Button(text="ln(",   center_x=675, center_y=275, height=50, width=50))
    buttons.append(Button(text="sinh(",  center_x=525, center_y=325, height=50, width=50))
    buttons.append(Button(text="cosh(",  center_x=575, center_y=325, height=50, width=50))
    buttons.append(Button(text="tanh(",  center_x=625, center_y=325, height=50, width=50))
    #buttons.append(Button(text="lg(",   center_x=675, center_y=325, height=50, width=50))
    buttons.append(Button(text="asinh(", center_x=525, center_y=375, height=50, width=50))
    buttons.append(Button(text="acosh(", center_x=575, center_y=375, height=50, width=50))
    buttons.append(Button(text="atanh(", center_x=625, center_y=375, height=50, width=50))
    #buttons.append(Button(text="exp(",  center_x=675, center_y=375, height=50, width=50))"""
    def callback(self, instance):
        self.dic["ANS"] = self.ans
        if len(self.display) > 0 and self.display[0] == "=": 
            self.display, self.calc = "", ""
        if instance.text == "=":
            try:
                self.ans = str(eval(self.calc))
                print self.ans
                self.display = "=" + self.ans
            except SyntaxError:
                print "SyntaxError"  
                self.display = "=SyntaxError"
            except ZeroDivisionError:
                print "ZeroDivisionError"
                self.display = "=ZeroDivisonError"  
        elif instance.text == "/":
            #if "." not in self.calc:
            #    self.calc += "."
            self.calc += instance.text
            self.display += instance.tex     
        elif instance.text in self.dic:
            self.calc += str(self.dic[instance.text])
            self.display += instance.text 
        else: 
            self.calc += instance.text
            self.display += instance.text
        print self.calc, self.display
    def update(self, event):
        self.label.text = self.display

class CalculatorApp(App):  
    def build(self):
        widget = CalculatorWidget()
        for button in widget.buttons:
            button.bind(on_press=widget.callback)
            widget.add_widget(button)
        Clock.schedule_interval(widget.update, 1.0/60.0)
        return widget

        

if __name__ == '__main__':
    CalculatorApp().run()
