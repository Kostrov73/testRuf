from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import ScreenManager, Screen
##hi
from  instructions import *
from scrollLabel import * 
from seconds import *
from sits import * 
from runner import *
from ruffier import *
##Hello

age=0
name=''
pulse1=0
pulse2=0
pulse3=0


class FirstScr(Screen):
    def __init__(self,name='first'):
        super().__init__(name=name)
        lay1=BoxLayout(orientation='vertical')
        layh1=BoxLayout(size_hint=(1,.1))
        layh2=BoxLayout(size_hint=(1,.1))
        label_n=Label(text="Ваше имя: ")
        label_age=Label(text="Введите Ваш возраст: ")
        scl = ScrollLabel(ltext=txt_instruction,pos_hint={'center_y':.5})
        self.name_val=TextInput(text='', multiline=False, size_hint=(.75,.9), pos_hint={"top":1,'center_x':.5})
        self.age_val=TextInput(text='7', multiline=False, size_hint=(.75,.9), pos_hint={"top":1,'center_x':.5})
        self.btn=Button(text="Продолжить",size_hint=(.33,.23), pos_hint={'top':0.5, 'center_x':.5})
        self.btn.on_press=self.next
        layh1.add_widget(label_n)
        layh2.add_widget(label_age)
        layh1.add_widget(self.name_val)
        layh2.add_widget(self.age_val)
        lay1.add_widget(scl)
        lay1.add_widget(layh1)
        lay1.add_widget(layh2)
        lay1.add_widget(self.btn)
        self.add_widget(lay1)

    def next(self):
        global age, name
        age=int(self.age_val.text)
        name=self.name_val.text
        self.manager.current='second'


        
class SecondScr(Screen):
    def __init__(self, name='second'):
        super().__init__(name=name)
        self.next_screen=False
        lay1=BoxLayout(orientation='vertical')
        lay2=BoxLayout(size_hint=(1,.1))
        scrl=ScrollLabel(txt_test1)
        label=Label(text='Введите результат:')
        self.sec=Seconds(15,pos_hint={'center_x':.5})
        self.sec.bind(done=self.sec_finished)
        self.ti=TextInput(text='0', multiline=False, size_hint=(.75,1.3), pos_hint={"top":1.3,'center_x':.5})
        self.ti.set_disabled(True)
        self.btn=Button(text="Продолжить",size_hint=(.33,.23), pos_hint={'top':0.5, 'center_x':.5})
        self.btn.on_press=self.next
        lay2.add_widget(label)
        lay2.add_widget(self.ti)
        lay1.add_widget(scrl)
        lay1.add_widget(self.sec)
        lay1.add_widget(lay2)
        lay1.add_widget(self.btn)
        self.add_widget(lay1)

    def next(self):
        if self.next_screen==False:
            self.sec.start()
            self.btn.set_disabled(True)
        else:
            global pulse1
            pulse1=int(self.ti.text)
            self.manager.current='third'

    def sec_finished(self,*args):
        self.btn.set_disabled(False)
        self.btn.text='Продолжить'
        self.ti.set_disabled(False)
        self.next_screen=True


class ThirdScr(Screen):
    def __init__(self, name='third'):
        super().__init__(name=name)
        self.next_screen=False
        instr=ScrollLabel(txt_sits,size_hint=(1,.1))
        self.sits_value=Sits(30,size_hint=(1,.1))
        self.run=Runner(total=30, steptime=1.5)
        self.run.bind(finished=self.run_finished)
        self.btn=Button(text='Начать', size_hint=(1,.1))
        self.btn.on_press=self.next
        lay1=BoxLayout(orientation='vertical')
        lay1.add_widget(instr)
        lay1.add_widget(self.sits_value)
        lay1.add_widget(self.run)
        lay1.add_widget(self.btn)
        self.add_widget(lay1)

    def next(self):
        if self.next_screen==False:
            self.run.start()
            self.btn.set_disabled(True)
            self.run.bind(value=self.sits_value.next)
        else:
            self.manager.current='fourth'

    def run_finished(self,*args):
        self.next_screen=True
        self.btn.set_disabled(False)
        self.btn.text='Продолжить'





        
