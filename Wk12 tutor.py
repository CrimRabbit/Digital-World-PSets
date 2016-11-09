from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen

class testApp(App):
        
    def build(self):
        #Q1 : 
        #self.label1 = Label(text="label", on_touch_down=self.alternate)
        #return self.label1
        
        #Q2 : 
        #self.label1 = Label(text="SLied moi.", on_touch_move=self.detect)
        #self.dx = 0
        #self.dy = 0
        #return self.label1
        
        #Q3 :
        #return root()
        
        #Q4 :
        sm=ScreenManager()
        ms=MainScreen(name='main')
        st=SettingsScreen(name='settings')
        sm.add_widget(ms)
        sm.add_widget(st)
        sm.current='main'
        return sm
        
    #Q2 :
    #def detect(self,instance,touch):
    #    #self.label1.text = str(touch.dx) + str(touch.dy)
    #    if touch.dx > 300.0 * touch.dy:
    #        if touch.dx >  self.dx:
    #            self.label1.text = "Slidded right"
    #        else:
    #            self.label1.text = "Slodded left"
    #    else:
    #        if touch.dy > self.dy:
    #            self.label1.text = "Sladed up"
    #        else:
    #            self.label1.text = "Sleded down"
    
    #Q1 :    
    #def alternate(self,instance,touch):
    #    if(self.label1.text == "meeep"):
    #        self.label1.text = "merrp"
    #    else:
    #        self.label1.text = "meeep"
        
    
class MainScreen(Screen):
    def __init__(self,**kwargs):
        Screen.__init__(self, **kwargs)
        #gl = GridLayout()
        #gl.cols = 2
        self.add_widget(Button(text="Settings",on_press = self.clickSettings,pos_hint={"x":0.0,"y":0},size_hint=(0.5,1)))
        self.add_widget(Button(text="Quit",on_press = self.clickQuit,pos_hint={"x":0.5,"y":0},size_hint=(0.5,1)))
        #self.layout=gl
        
    def clickSettings(self, value):
        self.manager.transition.direction = 'left'
    	self.manager.current= "settings"

    def clickQuit(self, value):
        App.get_running_app().stop()
    
class SettingsScreen(Screen):
    def __init__(self, **kwargs):
        Screen.__init__(self, **kwargs)
        #gl = GridLayout()
        #gl.cols = 2
        self.add_widget(Button(text="Main",on_press = self.clickMain,pos_hint={"x":0.0,"y":0},size_hint=(0.5,1)))
        self.settingsButton = Button(text="Quit (maybe.)",on_press = self.clickKappa,pos_hint={"x":0.5,"y":0},size_hint=(0.5,1))
        self.add_widget(self.settingsButton)
        #self.layout=gl

    def clickMain(self,value):
        self.manager.transition.direction = 'right'
        self.manager.current= "main"
    
    def clickKappa(self,value):
        self.manager.transition.direction = 'right'
        if self.settingsButton.text == "Quit (maybe.)":
            self.settingsButton.text = "Yes?"
        elif self.settingsButton.text == "Yes?":
            self.settingsButton.text = "No?"
        elif self.settingsButton.text == "No?":
            self.settingsButton.text = "Maybe So."
        else:
            self.settingsButton.text = "Yes?"
    
#Q3 :     
#class root(GridLayout):       
#    def __init__(self, **kwargs):
#        super(root,self).__init__(**kwargs)
#        self.cols = 2
#    
#        se.investmentAmount)
#        lf.add_widget(Label(text="Investment Amount",pos_hint={"x":0.5,"y":0}))
#        self.investmentAmount = TextInput(multiline=False) 
#        self.add_widget(self
#        self.add_widget(Label(text="Years",pos_hint={"x":0.5,"y":0}))
#        self.years = TextInput(multiline=False)
#        self.add_widget(self.years)
#        
#        self.add_widget(Label(text="Annual Interest Rate",pos_hint={"x":0.5,"y":0}))
#        self.annualInterestRate = TextInput(multiline=False)
#        self.add_widget(self.annualInterestRate)
#        
#        self.add_widget(Label(text="Future Value",pos_hint={"x":0.5,"y":0}))
#        self.result = Label(text=" ",pos_hint={"x":0.5,"y":0})
#        self.add_widget(self.result)
#        
#        self.add_widget(Button(text="Buton to culcolator",on_press = self.click ,pos_hint={"x":0.5,"y":0}))
#     
#        #Q3 :
#    def click(self,instance):
#        investmentAmount = float(self.investmentAmount.text)
#        annualInterestRate = float(self.annualInterestRate.text)
#        years = float(self.years.text)
#        self.result.text = str(round(investmentAmount * (1 + (annualInterestRate/12.0/100))**(years*12),2))
    
testApp().run()

#self.label1.text = "meeep: %f %f"%(touch.dx, touch.dy)