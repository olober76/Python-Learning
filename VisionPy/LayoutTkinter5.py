import tkinter as tk
from tkinter.messagebox import showinfo
from PIL import Image, ImageTk
import tkinter.font as tkfont

def on_button_click( button_number ):
   
    if button_number == 1:
        '''Kasih commandnya bang'''
        pesan = f"command untuk nomor {button_number}"
        # showinfo(title=f"POP UP", message=pesan)
        print(pesan)
    elif button_number == 2:
        '''Kasih commandnya bang'''
        pesan = f"command untuk nomor {button_number}"
        # showinfo(title="POP UP ", message=pesan)
        print(pesan)
    elif button_number == 3:
        '''Kasih commandnya bang'''
        pesan = f"command untuk nomor {button_number}"
        # showinfo(title="POP UP ", message=pesan)
        print(pesan)
    elif button_number == 4:
        '''Kasih commandnya bang'''
        pesan = f"command untuk nomor {button_number}"
        # showinfo(title="POP UP ", message=pesan)
        print(pesan)
    elif button_number == 5:
        '''Kasih commandnya bang'''
        pesan = f"command untuk nomor {button_number}"
        # showinfo(title="POP UP ", message=pesan)
        print(pesan)
    elif button_number == 6:
        '''Kasih commandnya bang'''
        pesan = f"command untuk nomor {button_number}"
        # showinfo(title="POP UP ", message=pesan)
        print(pesan)
    



root = tk.Tk()
root.configure(bg="#e57c23")
root.geometry("1280x720") #Ukuran awal
root.title("Button Command")




# Membuat frame untuk menampung tombol
frame = tk.Frame(root, width=800, height=400, bg="#e8aa42")
frame.pack(pady=5,padx=5, fill="x", expand=True)



    
# button shape
# POKOKNYA DIREKTORI LANGSUNG KE RESOURCENYA
gambar_files = ["../VisionPy/resources/tombol 1/active.png", 
                "../VisionPy/resources/tombol 1/active2.png", 
                "../VisionPy/resources/tombol 1/active3.png", 
                "../VisionPy/resources/tombol 1/active4.png", 
                "../VisionPy/resources/tombol 1/active5.png", 
                "../VisionPy/resources/tombol 1/active6.png"]

gambar_files2 = ["../VisionPy/resources/tombol 1/inactive.png", 
                "../VisionPy/resources/tombol 1/inactive2.png", 
                "../VisionPy/resources/tombol 1/inactive3.png", 
                "../VisionPy/resources/tombol 1/inactive4.png", 
                "../VisionPy/resources/tombol 1/inactive5.png", 
                "../VisionPy/resources/tombol 1/inactive6.png"]


def on_enter(event):
    button.config(image=gambar_files)
def on_leave(enter):
    button.config(image=gambar_files2)
    
    
bigFont = tkfont.Font(  
    family = "Bebas Neue",
    size = 40,
    slant = "roman",
    underline = 0,
    overstrike = 0,
    
)



# Membuat label dengan tulisan besar
label = tk.Label(root, 
                 text="MAHAREKSA UB", 
                 font=bigFont,
                 padx=5,
                 pady=5,
                 highlightthickness=0,  # Menghapus highlight border
                 bd=0,  # Menghapus border
                 background="#e8aa42",  # Atur background label sesuai dengan background root
                 foreground="#f8f1f1"  # Warna teks
                 
                 )

label.place(relx=0.5, rely=0.05, anchor="center")



# Membuat list tombol
buttons = []
for i in range(2):
    for j in range(3):
        button_number = i * 3 + j + 1

        # Membuka gambar menggunakan PIL
        image = Image.open(gambar_files[button_number-1])

        # Mengubah gambar menjadi objek PhotoImage Tkinter
        photo = ImageTk.PhotoImage(image)

        # Membuat tombol dengan gambar sebagai tampilan
        button = tk.Button(frame, 
                           image=photo, 
                           width=400, 
                           height=400,
                           border='0',
                           relief="sunken",
                           activebackground="#e8aa42",
                           command=lambda btn=button_number: on_button_click(btn),
                           )
        button.grid(row=i, column=j, padx=5, pady=5)
        buttons.append(button)

        # rulling button.image
        button.image = photo
     
frame.grid_columnconfigure(0, weight=1)
frame.grid_columnconfigure(1, weight=1)
frame.grid_columnconfigure(2, weight=1)

# button.bind("<Enter>", on_enter)
# button.bind("<Leave>", on_leave)


root.mainloop()