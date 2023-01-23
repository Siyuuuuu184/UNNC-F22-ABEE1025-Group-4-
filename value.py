from tkinter import *
from tkinter.messagebox import *
import time
class calc(object):
	def __init__(self, root):
 		super(calc, self).__init__()
 		self.root = root

 		#result display
 		self.res_text = Text(self.root,width=10,height=2,bg='#484848',fg='white',relief="flat")
 		self.res_text.grid(row=7,column=3)

 		#temperature gui set
 		Label(self.root, text='----- Temperature -----',bg='#484848',fg='white'
 			).grid(row=0,column=0,columnspan=3)
 		Label(self.root, text='Indoor Temperature:',bg='#484848',fg='white'
 			).grid(row=1,column=0)
 		Label(self.root, text='Outdoor Temperature:',bg='#484848',fg='white'
 			).grid(row=2,column=0)
 		Label(self.root, text="\N{DEGREE SIGN}C",bg='#484848',fg='white'
 			).grid(row=1,column=2)
 		Label(self.root, text="\N{DEGREE SIGN}C",bg='#484848',fg='white'
 			).grid(row=2,column=2)

 		#temperature entry
 		self.inEntry = Entry(self.root,width=5,relief="groove")
 		self.inEntry.grid(row=1,column=1,padx=5,pady=10)
 		self.outEntry = Entry(self.root,width=5,relief="groove")
 		self.outEntry.grid(row=2,column=1,padx=5,pady=10)


 		#area gui set
 		Label(self.root, text='----- Room \'s Dimension -----',bg='#484848',fg='white'
 			).grid(row=4,column=0,columnspan=3)
 		Label(self.root, text='Width:',bg='#484848',fg='white'
 			).grid(row=5,column=0)
 		Label(self.root, text="Length:",bg='#484848',fg='white',
 			).grid(row=6,column=0)
 		Label(self.root, text="m",bg='#484848',fg='white'
 			).grid(row=5,column=2)
 		Label(self.root, text="m",bg='#484848',fg='white'
 			).grid(row=6,column=2)

 		#room's dimension entry
 		self.width= Entry(self.root,width=5,relief="groove")
 		self.width.grid(row=5,column=1,padx=5,pady=10)
 		self.length = Entry(self.root,width=5,relief="groove")
 		self.length.grid(row=6,column=1,padx=5,pady=10)

 		self.res_display()
 		#valueList = {} #create an empty dictionary to save the values
 
	def delta_t_calc(self):
		try:
			self.t_in = float(self.inEntry.get())	
			self.t_out = float(self.outEntry.get())
		except:
			return showwarning('ValueError:','Please enter numbers')
		self.delta_t = self.t_in - self.t_out
		return self.delta_t

	def area_calc(self):
		try:
			self.width= float(self.inEntry.get())	
			self.length = float(self.outEntry.get())
		except:
			return showwarning('ValueError:','Please enter numbers')
		self.area = self.width * self.length
		return self.area

	def u_value_calc(self):
		pass

	def res_display(self):
		self.res = Button(self.root,text='calculate \n now',
			command=lambda: self.update(),relief="groove",bg="#393939",fg="white")
		#lambda: make self.update() only used by self.res_display
		self.res.grid(row=7,column=0,sticky=E+W)

	def update(self):
		while  True:
			self.result = self.delta_t_calc() * self.area_calc()
			self.res_text.delete('1.0','end')
			self.res_text.insert(END,str(self.result))

			self.root.update()
			time.sleep(1)

	'''	
	def res_show(self):
		self.res = Button(self.root,text='calculate \n now',
			relief="groove",bg="#393939",fg="white")
		#lambda: make self.delta_t_calc() only used by self.res_calc
		self.res.grid(row=2,column=0,sticky=E+W)
		self.res.bind("<Button-1>",self.res_calc) 
	'''
