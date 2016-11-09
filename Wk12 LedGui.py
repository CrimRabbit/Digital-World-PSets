from kivy.app import App
from kivy.config import Config
from kivy.uix.label import Label
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.gridlayout import GridLayout
import firebase as fire

fburl = "https://kivyled.firebaseio.com/"
token = "STPBn7iDLmuAITbCgSvAjVKV7HfzxBX1FyTSnzQj"

class ledApp(App):
        
    def build(self):
        Config.set('graphics', 'width', '400')
        Config.set('graphics', 'height', '200')
        return root()
        

class root(GridLayout):       
    def __init__(self, **kwargs):
        super(root,self).__init__(**kwargs)
        self.cols = 2
    
        firebase = fire.FirebaseApplication(fburl, token)
        redLedState = firebase.get('/redLed')
        if(redLedState == True):
            redLedState = "On"
        else:
            redLedState = "Off"
        yellowLedState = firebase.get('/yellowLed')
        if(yellowLedState == True):
            yellowLedState = "On"
        else:
            yellowLedState = "Off"
    
        self.add_widget(Label(text="Yellow LED",size_hint=(0.5,1)))
        self.yellowLedButton = ToggleButton(text=yellowLedState,on_press = self.clickYellow ,size_hint=(0.5,0.5))
        self.add_widget(self.yellowLedButton)
        
        self.add_widget(Label(text="Red LED",size_hint=(0.5,1)))
        self.redLedButton = ToggleButton(text=redLedState,on_press = self.clickRed ,size_hint=(0.5,0.5))
        self.add_widget(self.redLedButton)
        
    def clickYellow(self,instance):
        if(self.yellowLedButton.state == "normal"):
            firebase = fire.FirebaseApplication(fburl, token)
            firebase.put('/','yellowLed',False)
            self.yellowLedButton.text = "Off"
        else: 
            firebase = fire.FirebaseApplication(fburl, token)
            firebase.put('/','yellowLed',True)
            self.yellowLedButton.text = "On"
        
    def clickRed(self,*args):
        if args[0].state == "normal":
            firebase = fire.FirebaseApplication(fburl, token)
            firebase.put('/','redLed',False)
            self.redLedButton.text = "Off"
        else:
            firebase = fire.FirebaseApplication(fburl, token)
            firebase.put('/','redLed',True)
            self.redLedButton.text = "On"
        
ledApp().run()