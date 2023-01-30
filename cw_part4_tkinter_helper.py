from tkinter import *
from tkinter.ttk import *

#scroll bar
def scrollbar_autohide(bar,widget):
    def show():
        bar.lift(widget)
    def hide():
        bar.lower(widget)
    hide()
    widget.bind("<Enter>", lambda e: show())
    bar.bind("<Enter>", lambda e: show())
    widget.bind("<Leave>", lambda e: hide())
    bar.bind("<Leave>", lambda e: hide())


    
class WinGUI(Tk):
    def __init__(self):
        super().__init__()
        self.__win()
        #signs on the top
        self.label_ideal = self.__label_ideal()
        self.label_current = self.__label_current()
        self.input_ideal = self.input_ideal()
        self.input_current = self.input_current()
        self.label_unit1 = self.__label_unit1()
        self.label_unit = self.__label_unit()
        self.input_difference = self.input_difference()
        self.label_unit2 = self.__label_unit2()

        #frames
        self.label_frame_feature = Frame_feature(self)
        self.label_frame_dimension = Frame_dimension(self)        
        self.label_frame_temp = Frame_temp(self)
        self.frame_result = Frame_result(self)
        self.button_save = self.__button_save()
        self.button_calcNow = self.__button_calcNow()

        #values needed later
        self.level = ""
    def get_level(self):
        self.level = self.label_frame_feature.showMsg_lvl()
        return self.level
    def set_level(self,level):
        self.level = level
    #no1. set & get to transmit value to cw_part4_run.py

        self.insulation = ""
    def get_insulation(self):
        self.insulation = self.label_frame_feature.showMsg_ins()
        return self.insulation
    def set_insulation(self,insulation):
        self.insulation = insulation

        self.wall = ""
    def get_wall(self):
        self.wall = self.label_frame_feature.showMsg_wall()
        return self.wall
    def set_wall(self,wall):
        self.wall = wall

        self.length = ""
    def get_length(self):
        self.length = self.label_frame_dimension.showMsg_len()
        return self.length
    def set_length(self,length):
        self.length = length

        self.width = ""
    def get_width(self):
        self.width = self.label_frame_dimension.showMsg_wid()
        return self.width
    def set_width(self,width):
        self.width = width

        self.height = ""
    def get_height(self):
        self.height = self.label_frame_dimension.showMsg_hgt()
        return self.height
    def set_height(self,height):
        self.height = height

    
    def get_temp_out(self):
        self.temp_out = self.label_frame_temp.showMsg_amb()
        return self.temp_out
    def get_temp_in(self):
        self.temp_in = self.label_frame_temp.showMsg_tin()
        return self.temp_in

        self.delta_t = ""
    def set_delta_t(self,delta_t):
        self.delta_t = delta_t


    def __win(self):
        self.title("Heat Loss Calculator")
        width = 550
        height = 540
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)
        self.resizable(width=True, height=True)

    def __label_ideal(self):
        label = Label(self,text="Your ideal heat loss:",anchor="center")
        label.place(x=40, y=20, width=145, height=18)
        return label

    def __label_current(self):  
        label = Label(self,text="The current simulated heat loss:",anchor="center")
        label.place(x=40, y=51, width=212, height=19)
        return label

    def showMsg_idl(self):
        return self.ipt_idl.get()

    def input_ideal(self):
        self.ipt_idl = Entry(self)
        self.ipt_idl.place(x=187, y=20, width=59, height=20)
        return self.ipt_idl

    def input_current(self):
        self.ipt_res2 = Entry(self)
        self.ipt_res2.place(x=257, y=50, width=59, height=20)
        return self.ipt_res2

    def __label_unit1(self):
        label = Label(self,text="W/K.",anchor="center")
        label.place(x=240, y=20, width=28, height=20)
        return label

    def __label_unit(self):
        label = Label(self,text="W/K.",anchor="center")
        label.place(x=310, y=50, width=35, height=21)
        return label

    def input_difference(self):
        self.ipt_dif = Entry(self)
        self.ipt_dif.place(x=420, y=50, width=78, height=21)
        return self.ipt_dif

    def __label_unit2(self):
        label = Label(self,text="W/K.",anchor="center")
        label.place(x=500, y=50, width=34, height=21)
        return label

    def __button_save(self):
        btn = Button(self, text="Save")
        btn.place(x=510, y=140, width=44, height=181)
        return btn

    def __button_calcNow(self):
        btn = Button(self, text="Caculate Now")
        btn.place(x=47, y=482, width=207, height=33)
        return btn

