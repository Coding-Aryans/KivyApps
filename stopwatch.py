from kivy import platform
from kivy.lang import Builder
from kivy.properties import StringProperty, BooleanProperty, NumericProperty
from kivy.uix.anchorlayout import AnchorLayout
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen,SlideTransition
from kivy.clock import Clock

import time

# Builder.load_file("small.kv")
Builder.load_string(
    """
    
<MenuScreen>:
    name: 'menu'
    BoxLayout:
        orientation:"vertical"

        #Image:
            #source: "stopwatch.png"
            #allow_stretch: False
            #keep_ratio: True

<ProfileScreen>:
    name: 'profile'
    BoxLayout:

        orientation:"vertical"
        size_hint:1,.5
        pos_hint:{"center_y":.5}



        Label:
            id:my_lab
            text:f'00:00:00'
            font_size: "33dp"
            #font_name: "fonts/Lcd.ttf"
            color: 1, .5, 1, 1

    AnchorLayout:
        anchor_x:"left"
        anchor_y:"bottom"
        BoxLayout:
            size_hint:1,.5
            spacing:"30dp"
            padding:"10dp"
            Button:

                size_hint:.2,.2

                text:"start"
                on_press:root.on_button_click()
                

                disabled:  root.sw_start
                background_normal: ""
                background_color : (40/255, 84/255 , 150/255, 1)
            Button:
                size_hint:.2,.2

                text:"Stop"
                on_press:root.on_button_stop()
                disabled:  root.sw_stop
                background_normal: ""
                background_color : (255, 0 , 0, 1)


            Button:
                size_hint:.2,.2

                text:"Reset"


                on_press:root.reset()
                background_normal: ""
                background_color : (0, 128 , 128, 1)

    
    """

)

class MenuScreen(Screen):

   pass


class ProfileScreen(Screen):
   my_text = NumericProperty()
   seconds = 0
   sw_start=BooleanProperty(False)
   sw_stop = BooleanProperty(False)



   def update(self,nap):
        if  self.sw_start:
            self.seconds+=nap

            min,sec=divmod(self.seconds,60)

            part_sec=sec*100%100

            self.ids.my_lab.text=f'{int(min):02}:{int(sec):02}:{int(part_sec):02}'



   def start(self,interval):
       if self.my_text<=60:
           self.my_text+=1

   def on_button_click(self):
       self.sw_start = True
       self.sw_stop=False
       Clock.schedule_interval(self.update, 0)

       # Clock.unschedule(self.start)
       # Clock.schedule_interval(self.start,0)
   def on_button_stop(self):
       self.sw_start=False
       self.sw_stop=True

   def reset(self):
       self.sw_start = False
       self.sw_stop = True

       self.seconds=0
       self.ids.my_lab.text=f'00:00:00'










       #     print(self.count)
       #     time.sleep(.2)
       #     self.count -= 1






           # self.my_text = str(self.seconds)


# Create the screen manager
sm = ScreenManager(transition=SlideTransition())

sm.add_widget(MenuScreen())
sm.add_widget(ProfileScreen())



class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"  # "Light"

        Clock.schedule_once(self.screen_switch_one, 5)  # run timer.work1 after 5 seconds
        Clock.schedule_once(self.screen_switch_two, 5)




        return sm

    def screen_switch_one(a, b):
        sm.current = 'menu'

    def screen_switch_two(a, b):
        sm.current = 'profile'


MainApp().run()