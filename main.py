from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton, MDRectangleFlatIconButton
from kivy.core.window import Window
from kivymd.uix.imagelist import MDSmartTile

class HomeHub(MDApp):
    Window.size = (600, 840)

    def build(self):
        boxLayout = MDBoxLayout(
            orientation='vertical',
            spacing=15,
            pos_hint={'center_x': 0.5, 'center_y': 1}
        )
        botao = MDRectangleFlatIconButton(
            text='LOGIN',
            icon='home',
            pos_hint={'center_x': 0.5, 'center_y': 0}
        )

        boxLayout.add_widget(botao)


        return boxLayout

HomeHub().run()