class Frame_feature(LabelFrame):
    def __init__(self,parent):
        super().__init__(parent)
        self.__frame()
        self.select_box_level = self.select_box_level()
        self.select_box_insu = self.select_box_insu()
        self.select_box_wall = self.select_box_wall()
        self.label_level = self.__label_level()
        self.label_insu = self.__label_insu()
        self.label_wall = self.__label_wall()
    def __frame(self):
        self.configure(text="Room's feature")
        self.place(x=40, y=100, width=180, height=255)

    #no2 delete the "__" to make it possible to be used outside the class
    def showMsg_lvl(self, *arg):
        return self.var_lvl.get()

    def select_box_level(self):
        self.var_lvl = StringVar()
        self.cb_lvl = Combobox(self, state="readonly",textvariable=self.var_lvl)
        self.cb_lvl['values'] = ("Ground floor","Intermediated level","Top floor")
        self.cb_lvl.place(x=10, y=40, width=150, height=24)
        self.cb_lvl.bind('<<ComboboxSelected>>',self.showMsg_lvl)
        return self.cb_lvl

    def showMsg_ins(self, *arg):
        return self.var_ins.get()

    def select_box_insu(self):
        self.var_ins = StringVar()
        self.cb_ins = Combobox(self, state="readonly",textvariable=self.var_ins)
        self.cb_ins['values'] = ("No extra insulation","Mediocre insulation","Very well insulated")
        self.cb_ins.place(x=10, y=110, width=150, height=24)
        self.cb_ins.bind('<<ComboboxSelected>>',self.showMsg_ins)
        return self.cb_ins

    def showMsg_wall(self, *arg):
        return self.var_wall.get()

    def select_box_wall(self):
        self.var_wall = StringVar()
        cb_wall  = Combobox(self, state="readonly",textvariable=self.var_wall)
        cb_wall['values'] = ("1","2","3","4")
        cb_wall.place(x=10, y=180, width=150, height=24)
        return cb_wall

    def __label_level(self):
        label = Label(self,text="Level:",anchor="center")
        label.place(x=10, y=20, width=40, height=18)
        return label

    def __label_insu(self):
        label = Label(self,text="Insulation:",anchor="center")
        label.place(x=10, y=90, width=70, height=18)
        return label

    def __label_wall(self):
        label = Label(self,text="Number of external wall:",anchor="center",font=("",9))
        label.place(x=10, y=160, width=153, height=18)
        return label

