from tkinter import *
from tkinter import ttk 
from settings import Settings
from value import calc
#import main as mn
root = Tk()
cal_settings = Settings()
root.title(cal_settings.title)
root.geometry(cal_settings.geometry)
root.configure(bg="#484848")

runner = calc(root)

root.mainloop()
#cal_settings = Settings()
'''
class s:
	def __init__(self,root):
		self.root = root

	def run(self):
	#create a window
		self.root = Tk()
		self.cal_settings = Settings()
		self.root.title(self.cal_settings.title)
		self.root.geometry(self.cal_settings.geometry)
		self.root.configure(bg="#484848")
		self.root.mainloop()
'''

'''
def delta_t_calc():
	t_in = float(inEntry.get())
	t_out = float(outEntry.get())
	delta_t = t_in - t_out
	return print(delta_t)
inEntry = Entry(root,width=5,relief="groove")
inEntry.grid(row=0,column=0,padx=20,pady=20)
outEntry = Entry(root,width=5,relief="groove")
outEntry.grid(row=1,column=0,padx=20,pady=20)
'''
'''
res = Button(root,text='calculate \n now',command=delta_t_calc,relief="groove",bg="#393939",fg="white")
res.grid(row=2,column=0,)
'''

'''
u = StringVar()
u_entry = Entry(root,textvariable=u,width=3).grid(
			row=10,column=10)
u_value = float(u_entry.get())
'''
#a page 
#page = Frame(root)
#page.pack()

#result = Result(root)






#run = run_calculator()