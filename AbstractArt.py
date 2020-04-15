from tkinter import *
from random import *
tk=Tk()
canvas = Canvas(tk, height=500,width=500)
def AbstractArt():
	for a in range(0,35):
		color = randrange(1,6)
		x1 = randrange(0,500)
		x2 = randrange(0,500)
		y1 = randrange(0,500)
		y2 = randrange(0,500)
		if color == 1:
			canvas.create_rectangle(x1,y1,x2,y2, fill="red")
		if color == 2:
			canvas.create_rectangle(x1,y1,x2,y2, fill="green")
		if color == 3:
			canvas.create_rectangle(x1,y1,x2,y2, fill="blue")
		if color == 4:
			canvas.create_rectangle(x1,y1,x2,y2, fill="yellow")
		if color == 5:
			canvas.create_rectangle(x1,y1,x2,y2, fill="purple")

			
btn = Button(tk, text = "Generate Art!", command=AbstractArt)
canvas.pack()
btn.pack()
tk.mainloop()
input()
