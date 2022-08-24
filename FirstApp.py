from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class ChildApp(GridLayout):
    def __init__(self, **kwargs):
        super(ChildApp, self).__init__()
        self.cols = 2

        self.add_widget(Label(text='Username'))
        self.u_name = TextInput()
        self.add_widget(self.u_name)

        self.add_widget(Label(text='Email'))
        self.u_email = TextInput()
        self.add_widget(self.u_email)

        self.add_widget(Label(text='Password'))
        self.u_password = TextInput()
        self.add_widget(self.u_password)

        self.press = Button(text='Click me')
        self.press.bind(on_press=self.click_me)
        self.add_widget(self.press)

    def click_me(self, instance):
        print("Username:  " + self.u_name.text)
        print("Email:  " + self.u_email.text)
        print("Password: " + self.u_password.text)
        print("")


class ParentApp(App):
    def build(self):
        return ChildApp()


if __name__ == "__main__":
    ParentApp().run()
