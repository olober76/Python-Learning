#Graphical User Interface untuk Vision
 
from tkinter import *
import tkinter.font as tkfont
from PIL import Image, ImageTk
# from tkinter import ttk
from tkinter.messagebox import showinfo


#Init
window = Tk()
window.configure(bg="#fcba03")
window.geometry("1280x720") #Ukuran awal
window.title("Button Command")



bigFont = tkfont.Font(  
    family = "Bebas Neue",
    size = 25,
    slant = "roman",
    underline = 0,
    overstrike = 0
)



def notif_popUp():
    text = f"coba saja"
    showinfo(title="booyah",message=text)
    
    
# canva = Canvas(window, bg="#1b1b1b")
# canva.pack(fill=BOTH, expand=True)
    





# Frame input
input_frame = Frame(window,width=800,height=200, bg="blue")

#Penempatan Grid, Pack, Place
# input_frame.pack(padx=10, pady=10, fill="y", expand=True)
input_frame.pack(fill="x", expand=True)

tombol1 = Button(input_frame, text="Tombol 1", font=bigFont,command=notif_popUp)
tombol1.pack(pady=10,padx=10)








#For Looping windows
window.mainloop()
