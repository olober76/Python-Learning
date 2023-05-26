import tkinter as tk
from tkinter.messagebox import showinfo
import tkinter.font as tkfont

def on_button_click( button_number ):
   
    if button_number == 1:
        '''Kasih commandnya bang'''
        pesan = f"command untuk nomor {button_number}"
        showinfo(title=f"POP UP", message=pesan)
    elif button_number == 2:
        '''Kasih commandnya bang'''
        pesan = f"command untuk nomor {button_number}"
        showinfo(title="POP UP ", message=pesan)
    elif button_number == 3:
        '''Kasih commandnya bang'''
        pesan = f"command untuk nomor {button_number}"
        showinfo(title="POP UP ", message=pesan)
    elif button_number == 4:
        '''Kasih commandnya bang'''
        pesan = f"command untuk nomor {button_number}"
        showinfo(title="POP UP ", message=pesan)
    elif button_number == 5:
        '''Kasih commandnya bang'''
        pesan = f"command untuk nomor {button_number}"
        showinfo(title="POP UP ", message=pesan)
    elif button_number == 6:
        '''Kasih commandnya bang'''
        pesan = f"command untuk nomor {button_number}"
        showinfo(title="POP UP ", message=pesan)
    



root = tk.Tk()
root.configure(bg="#fcba03")
root.geometry("1280x720") #Ukuran awal
root.title("Button Command")

bigFont = tkfont.Font(  
    family = "Bebas Neue",
    size = 40,
    slant = "roman",
    underline = 0,
    overstrike = 0
)

# Membuat frame untuk menampung tombol
frame = tk.Frame(root, bg="#03e8fc")
frame.pack(pady=5,padx=5, fill="x", expand=True)

# Membuat tombol-tombol
buttons = []
for i in range(2):
    for j in range(3):
        button_number = i*3+j+1
        button = tk.Button(
            frame, 
            text=f"Tombol {button_number}", 
            font=bigFont,
            width= 9, 
            height= 3, 
            command=lambda btn=button_number: on_button_click(btn)
            )
        button.grid(row=i, column=j, padx=20, pady=20, sticky="nsew")
        buttons.append(button)
        
frame.grid_columnconfigure(0, weight=1)
frame.grid_columnconfigure(1, weight=1)
frame.grid_columnconfigure(2, weight=1)

root.mainloop()
