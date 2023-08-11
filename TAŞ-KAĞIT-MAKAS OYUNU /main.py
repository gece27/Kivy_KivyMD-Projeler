from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp

#rock->taş  #paper->kağıt #scissors->makas

import random
from kivy.uix.button import ButtonBehavior
from kivymd.utils.fitimage import FitImage

class Karma(ButtonBehavior,FitImage): #button
    pass

liste=["taş","kağıt","makas"] #rock->taş  #paper->kağıt #scissors->makas
oyuncuskor=0
pcskor=0

# liste,oyuncuskor,pcskor ->global değişkenler(variables)

class Login(MDApp):
    

    def build(self):
        global ekran
        ekran=ScreenManager()
        ekran.add_widget(Builder.load_file("main.kv"))
        
        return ekran

    def tas(self):
        global gamesecim
        gamesecim="taş"
       
        self.kiyasla()

    def kagit(self):
        global gamesecim
        gamesecim="kağıt"
        self.kiyasla()

    def makas(self):
        global gamesecim
        gamesecim="makas"
        self.kiyasla()

    def kiyasla(self):
        global liste
        global oyuncuskor
        global pcskor
        global gamesecim #oyuncu seçimi pass
        random.shuffle(liste)
        

        if liste[0]=="taş" and gamesecim=="makas":
            ekran.get_screen("xx").ids.pcsecim.source="tas.png"
            ekran.get_screen("xx").ids.benimsecim.source="makas.png"
            pcskor+=1
            ekran.get_screen("xx").ids.pcpuan.text=f"pc:{str(pcskor)}"
        
        if liste[0]=="taş" and gamesecim=="kağıt":
            ekran.get_screen("xx").ids.pcsecim.source="tas.png"
            ekran.get_screen("xx").ids.benimsecim.source="kagit.png"
            oyuncuskor+=1
            ekran.get_screen("xx").ids.benimpuan.text=f"oyuncu:{str(oyuncuskor)}"

        ###
        if liste[0]=="makas" and gamesecim=="kağıt":
            ekran.get_screen("xx").ids.pcsecim.source="makas.png"
            ekran.get_screen("xx").ids.benimsecim.source="kagit.png"
            pcskor+=1
            ekran.get_screen("xx").ids.pcpuan.text=f"pc:{str(pcskor)}"

        if liste[0]=="makas" and gamesecim=="taş":
            ekran.get_screen("xx").ids.pcsecim.source="makas.png"
            ekran.get_screen("xx").ids.benimsecim.source="tas.png"
            oyuncuskor+=1
            ekran.get_screen("xx").ids.benimpuan.text=f"oyuncu:{str(oyuncuskor)}"

        ###
        if liste[0]=="kağıt" and gamesecim=="taş":
            ekran.get_screen("xx").ids.pcsecim.source="kagit.png"
            ekran.get_screen("xx").ids.benimsecim.source="tas.png"
            pcskor+=1
            ekran.get_screen("xx").ids.pcpuan.text=f"pc:{str(pcskor)}"

        if liste[0]=="kağıt" and gamesecim=="makas":
            ekran.get_screen("xx").ids.pcsecim.source="kagit.png"
            ekran.get_screen("xx").ids.benimsecim.source="makas.png"
            oyuncuskor+=1
            ekran.get_screen("xx").ids.benimpuan.text=f"oyuncu:{str(oyuncuskor)}"

if __name__=='__main__':
    Login().run()