class Frame_dimension(LabelFrame):
    def __init__(self,parent):
        super().__init__(parent)
        self.__frame()
        self.label_length = self.__label_length()
        self.label_width = self.__label_width()
        self.label_height = self.__label_height()
        self.input_length = self.input_length()
        self.input_width = self.input_width()
        self.input_height = self.input_height()
        self.label_unit3 = self.__label_unit3()
        self.label_unit4 = self.__label_unit4()
        self.label_unit5 = self.__label_unit5()
    def __frame(self):
        self.configure(text="Room's dimensions")
        self.place(x=270, y=100, width=180, height=255)

    def __label_length(self):
        label = Label(self,text="Length:",anchor="center")
        label.place(x=10, y=20, width=50, height=18)
        return label

    def __label_width(self):
        label = Label(self,text="Width:",anchor="center")
        label.place(x=10, y=90, width=44, height=18)
        return label

    def __label_height(self):
        label = Label(self,text="Height:",anchor="center")
        label.place(x=10, y=160, width=48, height=18)
        return label

    def showMsg_len(self):
        return self.ipt_len.get()

    def input_length(self):
        self.ipt_len = Entry(self)
        self.ipt_len.place(x=10, y=40, width=98, height=20)
        return self.ipt_len

    def showMsg_wid(self):
        return self.ipt_wid.get()

    def input_width(self):
        self.ipt_wid = Entry(self)
        self.ipt_wid.place(x=10, y=110, width=98, height=20)
        return self.ipt_wid

    def showMsg_hgt(self):
        return self.ipt_hgt.get()

    def input_height(self):
        self.ipt_hgt = Entry(self)
        self.ipt_hgt.place(x=10, y=180, width=98, height=20)
        return self.ipt_hgt

    def __label_unit3(self):
        label = Label(self,text="m",anchor="center")
        label.place(x=110, y=41, width=15, height=19)
        return label

    def __label_unit4(self):
        label = Label(self,text="m",anchor="center")
        label.place(x=110, y=110, width=16, height=20)
        return label

    def __label_unit5(self):
        label = Label(self,text="m",anchor="center")
        label.place(x=110, y=181, width=14, height=19)
        return label

class Frame_temp(LabelFrame):
    def __init__(self,parent):
        super().__init__(parent)
        self.__frame()
        self.input_ambient = self.input_ambient()
        self.label_ambient = self.__label_ambient()
        self.label_unit6 = self.__label_unit6()
        self.label_inter = self.__label_inter()
        self.input_inter = self.input_inter()
        self._label_unit7 = self.__label_unit7()
    def __frame(self):
        self.configure(text="Temperature")
        self.place(x=40, y=380, width=230, height=99)

    def showMsg_amb(self):
        return self.ipt_amb.get()

    def input_ambient(self):
        self.ipt_amb = Entry(self)
        self.ipt_amb.place(x=70, y=10, width=97, height=24)
        return self.ipt_amb

    def __label_ambient(self):
        label = Label(self,text="Ambient:",anchor="center")
        label.place(x=10, y=10, width=57, height=24)
        return label

    def __label_unit6(self):
        label = Label(self,text="\N{DEGREE SIGN}C",anchor="center")
        label.place(x=180, y=10, width=26, height=24)
        return label

    def __label_inter(self):
        label = Label(self,text="Internal:",anchor="center")
        label.place(x=10, y=50, width=56, height=24)
        return label

    def showMsg_tin(self):
        return self.ipt_tin.get()

    def input_inter(self):
        self.ipt_tin = Entry(self)
        self.ipt_tin.place(x=70, y=50, width=97, height=24)
        return self.ipt_tin

    def __label_unit7(self):
        label = Label(self,text="\N{DEGREE SIGN}C",anchor="center")
        label.place(x=180, y=50, width=26, height=24)
        return label

class Frame_result(Frame):
    def __init__(self,parent):
        super().__init__(parent)
        self.__frame()
        self.label_hLoss = self.__label_hLoss()
        self.label_wPower = self.__label_wPower()
        self.input_hLoss = self.input_hLoss()
        self.label_unit8 = self.__label_unit8()
        self.input_wPower = self.input_wPower()
    def __frame(self):
        self.place(x=275, y=385, width=264, height=141)

    def __label_hLoss(self):
        label = Label(self,text="HEAT LOSS:",anchor="center")
        label.place(x=20, y=20, width=85, height=40)
        return label

    def __label_wPower(self):
        label = Label(self,text="W POWER REQUIRED",anchor="center")
        label.place(x=112, y=90, width=140, height=40)
        return label

    def input_hLoss(self):
        self.ipt_res = Entry(self)
        self.ipt_res.place(x=120, y=30, width=81, height=24)
        return self.ipt_res

    def __label_unit8(self):
        label = Label(self,text="W/K",anchor="center")
        label.place(x=220, y=30, width=35, height=24)
        return label

    def input_wPower(self):
        self.ipt_pow = Entry(self)
        self.ipt_pow.place(x=30, y=100, width=81, height=24)
        return self.ipt_pow
        

