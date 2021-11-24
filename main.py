from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.boxlayout import BoxLayout
from allInfo import txt_instruction, txt_test1, txt_test2, txt_test3, txt_sits

p1,p2,p3=0,0,0
age=7
name=""

class screen1(Screen):
    def __init__(self, name):
        super().__init__(name=name)
        txt_instructionLabel=Label(text=txt_instruction)
        nameLayout=BoxLayout(orientation="horizontal")
        nameLabel=Label(text="Введите ваше имя: ")
        self.nameInput=TextInput()
        nameLayout.add_widget(nameLabel)
        nameLayout.add_widget(self.nameInput)
        ageLayout=BoxLayout(orientation="horizontal")
        ageLabel=Label(text="Введите ваш возраст: ")
        self.ageInput=TextInput()
        ageLayout.add_widget(ageLabel)
        ageLayout.add_widget(self.ageInput)
        nextButton=Button(text="Продолжить")
        nextButton.on_press=self.nextScreen
        mainLayout=BoxLayout(orientation="vertical")
        mainLayout.add_widget(txt_instructionLabel)
        mainLayout.add_widget(nameLayout)
        mainLayout.add_widget(ageLayout)
        mainLayout.add_widget(nextButton)
        self.add_widget(mainLayout)
    def nextScreen(self):
        global name, age
        name=self.nameInput.text
        age=self.ageInput.text
        self.manager.current="Инфа"
class screen2(Screen):
    def __init__(self, name):
        super().__init__(name=name)
        inputLayout=BoxLayout(orientation="horizontal", size_hint=(0.7, 0.1), pos_hint={"center_x":0.5})
        mainLayout=BoxLayout(orientation="vertical")
        labelInfo=Label(text=txt_test2)
        labelResult=Label(text="Введите ваш результат")
        self.resultInput=TextInput()
        self.next=Button(text="Продолжить", size_hint=(0.3, None), pos_hint={"center_x":0.5})
        self.next.on_press=self.nextScreen
        inputLayout.add_widget(labelResult)
        inputLayout.add_widget(self.resultInput)
        mainLayout.add_widget(labelInfo)
        mainLayout.add_widget(inputLayout)
        mainLayout.add_widget(self.next)
        self.add_widget(mainLayout)
    def nextScreen(self):
        global p1
        p1=self.resultInput.text
        self.manager.current="Замер1"


class screen3(Screen):
    def __init__(self, name):
        super().__init__(name=name)
        mainLayout=BoxLayout(orientation="vertical", size_hint=(0.5, 0.5), pos_hint={"center_y":0.5, "center_x":0.5}, spacing=150)
        text=Label(text=txt_test3, size_hint=(0.3, None), pos_hint={"center_x":0.5})
        button=Button(text="Продолжить", size_hint=(0.7, None), pos_hint={"center_x":0.5})
        button.on_press=self.nextScreen
        mainLayout.add_widget(text)
        mainLayout.add_widget(button)
        self.add_widget(mainLayout)
    def nextScreen(self):
        self.manager.current="Замер2"
class screen4(Screen):
    def __init__(self, name):
        super().__init__(name=name)
        txt_instructionLabel=Label(text=txt_test3)
        nameLayout=BoxLayout(orientation="horizontal")
        nameLabel=Label(text="Результат: ")
        self.nameInput=TextInput()
        nameLayout.add_widget(nameLabel)
        nameLayout.add_widget(self.nameInput)
        ageLayout=BoxLayout(orientation="horizontal")
        ageLabel=Label(text="Результат после отдыха: ")
        self.ageInput=TextInput()
        ageLayout.add_widget(ageLabel)
        ageLayout.add_widget(self.ageInput)
        nextButton=Button(text="Завершить")
        nextButton.on_press=self.nextScreen
        mainLayout=BoxLayout(orientation="vertical")
        mainLayout.add_widget(txt_instructionLabel)
        mainLayout.add_widget(nameLayout)
        mainLayout.add_widget(ageLayout)
        mainLayout.add_widget(nextButton)
        self.add_widget(mainLayout)
    def nextScreen(self):
        global p2, p3
        p2=self.nameInput.text
        p3=self.ageInput.text
        self.manager.current="Результат"

class screen5(Screen):
    def __init__(self, name):
        super().__init__(name=name)
        txt_instructionLabel=Label(text="Ага")
        mainLayout=BoxLayout()
        mainLayout.add_widget(txt_instructionLabel)
        self.add_widget(mainLayout)


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