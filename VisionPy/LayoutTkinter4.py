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
frame = tk.Frame(root, bg="#e8aa42")
frame.pack(pady=5,padx=5, fill="x", expand=True)



    
# button shape
gambar_files = ["C:/Users/kuhpr/Documents/Python/Python-Learning/VisionPy/resources/tombol 1/active.png", 
                "C:/Users/kuhpr/Documents/Python/Python-Learning/VisionPy/resources/tombol 1/active2.png", 
                "C:/Users/kuhpr/Documents/Python/Python-Learning/VisionPy/resources/tombol 1/active3.png", 
                "C:/Users/kuhpr/Documents/Python/Python-Learning/VisionPy/resources/tombol 1/active4.png", 
                "C:/Users/kuhpr/Documents/Python/Python-Learning/VisionPy/resources/tombol 1/active5.png", 
                "C:/Users/kuhpr/Documents/Python/Python-Learning/VisionPy/resources/tombol 1/active6.png"]




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
                           width=380, 
                           height=380,
                           bd=0,
                           relief="sunken",
                        #  activebackground="#e8aa42",
                           command=lambda btn=button_number: on_button_click(btn),
                           )
        button.grid(row=i, column=j, padx=5, pady=5)
        buttons.append(button)

        # rulling button.image
        button.image = photo
     

frame.grid_columnconfigure(0, weight=1)
frame.grid_columnconfigure(1, weight=1)
frame.grid_columnconfigure(2, weight=1)




root.mainloop()