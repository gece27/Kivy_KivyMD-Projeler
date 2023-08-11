from kivymd.app import MDApp
from kivy.lang import Builder
from plyer import filechooser
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.metrics import dp
from kivymd.uix.datatables import MDDataTable

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
						

		def add_datatable(self):
			import pandas as pd
			data=pd.read_excel(self.data)
			cols=data.columns.values #sütun değerleri
			values=data.values #değerler
			self.data_tables = MDDataTable(
				use_pagination=True,
				size_hint=(0.9, 0.8),
				column_data=[
					(col, dp(30))
					for col in cols
				],
				row_data=values
			)
			ekran.get_screen("zz").ids.ekle.add_widget( self.data_tables)
		


	
if __name__=='__main__':
    Tablo().run()
