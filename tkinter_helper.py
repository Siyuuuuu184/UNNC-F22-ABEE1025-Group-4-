from tkinter import *
from tkinter.ttk import *

'''
# 自动隐藏滚动条
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

'''
    
class WinGUI(Tk):
    def __init__(self):
        super().__init__()
        self.__win()
        #signs on the top
        self.label_ideal = self.label_ideal()
        self.label_current = self.__label_current()
        self.input_ideal = self.__input_ideal()
        self.input_current = self.__input_current()
        self.label_unit1 = self.__label_unit1()
        self.label_unit = self.__label_unit()
        self.input_difference = self.__input_difference()
        self.label_unit2 = self.__label_unit2()

        #frames
        self.label_frame_feature = Frame_feature(self)
        self.label_frame_dimension = Frame_dimension(self)        
        self.label_frame_temp = Frame_temp(self)
        self.frame_result = Frame_result(self)
        self.button_more = self.__button_more()
        self.button_calcNow = self.__button_calcNow()

        #values needed later
        self.level = ""
    def get_level(self):
        self.level = self.label_frame_feature.showMsg()
        return self.level
    def set_level(self,level):
        self.level = level
    #no1. 上面这一小坨每个人都要有的 用来传数据给event.py的

    def __win(self):
        self.title("Heat Loss Calculator")
        width = 550
        height = 540
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)
        self.resizable(width=True, height=True)

    def label_ideal(self):
        label = Label(self,text="Your ideal heat loss:",anchor="center")
        label.place(x=40, y=20, width=145, height=18)
        return label

    def __label_current(self):  
        label = Label(self,text="The current simulated heat loss:",anchor="center")
        label.place(x=40, y=51, width=212, height=19)
        return label

    def __input_ideal(self):
        ipt = Entry(self)
        ipt.place(x=187, y=20, width=59, height=20)
        return ipt

    def __input_current(self):
        ipt = Entry(self)
        ipt.place(x=257, y=50, width=59, height=20)
        return ipt

    def __label_unit1(self):
        label = Label(self,text="W/K.",anchor="center")
        label.place(x=240, y=20, width=28, height=20)
        return label

    def __label_unit(self):
        label = Label(self,text="W/K.",anchor="center")
        label.place(x=310, y=50, width=35, height=21)
        return label

    def __input_difference(self):
        ipt = Entry(self)
        ipt.place(x=420, y=50, width=78, height=21)
        return ipt

    def __label_unit2(self):
        label = Label(self,text="W/K.",anchor="center")
        label.place(x=500, y=50, width=34, height=21)
        return label

    def __button_more(self):
        btn = Button(self, text="More")
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
        self.select_box_insu = self.__select_box_insu()
        self.select_box_wall = self.__select_box_wall()
        self.label_level = self.__label_level()
        self.label_insu = self.__label_insu()
        self.label_wall = self.__label_wall()
    def __frame(self):
        self.configure(text="Room's feature")
        self.place(x=40, y=100, width=180, height=255)

    #no2 showMsg和cb.bind每个都会有的，如果要在外部调用就要把前面的两杠杠删掉，
    #两杠杠表示它是私有函数
    def showMsg(self, *arg):
        return self.var.get()

    def select_box_level(self):
        self.var = StringVar()
        self.cb = Combobox(self, state="readonly",textvariable=self.var)
        self.cb['values'] = ("Ground floor","Intermediated level","Top floor")
        self.cb.place(x=10, y=40, width=150, height=24)
        self.cb.bind('<<ComboboxSelected>>',self.showMsg)
        return self.cb

    def __select_box_insu(self):
        cb = Combobox(self, state="readonly")
        cb['values'] = ("Insulation","No extra insulation","Mediocre insulation","Very well insulated")
        cb.place(x=10, y=110, width=150, height=24)
        return cb

    def __select_box_wall(self):
        cb = Combobox(self, state="readonly")
        cb['values'] = ("1","2","3","4")
        cb.place(x=10, y=180, width=150, height=24)
        return cb

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
        self.input_length = self.__input_length()
        self.input_width = self.__input_width()
        self.input_height = self.__input_height()
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

    def __input_length(self):
        ipt = Entry(self)
        ipt.place(x=10, y=40, width=98, height=20)
        return ipt

    def __input_width(self):
        ipt = Entry(self)
        ipt.place(x=10, y=110, width=98, height=20)
        return ipt

    def __input_height(self):
        ipt = Entry(self)
        ipt.place(x=10, y=180, width=98, height=20)
        return ipt

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
        self.input_ambient = self.__input_ambient()
        self.label_ambient = self.__label_ambient()
        self.label_unit6 = self.__label_unit6()
        self.label_inter = self.__label_inter()
        self.input_inter = self.__input_inter()
        self._label_unit7 = self.__label_unit7()
    def __frame(self):
        self.configure(text="Temperature")
        self.place(x=40, y=380, width=230, height=99)

    def __input_ambient(self):
        ipt = Entry(self)
        ipt.place(x=70, y=10, width=97, height=24)
        return ipt

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

    def __input_inter(self):
        ipt = Entry(self)
        ipt.place(x=70, y=50, width=97, height=24)
        return ipt

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
        self.input_hLoss = self.__input_hLoss()
        self.label_unit8 = self.__label_unit8()
        self.input_wPower = self.__input_wPower()
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

    def __input_hLoss(self):
        ipt = Entry(self)
        ipt.place(x=120, y=30, width=81, height=24)
        return ipt

    def __label_unit8(self):
        label = Label(self,text="W/K",anchor="center")
        label.place(x=220, y=30, width=35, height=24)
        return label

    def __input_wPower(self):
        ipt = Entry(self)
        ipt.place(x=30, y=100, width=81, height=24)
        return ipt
        

