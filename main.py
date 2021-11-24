from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.boxlayout import BoxLayout
from allInfo import txt_instruction, txt_test1, txt_test2, txt_test3, txt_sits


class screen1(Screen):
    def __init__(self, name):
        super().__init__(name=name)
        txt_instructionLabel=Label(text=txt_instruction)
        nameLayout=BoxLayout(orientation="horizontal")
        nameLabel=Label(text="Введите ваше имя: ")
        nameInput=TextInput()
        nameLayout.add_widget(nameLabel)
        nameLayout.add_widget(nameInput)
        ageLayout=BoxLayout(orientation="horizontal")
        ageLabel=Label(text="Введите ваш возраст: ")
        ageInput=TextInput()
        ageLayout.add_widget(ageLabel)
        ageLayout.add_widget(ageInput)
        nextButton=Button(text="Продолжить")
        mainLayout=BoxLayout(orientation="vertical")
        mainLayout.add_widget(txt_instructionLabel)
        mainLayout.add_widget(nameLayout)
        mainLayout.add_widget(ageLayout)
        mainLayout.add_widget(nextButton)
        self.add_widget(mainLayout)
class screen2(Screen):
    pass
class screen3(Screen):
    pass
class screen4(Screen):
    pass
class screen5(Screen):
    pass
class screen6(Screen):
    pass
class HeartTester(App):
    def build(self):
        screenManager=ScreenManager()
        screenManager.add_widget(screen1(name="Логин"))
        screenManager.add_widget(screen2(name="Инфа"))
        screenManager.add_widget(screen3(name="Замер1"))
        screenManager.add_widget(screen4(name="Замер2"))
        screenManager.add_widget(screen5(name="Результат"))
        return screenManager
HeartTester().run()