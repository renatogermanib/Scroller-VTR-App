from tkinter import Button, Tk, Frame, Entry, END
#config ventana:
ventana = Tk()
ventana.geometry('240x280')
ventana.config(bg='red')
ventana.iconbitmap(bitmap='icono.ico')
ventana.resizable(0,0)
ventana.title('análisis')

#clase efecto hover
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
'''
def obtener(dato):
	global i
	i+=1
	Resultado.insert(i, dato)
'''
def operacion(): #función relacionada al boton =
	print('soy la función')
	i = 0
	#ecuacion = Resultado.get()
	if i == 0: #si se ingresó un dato
		try:
			print('soy la función dentro del try')
			#result = str(eval(ecuacion)) #eval transforma strings en operaciones matemáticas
			result = i + 14
			Resultado.delete(0, END)
			Resultado.insert(0,"hola")
			longitud = len(result)
			i = longitud
			
		except:
			result = 'ERROR'
			Resultado.delete(0,END)
			Resultado.insert(0,result)
	else:
		pass

def eliminar():
	global i
	Resultado.delete(i, END)
	i=0

def limpiar():
	Resultado.delete(0, END)
	i=0

frame = Frame(ventana, bg='gray', relief='raised')
frame.grid(column=0, row=0, padx=1, pady=3, ipadx=1, ipady=1)
'''
Resultado = Entry(frame, bg='#9EF8E8', width=18, relief='groove', font='Monstserrat 16', justif='right')
Resultado.grid(columnspan=4 , row=0, pady=3,padx=1, ipadx=1, ipady=1) 

Button_borrar = HoverButton(frame, text= "⌫", height=2, width=5,font= ('Comic sens MC',12,'bold'), borderwidth=2,  relief = "raised", activebackground="red", bg='#FD0371',  anchor="center",command=lambda: eliminar())  
Button_borrar.grid(column =3, row=1, pady=2,padx=2)

Button_mas = HoverButton(frame, text= "+", height=2, width=5,font= ('Comic sens MC',12,'bold'), borderwidth=2,  relief = "raised", activebackground="#FEEF02", bg='#2A16F7',  anchor="center",command=lambda: obtener('+'))  
Button_mas.grid(column =3, row=2, pady=2,padx=2)


Button_punto = HoverButton(frame, text= ".", height=2, width=5,font= ('Comic sens MC',12,'bold'), borderwidth=2,  relief = "raised", activebackground="aqua",bg ='#999AB8', anchor="center",command=lambda: obtener('.'))  
Button_punto.grid(column =1 , row=4, pady=1,padx=1)

Button_entre = HoverButton(frame, text= "÷", height=2, width=5,font= ('Comic sens MC',12,'bold'), borderwidth=2,  relief = "raised", activebackground="#FEEF02",bg ='#2A16F7',  anchor="center",command=lambda: obtener('/'))  
Button_entre.grid(column =2, row=4, pady=1,padx=1)

Button_por = HoverButton(frame, text= "x", height=2, width=5,font= ('Comic sens MC',12,'bold'), borderwidth=2,  relief = "raised", activebackground="#FEEF02", bg='#2A16F7',  anchor="center",command=lambda: obtener('*'))  
Button_por.grid(column =3, row=4, pady=2,padx=2)

Button_igual = HoverButton(frame, text= "=", height=2, width=12,font= ('Comic sens MC',12,'bold'), borderwidth=2,  relief = "raised", activebackground="#16FD03", bg='#2FEC71', anchor="center",command=lambda: operacion())  
Button_igual.grid(column =1 ,columnspan=2, row=5, pady=1,padx=1)

Button_borrar = HoverButton(frame, text= "C", height=2, width=5,font= ('Comic sens MC',12,'bold'), borderwidth=2, relief = "raised", activebackground="red", bg='#FD5603', anchor="center",command=lambda: limpiar())  
Button_borrar.grid(column =3, row=5, pady=2,padx=2)
'''
scroll = HoverButton(frame, text= "SCROLL ONE PAGE", height=2, width=18,font= ('Bahnschrift',13), borderwidth=2,  relief = "raised", activebackground="dark goldenrod", bg='gold',  anchor="center",command=lambda: operacion())  
scroll.grid(column =3, row=1, pady=2,padx=2)

Resultado = Entry(frame, bg='#9EF8E8', width=18, relief='groove', font='Monstserrat 16', justif='right')
Resultado.grid(columnspan=4 , row=0, pady=3,padx=1, ipadx=1, ipady=1)

ventana.mainloop()

# < >