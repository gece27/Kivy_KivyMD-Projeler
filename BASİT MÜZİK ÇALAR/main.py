#    ***NORMAL PROGRAMMER***
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.core.audio import SoundLoader
from kivy.uix.behaviors import ButtonBehavior
from kivymd.utils.fitimage import FitImage
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.behaviors import FakeRectangularElevationBehavior


class Card(MDFloatLayout,FakeRectangularElevationBehavior):
    pass

class Tus(ButtonBehavior,FitImage):
  pass
        

class MusicApp(MDApp):
    def build(self):
        global screen
        screen=ScreenManager()
        screen.add_widget(Builder.load_file("es.kv"))

        self.music_file = "sarkı6.mp3"
        self.music_obj = None
        return screen 

    def play(self,value):
        self.music_obj = SoundLoader.load(self.music_file)
        if self.music_obj:
            print(self.music_obj.source)
            print(self.music_obj.length)
            screen.get_screen("xx").ids.song_title.text = self.music_file.strip(".mp3")
            screen.get_screen("xx").ids.slider.max = self.music_obj.length
            self.music_obj.play()
            self.music_obj.seek(value)
        
        

    def change(self, value):
        if self.music_obj is not None:
            self.music_obj.play()
            self.music_obj.seek(value)


    def stop(self,value):
        if self.music_obj is not None:
            self.music_obj.stop()
            self.music_obj.seek(value)
  

	    

MusicApp().run()
