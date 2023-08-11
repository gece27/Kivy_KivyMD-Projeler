from kivymd.app import MDApp
from kivy.lang import Builder
from plyer import filechooser
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.metrics import dp
from kivymd.uix.datatables import MDDataTable
import sqlite3
class Tablo(MDApp):
			

                def __init__(self, **kwargs):
                    super().__init__(**kwargs)
                    self.data_tables = None

                def build(self):
                    global ekran
                    ekran=ScreenManager()
                    ekran.add_widget(Builder.load_file("ee.kv"))
                    return ekran

                
                
                def file_chooser(self):
                        filechooser.open_file(on_selection=self.xx)
                
                def xx(self,selection):
                        if selection:
                                self.data=selection[0] #class içinde data değişkeni ayzdım baska fonksta kullanma adına
                                    
                                vt = sqlite3.connect(self.data)
                                im = vt.cursor()
                                result = vt.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
                                table_names = sorted(list(zip(*result))[0])
                                im.execute(f"select * from {table_names[0]}") #TABLO ISMINE ULASMA
                                self.cols=list(map(lambda x: x[0], im.description))	

                                ekran.get_screen("zz").ids.yazı.text=selection[0]							

                


                def add_datatable(self):
                        import sqlite3
                        vt = sqlite3.connect(self.data)
                        im = vt.cursor()
                        result = vt.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
                        table_names = sorted(list(zip(*result))[0])
                        im.execute(f"select * from {table_names[0]}")
                        
                        
                        veri=im.fetchall()
                        
                        
                        self.data_tables = MDDataTable(
                            size_hint=(0.5, 0.5),
                            use_pagination=True,
                            check=True,
                            column_data=[
                                (col, dp(30))
                                for col in self.cols
                            ],
                            row_data=[
                                (
                                i[:][0],
                                i[:][1],
                                i[:][2],
                                
                                )
                                for i in veri  
                            ],


                        )
                        
                        ekran.get_screen("zz").ids.ekle.add_widget( self.data_tables)
        

            

	
if __name__=='__main__':
    Tablo().run()
