from tkinter import *

window = Tk() #Instanciar una instancia de una ventana
window.geometry("420x420")
window.title("Bro Code first GUI program")

icon = PhotoImage(file='logo.png')
window.iconphoto(True, icon)
window.config(background="#7302c9")

window.mainloop() #Colocar la ventana en la pantalla, esperar eventos