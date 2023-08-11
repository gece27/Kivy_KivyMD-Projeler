from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.behaviors import FakeRectangularElevationBehavior
from kivy.core.window import Window

from kivymd.uix.snackbar import Snackbar
from kivy.utils import get_color_from_hex


Window.size = (900, 700)

class Panel(MDFloatLayout,FakeRectangularElevationBehavior):
    pass


class TTApp(MDApp):
  
    def build(self):
        global SC
        SC=ScreenManager()
        SC.add_widget(Builder.load_file("main.kv"))
        SC.add_widget(Builder.load_file("ll.kv"))

        
        return SC


    def psw(self):
        if SC.get_screen("z").ids.password.password==True:
            SC.get_screen("z").ids.password.password=False
            SC.get_screen("z").ids.l.icon="eye"
        else:
            SC.get_screen("z").ids.password.password=True
            SC.get_screen("z").ids.l.icon="eye-off"

    
    


    def login(self,username,password):
        from firebase import firebase
        firebase=firebase.FirebaseApplication('https://normal-1f2de-default-rtdb.firebaseio.com/',None)

        rs=firebase.get('Users/first','')
        
        if rs["name"]==username:
                if rs["password"]==password:
                    SC.current="new"

        else:
            snb=Snackbar(text="you entered wrong value",bg_color=get_color_from_hex("#67DA49"))
            snb.open()
                            




    def delete(self):
        SC.get_screen("z").ids.password.password=False 
        SC.get_screen("z").ids.password.text=" "
         
        
        SC.get_screen("z").ids.username.text=" "
                       
       

TTApp().run()
