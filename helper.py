screen_helper = """
ScreenManager:
    MenuScreen:
    ProfileScreen:

<MenuScreen>
    name: 'menu'
    MDTextField:
        hint_text: "Enter Mobile Number"
        pos_hint: {'center_x':0.5, 'center_y':0.5}
        size_hint_x: None
        width: 300

<ProfileScreen>
    name: 'profile'
    MDLabel:
        text:'Wlcome'
        halign:'center'
"""

