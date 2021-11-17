from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
class loginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        label1=Label(text="Эл. Почта:")
        emailInput=TextInput()
        label2=Label(text="Пароль")
        password=TextInput()
        superMainLayout=BoxLayout(orientation="vertical")
        superMainLayout.add_widget(label1)
        superMainLayout.add_widget(emailInput)
        superMainLayout.add_widget(label2)
        superMainLayout.add_widget(password)
        layoutForgotPassword=BoxLayout(orientation="horizontal")
        forgotPassword=Button(text="Забыл пароль")
        enter=Button(text="Войти")
        layoutForgotPassword.add_widget(forgotPassword)
        layoutForgotPassword.add_widget(enter)
        superMainLayout.add_widget(layoutForgotPassword)
        self.add_widget(superMainLayout)

class mainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        mainLayout=BoxLayout()
        button1=Button(text="Войти")
        button1.on_press=self.login
        self.add_widget(button1)
    def login(self):
        self.manager.current="Логин"
        self.manager.transition.direction="up"
    def log(self):
        loginText=emailInput(text="Войти")
        passwordText=password(text="Войти")
        with open("bd.json") as bd:
            for i in bd:
                if loginText==bd[i][login]:
                    if passwordText==bd[i][password]:
                        pass

class app(App):
    def build(self):
        sm=ScreenManager()
        sm.add_widget(mainScreen(name="Главный экран"))
        sm.add_widget(loginScreen(name="Логин"))
        return sm

app().run()
