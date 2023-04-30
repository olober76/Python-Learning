# GUI ->  Graphical User Interface

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# Init
window = tk.Tk()
window.configure(bg="white")
window.geometry("300x200")
window.resizable(False,False)# GUI tidak akan bisa dikostumisasi ukuran layarnya
window.title("Program Hallo")

#Variable dan fungsi
NAMA_DEPAN = tk.StringVar()
NAMA_BELAKANG = tk.StringVar()

def tombol_click():
    # print("Jaka ganteng bat")
    #Fungsi ini akan dipanggil oleh tombol
    print(NAMA_BELAKANG.get())
    pesan = f"HALO {NAMA_DEPAN.get()} {NAMA_BELAKANG.get()}"
    showinfo(title="WHAZZZUP", message=pesan)

# Frame input
input_frame = ttk.Frame(window)
#Penempatan Grid, Pack, Place
input_frame.pack(padx=10, pady=10, fill="x", expand=True)

# Komponen komponen
# 1. Label untuk nama depan
nama_depan_label = ttk.Label(input_frame, text="NAMA DEPAN")
nama_depan_label.pack(padx=10, fill="x", expand=True)

# 2. Entry nama depan

nama_depan_entry = ttk.Entry(input_frame, textvariable=NAMA_DEPAN)
nama_depan_entry.pack(padx=10, fill="x", expand=True)

# 3. Label untuk nama belakang
nama_belakang_label = ttk.Label(input_frame, text="NAMA BELAKANG")
nama_belakang_label.pack(padx=10, fill="x", expand=True)

# 4. Entry nama belakang

nama_belakang_entry = ttk.Entry(input_frame, textvariable=NAMA_BELAKANG)
nama_belakang_entry.pack(padx=10, fill="x", expand=True)

# 5. Tombol

tombol_sapa = ttk.Button(input_frame, text="Sapa!",command=tombol_click)
tombol_sapa.pack(fill='x' , expand=True, padx=10, pady=10)



#Main loop window
window.mainloop()
