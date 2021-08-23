import firebaseloginscreen
import requests
import json

from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.lang import Builder
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDFillRoundFlatButton
from kivy.uix.screenmanager import Screen, ScreenManager


from helper import screen_helper


# screen_helper = """
# ScreenManager:
#     MenuScreen:
#     ProfileScreen:
#
# <MenuScreen>
#
#     name: 'menu'
#     MDFillRoundFlatButton:
#         text: 'Login'
#         pos_hint: {'center_x':0.5, 'center_y':0.2}
#         on_press: root.manager.current = 'profile'
#     MDTextField:
#         hint_text: "Enter Mobile Number"
#         pos_hint: {'center_x':0.5, 'center_y':0.5}
#         size_hint_x: None
#         width: 300
#
# <ProfileScreen>
#     name: 'profile'
#     MDLabel:
#         text:'Wlcome'
#         halign:'center'
# """
#

class MenuScreen(Screen):
    pass


class ProfileScreen(Screen):
    pass


sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(MenuScreen(name='profile'))


class Myapp(MDApp):
    firebase_url = "https://kivo-6c302-default-rtdb.firebaseio.com/.json"
    def build(self):
        screen = Screen()
        button = MDFillRoundFlatButton(text='Login', pos_hint={'center_x': 0.5, 'center_y': 0.2},
                                       on_release=self.show_data)
        self.username = MDTextField(hint_text="Enter Mobile Number",
                                    pos_hint={'center_x': 0.5, 'center_y': 0.5},
                                    size_hint_x=None, width=300)

        # screen.add_widget(username)
        # self.username = Builder.load_string(screen_helper)
        screen.add_widget(self.username)
        screen.add_widget(button)
        return screen

    def show_data(self, obj):
        json_data = '{"url":"google.com", "age":"15 yr old"}'
        print(self.username.text)
        res = requests.patch(url=self.firebase_url, json= json.loads(json_data))
        print(res)


Myapp().run()
