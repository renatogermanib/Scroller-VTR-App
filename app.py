from tkinter import Button, Tk, Frame, Entry, END
#config ventana:
ventana = Tk()
ventana.geometry('186x253')
ventana.config(bg='dark slate gray')
ventana.iconbitmap(bitmap='icono.ico')
ventana.resizable(0,0)
ventana.title('análisis')

#clase para efecto hover
class HoverButton(Button):
	def __init__(self,master,**kw):
		Button.__init__(self,master=master,**kw)
		self.defaultBackground = self['background']
		self.bind('<Enter>', self.on_enter)
		self.bind('<Leave>', self.on_leave)

	def on_enter(self, e):
		self['background'] = self['activebackground']
	def on_leave(self, e):
		self['background'] = self.defaultBackground

i=0

def scroll(*events): #función relacionada al boton =
	global i
	i += 14
	Resultado.delete(0, END)
	Resultado.insert(0,i)

def rollback(*events):
	global i
	if i != 0:
		i -= 14
		Resultado.delete(0, END)
		Resultado.insert(0,i)
	else:
		i = 0
		Resultado.delete(0, END)
		Resultado.insert(0,i)

def reset(*events):
	global i
	Resultado.delete(0, END)
	i=0
	Resultado.insert(0,i)

'''
frame = Frame(ventana, bg='dark slate gray', relief='raised', width=500, height=500)
frame.grid()
'''

scroll_button = HoverButton(ventana, text= "SCROLL ONE PAGE", height=2, width=18,font= ('Bahnschrift',13), borderwidth=2,  relief = "raised", activebackground="dark goldenrod", bg='gold',  anchor="center",command=lambda: scroll())  
scroll_button.grid(column =1, row=1, pady=4,padx=7)

rollback_button = HoverButton(ventana, text= "Rollback one page", height=2, width=18,font= ('Bahnschrift',13), borderwidth=2,  relief = "raised", activebackground="dark goldenrod", bg='gold',  anchor="center",command=lambda: rollback())  
rollback_button.grid(column =1, row=2, pady=4,padx=7)

reset_button = HoverButton(ventana, text= "Start Again", height=2, width=18,font= ('Bahnschrift',13), borderwidth=2,  relief = "raised", activebackground="dark goldenrod", bg='gold',  anchor="center",command=lambda: reset())  
reset_button.grid(column =1, row=3, pady=4,padx=7)


Resultado = Entry(ventana, bg='gray', width=10, relief='groove', font =('Bahnschrift',20), justif='center')
Resultado.grid(columnspan=10 , row=4, pady=3,padx=1, ipadx=1, ipady=1)

ventana.bind('<space>', scroll)
ventana.bind('<BackSpace>', rollback)
ventana.bind('<Delete>', reset)
ventana.mainloop()

# < >