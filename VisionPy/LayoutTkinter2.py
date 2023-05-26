from tkinter import *
from PIL import Image, ImageTk

window = Tk()
window.geometry("1280x720")

canva = Canvas(window, bg="#fcba03")
canva.pack(fill=BOTH, expand=TRUE)

btn_inactive = Image.open()#directory gambar
btn_active = Image.open()#directory gambar
                        
