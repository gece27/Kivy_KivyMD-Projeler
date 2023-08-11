import kivy 
from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.uix.gridlayout import GridLayout
 
from kivy.config import Config
Config.set('graphics', 'resizable', 1)

Window.size=(400,500)

class CalcGridLayout(GridLayout):
  
    #main function /asıl fonskiyon
    def calculate(self, calculation):
        if calculation:
            try:
                self.display.text = str(eval(calculation)) #EVAL()! İŞARETLERİ TANICAK İŞLEM OLUR
            except Exception:
                self.display.text = "Error"
  

class CalculatorApp(MDApp):
  
    def build(self):
        global ekran
        ekran=ScreenManager()
        ekran.add_widget(Builder.load_file("hsp.kv"))
        
        return ekran
       

if __name__=='__main__':
  CalculatorApp().run()
