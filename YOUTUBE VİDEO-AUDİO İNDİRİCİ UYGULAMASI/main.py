from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from pytube import YouTube #!

class Gece(MDApp):
    def build(self):
        self.title="video-audio downloader"
        global sc
        sc=ScreenManager()
        sc.add_widget(Builder.load_file("main.kv"))
        
        return sc
        
    def video(self):
        self.v=1
        
    def audio(self):
        self.v=2 

    def dwn(self,url):
       if self.v==1:
            video=YouTube(url)
            streams=video.streams.filter().first()
            
            print("dowland...")
            print("filepath:",streams.download())
            print("finished")
            sc.get_screen("xx").ids.title.text=video.title
            sc.get_screen("xx").ids.length.text=str(video.length)
            

       if self.v==2:
            video=YouTube(url)
            streams=video.streams.filter(only_audio=True).first()
            print("dowland...")
            print("filepath:",streams.download())
            print("finished")
            sc.get_screen("xx").ids.title.text=video.title
            sc.get_screen("xx").ids.length.text=str(video.length)



if __name__=='__main__':
    Gece().run()
