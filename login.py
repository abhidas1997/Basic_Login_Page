from kivymd.app import MDApp
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDLabel
from kivy.uix.screenmanager import Screen, ScreenManager


# Registration Page
class MyRegister(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.firstname_txt = MDTextField(mode="rectangle", hint_text="First Name",
                                         pos_hint={'center_x': 0.5, 'center_y': 0.9},
                                         size_hint= (0.7,0.5),
                                         icon_left="account")

        self.lastname_txt = MDTextField(mode="rectangle", hint_text="Last Name",
                                        pos_hint={'center_x': 0.5, 'center_y': 0.8},
                                        size_hint= (0.7,0.5),
                                        icon_left="account")

        self.phone_txt = MDTextField(mode="rectangle", hint_text="Phone",
                                     pos_hint={'center_x': 0.5, 'center_y': 0.7},
                                     size_hint= (0.7,0.5),
                                     icon_left="phone")

        self.email_txt = MDTextField(mode="rectangle", hint_text="Email",
                                     pos_hint={'center_x': 0.5, 'center_y': 0.6},
                                     size_hint= (0.7,0.5),
                                     icon_left="email")

        self.address_txt = MDTextField(mode="rectangle", hint_text="Address",
                                       pos_hint={'center_x': 0.5, 'center_y': 0.5},
                                       size_hint= (0.7,0.5),
                                       icon_left="earth")

        self.country_text = MDTextField(mode="rectangle", hint_text="Country",
                                        pos_hint={'center_x': 0.32, 'center_y': 0.4},
                                        size_hint=(0.34, 0.5),icon_left='map')

        self.city_txt = MDTextField(mode="rectangle", hint_text="City",
                                    pos_hint={'center_x': 0.68, 'center_y': 0.4},
                                    size_hint=(0.34,0.5),
                                    icon_left="city")

        self.submit_btn = MDRectangleFlatButton(text="Submit",
                                                pos_hint={'center_x': 0.5, 'center_y': 0.3},
                                                on_release=self.validate)

        button_2 = MDRectangleFlatButton(text="Already has a account",
                                         pos_hint={'center_x': 0.5, 'center_y': 0.2},
                                         size_hint_x=0.5,
                                         on_release=self.swtich_login)
        self.add_widget(self.firstname_txt)
        self.add_widget(self.lastname_txt)
        self.add_widget(self.phone_txt)
        self.add_widget(self.email_txt)
        self.add_widget(self.address_txt)
        self.add_widget(self.country_text)
        self.add_widget(self.city_txt)
        self.add_widget(self.submit_btn)
        self.add_widget(button_2)

    def swtich_login(self, instance):
        self.firstname_txt.text = ""
        self.lastname_txt.text = ""
        self.phone_txt.text = ""
        self.email_txt.text = ""
        self.address_txt.text = ""
        self.city_txt.text = ""
        self.country_text.text = ""
        self.manager.current = 'login'
        self.manager.transition.direction = "right"

    def validate(self, instance):
        self.cancel_success = MDRectangleFlatButton(text="Cancel", on_release=self.cancel_success_message)
        self.success_message = MDDialog(title="Successful", text="Registration Successfully Submitted",
                                        buttons=[self.cancel_success],
                                        )
        if (self.firstname_txt.text != "" and self.lastname_txt.text != "" and self.phone_txt.text != "" and
                self.email_txt.text != "" and self.address_txt.text != "" and self.city_txt.text != "" and
                self.country_text.text != ""):
            self.firstname_txt.text = ""
            self.lastname_txt.text = ""
            self.phone_txt.text = ""
            self.email_txt.text = ""
            self.address_txt.text = ""
            self.city_txt.text = ""
            self.country_text.text = ""
            self.success_message.open()


        else:
            self.cancel_failed = MDRectangleFlatButton(text="Cancel", on_release=self.cancel_failed_message)
            self.failed_message = MDDialog(title="Failed", text="Registration Failed, Check entry data again",
                                           buttons=[self.cancel_failed])
            self.failed_message.open()

    def cancel_success_message(self, instance):
        self.success_message.dismiss()

    def cancel_failed_message(self, instance):
        self.failed_message.dismiss()


# Login Page
class MyGrid(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.username = MDTextField(hint_text="Enter Username",
                                    pos_hint={'center_x': 0.5, 'center_y': 0.67},
                                    mode="rectangle", size_hint = (0.7,0.5))
        self.password = MDTextField(hint_text="Password",
                                    pos_hint={'center_x': 0.5, 'center_y': 0.55},
                                    mode="rectangle", size_hint = (0.7,0.5))

        self.button = MDRectangleFlatButton(text="Submit",
                                            pos_hint={'center_x': 0.5, 'center_y': 0.4},
                                            size_hint=(None, None), size=("380dp", "80dp"),
                                            on_release=self.on_click)

        self.button_new = MDRectangleFlatButton(text="Register",
                                                pos_hint={'center_x': 0.5, 'center_y': 0.3},
                                                size_hint=(None, None), size=("380dp", "80dp"),
                                                on_release=self.switch_register)

        self.add_widget(self.username)
        self.add_widget(self.password)
        self.add_widget(self.button)
        self.add_widget(self.button_new)

    def on_click(self, instance):
        if self.username.text != "" and self.password.text != "":
            self.message_text_login = MDLabel(text="Successfully Login")
            self.close_popup_login = MDFlatButton(text="Close", on_release=self.close_login)

            self.popup_success = MDDialog(title="Message", text=self.message_text_login.text,
                                          buttons=[self.close_popup_login])
            self.username.text = ""
            self.password.text = ""
            self.popup_success.open()
        else:
            self.message_text = MDLabel(text="Login Failed")
            self.close_popup = MDFlatButton(text="Close", on_release=self.close)

            self.popup = MDDialog(title="Message", text=self.message_text.text,
                                  buttons=[self.close_popup])
            self.popup.open()

    def close_login(self, instance):
        self.popup_success.dismiss()

    def close(self, instance):
        self.popup.dismiss()

    def switch_register(self, instance):
        self.username.text = ""
        self.password.text = ""
        self.manager.current = 'register'
        self.manager.transition.direction = "left"


# Main Function
class Myapp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "DeepPurple"
        self.theme_cls.primary_hue = "500"
        self.theme_cls.theme_style = "Dark"
        sc = ScreenManager()
        sc.add_widget(MyGrid(name="login"))
        sc.add_widget(MyRegister(name="register"))
        return sc


if __name__ == "__main__":
    Myapp().run()
