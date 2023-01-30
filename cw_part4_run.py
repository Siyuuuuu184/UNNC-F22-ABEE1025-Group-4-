#Author: Siyu WANG & Chengyang WANG
#First editing date: 2023.01.16
#Latest editing date: 2023.01.30

from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
import tkinter.filedialog
import tkinter.dialog
from cw_part4_tkinter_helper import WinGUI

class Win():
    def __init__(self,win_gui_instance):
        self.win_gui = win_gui_instance
        self.__event_bind()
        self.file_path = ''
        self.file_text = ''

    ##no3 calc & update for level
    def calc_level(self):
        self.level = self.win_gui.get_level()
        if self.level == "Intermediated level":
            self.level = 0   
        elif self.level == "Ground floor":
            self.level = 1
        elif self.level == "Top floor":
            self.level = 0.7
        else:
            showerror("Error","Parameters cannot be null.")
        return self.level

    def update_level(self):   
        new_level = self.calc_level()
        self.win_gui.set_level(new_level)
        return self.win_gui.level

    #calc & update for insulation
    def calc_insulation(self):
        self.insulation = self.win_gui.get_insulation()
        if self.insulation == "No extra insulation":
            self.insulation = 2.2
        elif self.insulation == "Mediocre insulation":
            self.insulation = 1
        elif self.insulation == "Very well insulated":
            self.insulation = 0.6
        else:
            showerror("Error","Parameters cannot be null.")
        return self.insulation

    def update_insulation(self):
        new_insulation = self.calc_insulation()
        self.win_gui.set_insulation(new_insulation)
        return self.win_gui.insulation

    #calc & update for wall
    def calc_wall(self):
        self.wall = self.win_gui.get_wall()
        if self.wall == "1":
            self.wall = 1
        elif self.wall == "2":
            self.wall = 2
        elif self.wall == "3":
            self.wall = 3
        elif self.wall == "4":
            self.wall = 4
        else:
            showerror("Error","Parameters cannot be null.")
        return self.wall

    def update_wall(self):
        new_wall = self.calc_wall()
        self.win_gui.set_wall(new_wall)
        return self.win_gui.wall

    #calc & update for length
    def calc_length(self):
        try:
            self.length = float(self.win_gui.get_length())
        except:
            return showerror("ValueError","Length should be a postive number.") 
        return self.length

    def update_length(self):
        new_length = self.calc_length()
        self.win_gui.set_length(new_length)
        return self.win_gui.length

    #calc & update for width
    def calc_width(self):
        try:
            self.width = float(self.win_gui.get_width())
        except:
            return showerror("ValueError","Width should be a postive number.") 
        return self.width

    def update_width(self):
        new_width = self.calc_width()
        self.win_gui.set_width(new_width)
        return self.win_gui.width

    #calc & update for height
    def calc_height(self):
        try:
            self.height = float(self.win_gui.get_height())
        except:
            return showerror("ValueError","Height should be a postive number.") 
        return self.height

    def update_height(self):
        new_height = self.calc_height()
        self.win_gui.set_height(new_height)
        return self.win_gui.height

    #calc & update for the final result
    def update_result(self,*arg):
        self.h = self.update_height()
        self.w = self.update_width()
        self.l = self.update_length()
        self.lvl = self.update_level()
        self.wll = self.update_wall()
        self.insu = self.update_insulation()

        self.res = self.h*((self.w+self.l)/2)*self.wll*self.insu + self.w*self.l*self.lvl
        return self.res

    #calc & update for delta_t
    def calc_delta_t(self):
        try:
            self.temp_in = float(self.win_gui.get_temp_in())
            self.temp_out= float(self.win_gui.get_temp_out())
        except:
            return showerror("ValueError","Temperature should be a number.")
        self.delta_t = self.temp_in - self.temp_out
        return self.delta_t

    def update_delta_t(self):
        new_delta_t = self.calc_delta_t()
        self.win_gui.set_delta_t(new_delta_t)
        return self.win_gui.delta_t

    def update_power(self):
        self.t = self.update_delta_t()
        self.r = self.update_result()

        self.power = self.t * self.r
        return self.power

    def calc_difference(self):
        try:
            self.ideal = float(self.win_gui.ipt_idl.get())
        except:
            return showerror("ValueError","Your ideal heat loss should be a number.")
        return self.ideal

    def update_difference(self):
        self.current = self.update_result()
        self.ideal = self.calc_difference()
        self.difference = self.current - self.ideal
        return self.difference

    def display_result(self,*arg):
        res = self.update_result()
        self.win_gui.frame_result.ipt_res.delete(0, END)
        self.win_gui.frame_result.ipt_res.insert('0',res)
        self.win_gui.input_current.delete(0, END)
        self.win_gui.input_current.insert('0',res)
        self.win_gui.frame_result.ipt_pow.delete(0,END)
        power = self.update_power()
        self.win_gui.frame_result.ipt_pow.insert('0',power)
        difference = self.update_difference()
        self.win_gui.input_difference.delete(0,END)
        if difference > 0:
            self.win_gui.ipt_dif.configure(foreground='red')
        else:
            self.win_gui.ipt_dif.configure(foreground='green')
        self.win_gui.input_difference.insert('0',difference)

    def save_file(self,*arg):
        self.file_path = tkinter.filedialog.asksaveasfilename(title=u'Save as file')
        print('Save as file：', self.file_path)
        self.file_text = "Current heat loss:"+ str(self.update_result())+ \
        "\n\nUnder the following situation:"+"\nRoom's level:"+str(self.win_gui.get_level())+\
        "\nExternal wall's insulation:"+str(self.win_gui.get_insulation())+\
        "\nNumber of external wall:"+str(self.update_wall())+\
        "\nRoom's dimensions:"+"\n"+str(self.update_length())+"m\x20long\n"+\
        str(self.update_width())+"m\x20wide\n"+str(self.update_height())+"m\x20high\n"+\
        "\nIndoor and Outdoor Temperature Difference:"+str(self.update_delta_t())+\
        "\n"+str(self.update_difference())+\
        "W\x20power is required to reach to the targeted indoor temperature."
        if self.file_path is not None:
            with open(file=self.file_path, mode='a+', encoding='utf-8') as file:
                file.write(self.file_text)
            #text1.delete('1.0', tk.END)
            tkinter.dialog.Dialog(None, {'title': 'File Modified', 'text': 'Successfully saved!', 'bitmap': 'warning', 
                'default': 0, 'strings': ('OK', 'Cancle')})
            print('Successfully saved!')

         
    def __event_bind(self):
        self.win_gui.button_calcNow.bind('<Button-1>',self.display_result) #final display
        self.win_gui.button_save.bind('<Button-1>',self.save_file)

root = WinGUI() 
win = Win(root)
root.mainloop()