class FourthScr(Screen):
    def __init__(self, name='fourth'):
        super().__init__(name=name)
        # флаг перехода к следующей страницы в False
        self.next_screen = False
        # режим работы секундомера
        self.stage = 0
        # создаём виджеты
        instr1 = ScrollLabel(txt_test3)
        self.instr2 = ScrollLabel('Считайте пульс')
        # создаём секундомер (первый раз считает 15 секунд)
        self.sec = Seconds(15)
        # по завершению работы вызовем метод sec_finished
        self.sec.bind(done = self.sec_finished)
        res1_label = Label(text='Результат:')
        self.res1_value = TextInput(text='0')
        self.res1_value.set_disabled(True)
        res2_label = Label(text='Результат после отдыха:')
        self.res2_value = TextInput(text='0')
        self.res2_value.set_disabled(True)
        self.but = Button(text='Начать',size_hint=(1,0.2))
        self.but.on_press = self.next
        # размещаем виджеты по направляющим
        hor1 = BoxLayout(size_hint=(1,0.2))
        hor1.add_widget(res1_label)
        hor1.add_widget(self.res1_value)
        hor2 = BoxLayout(size_hint=(1,0.2))
        hor2.add_widget(res2_label)
        hor2.add_widget(self.res2_value)
        ver = BoxLayout(orientation = 'vertical')
        ver.add_widget(instr1)
        ver.add_widget(self.instr2)
        ver.add_widget(self.sec)
        ver.add_widget(hor1)
        ver.add_widget(hor2)
        ver.add_widget(self.but)
        self.add_widget(ver)

    # метод срабатывает по завершению работы секундомера
    def sec_finished(self, instance, value):
        if value:
            # меняем режим работы секундомера (+1)
            self.stage += 1
        # если отсчитали первые 15 секунд
            if self.stage == 1:
                # напишем Отдыхайте
                self.instr2.set_text('Отдыхайте')
                # перезапустим секундомер на 30 секунд
                self.sec.restart(30)
                # разблокировка res1_value
                self.res1_value.set_disabled(False)
            # если отсчитали второй раз (30 секунд )
            elif self.stage == 2:
                # напишем считайте пульс
                self.instr2.set_text('Считайте пульт')
                # перезапускаем таймер на 15 секунд
                self.sec.restart(15)
            # если отсчитали третий раз (15 секунд)
            elif self.stage == 3:
                # разблокировка res2_value
                self.res2_value.set_disabled(False)
                # меняем текст кнопкп
                self.but.text = 'Завершить'
                # разблокировка but
                self.but.set_disabled(False)
                # можно переходить на следующий экран
                self.next_screen = True
                # метод отрабатываем при клике по кнопке
    def next(self):
        # если переходить на следующий экран нельзя
        if self.next_screen == False:
            # блокируем кнопку
            self.but.set_disabled(True)
            # запускаем секундомер (первый раз 15 сек)
            self.sec.start()
        else:
            # запоминаем пульс в глобальных переменных
            global pulse2, pulse3
            pulse2 = int(self.res1_value.text)
            pulse3 = int(self.res2_value.text)
            # идем на четвертый экран
            self.manager.current = 'fiveth'

# функция для формирования строки с результатом
def get_result():
    # вызываем функцию test из ruffier.py
    res = test(pulse1, pulse2, pulse3, age)
    # возвращаем строку с именем и результатом
    return name + '\n' + res[0] + '\n' + res[1] 

class FivethScr(Screen):
    def __init__(self, name='fiveth'):
        super().__init__(name=name)
        ver = BoxLayout(orientation='vertical', padding=8, spacing=8)
        # добавили один виджет, в нём будет результат измерений
        self.instr = ScrollLabel('')
        self.btn=Button(text="Заново",size_hint=(.33,.23), pos_hint={'top':0.5, 'center_x':.5})
        self.btn.on_press = self.next
        ver.add_widget(self.instr)
        ver.add_widget(self.btn)
        self.add_widget(ver)
        # при показе экрана вызвать метод before
        self.on_enter = self.before


    def before(self):
        # установить в виджет результат get_result
        self.instr.set_text(get_result())

    def next(self):
        self.manager.current = 'first'



class SixthScr(Screen):
    def __init__(self, name='sixth'):
        super().__init__(name=name)
        




class MainScr(Screen):
    def __init__(self,name='main'):
        super().__init__(name=name)
        
        

class MyApp(App):
    def build(self):
        sm=ScreenManager()
        #sm.add_widget(MainScr(name='main'))
        sm.add_widget(FirstScr(name='first'))
        sm.add_widget(SecondScr(name='second'))
        sm.add_widget(ThirdScr(name='third'))
        sm.add_widget(FourthScr(name='fourth'))
        sm.add_widget(FivethScr(name='fiveth'))
        sm.add_widget(SixthScr(name='sixth'))
        return sm


MyApp().run()
