from tkinter import *
from tkinter.ttk import *
from tkinter_helper import WinGUI

class Win():
    def __init__(self,win_gui_instance):
        self.win_gui = win_gui_instance
        self.__event_bind()

    #no3 给每个写一个calc和update
    def calc_level(self):
        self.level = self.win_gui.get_level()
        if self.level == "Intermediated level":
            self.level = 0   
        elif self.level == "Ground floor":
            self.level = 1
        else:
            self.level =0.7
        return self.level

    def update_level(self,level):   
        new_level = self.calc_level()
        self.win_gui.set_level(new_level)
        return print(self.win_gui.level)
        
    
    def __event_bind(self):
        self.win_gui.button_calcNow.bind('<Button-1>',self.update_level)

root = WinGUI() 
win = Win(root)
root.mainloop()

'''
每个需要参与计算的 界面上的东西 都需要加上no1, no2, no3
计算方法：
level和insulation 官网上有
设number of wall=n
area = n x(长加宽的1/2) x 高

'''