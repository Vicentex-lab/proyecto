from tkinter import *

#label = un widget de área que lleva texto y/o una imagen dentro de una ventana

window = Tk()
photo = PhotoImage(file="logo.png")

label = Label(window, 
              text="soloso", 
              font=("Arial", 40, "bold"),
              fg="green", #color letra
              bg="brown",
              relief="groove", #borde
              bd=10, #tamaño del borde
              padx=20, #distancia del borde en x
              pady=20,
              image=photo,
              compound="top") #donde aparece la imagen
label.pack() #centrado
#label.place(x=0,y=0) se escoge dónde quiero que vayan en la ventana

window.mainloop()