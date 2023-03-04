from tkinter import*

window=tk()
canvas=Canvas(window,height=500,wigth=500)

#canvas.create_line(0,0,500,500,fill=(“blue”,width=5))
canvas.create_line(0,500,500,fill=(“red”,width=5))
canvas.create_rectangle(50,50,250,250,fill=(“purple”))
canvas.create_triangle(0,0,500,500,fill=(“blue”,width=5))
points=[0250,0,500,500,0,500]
canvas.create_polygon(points,fill=(“yellow,outline=black,width=5))
canvas.create_arc(0,0,500,500,fill=(“greene”,style=pieslice,start=270,width=5))
canvas.create_arc(0,0,500,500,fill=(“red”,extent=180,width=10))
canvas.create_arc(0,0,500,500,fill=(“white”,extent=180,start=180,width=10))
canvas.create_oval(190,0,500,500,fill=(“red”,extent=100,width=10))

canvas.pack()
window.mainloop()
