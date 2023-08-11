(A) KİVYMD SQLİTE İLE HESAP GİRİŞİ KİVYMD-2(farklı örnek videom içindeki😎

#py kısmı

from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.behaviors import FakeRectangularElevationBehavior
import sqlite3


from kivy.core.window import Window

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


    def login(self,user,password):
        conn = sqlite3.connect('zl.db')   
        x=conn.cursor()
        x.execute(" select * from user")
        data=x.fetchall()
        for i in data:
            if i[:][0]==user:
                    if i[:][1]==password:
                       SC.get_screen("z").ids.zc.text="👍"
                       SC.current="ll"
            else:
                SC.get_screen("z").ids.zc.text="zzzzz"
                       
       

TTApp().run()




