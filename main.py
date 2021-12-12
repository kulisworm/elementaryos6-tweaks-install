from tkinter import *
from tkinter import ttk
import os


def install_tweaks():
    os.system("clear")
    os.system("sudo apt install software-properties-common -y")
    os.system("sudo add-apt-repository ppa:philip.scott/pantheon-tweaks")
    os.system("sudo apt update")
    os.system("sudo apt install pantheon-tweaks")
    os.system("clear")
    print("Installed!!!")
def install_package():
    os.system(txt.get())
window = Tk()
window["bg"] = "black"
window.title("Elementary tweaks installer")
window.geometry('530x220')
qbtn = Button(window, text="Выйти", bg="green", fg="white", command=window.destroy)
qbtn.grid(column=0, row=0)
lbl = Label(window, text="Выберите пункт",bg="black", fg="white")
lbl.grid(column=0, row=1)
lbl1 = Label(window, text="Cледите за процессом установки, где то понадобится подтверждение пользователя",bg="black", fg="white")
lbl1.grid(column=0, row=2)
btn = Button(window, text="Установить твики", bg="purple", fg="white", command=install_tweaks)
btn.grid(column=0, row=3)
lbl2 = Label(window, text="Исполнение команд, введите ниже команду",bg="black", fg="white")
lbl2.grid(column=0, row=4)
btn1 = Button(window, text="Исполнить", bg="purple", fg="white", command=install_package)
btn1.grid(column=0, row=5)
txt = Entry(window,width=10, bg="white")
txt.grid(column=0, row=6)
window.mainloop()