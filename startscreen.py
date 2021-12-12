from tkinter import *
import os
os.system("chmod +x main.py")

def starter():
    window.destroy()
    os.system("sudo python3 main.py")
def restarter():
    window.destroy()
    os.system("sudo python3 startscreen.py")
window = Tk()
window["bg"] = "black"
window.title("Elementary tweak installer")
window.geometry('420x340')
lbl = Label(window, text="by kulisworm  <3",bg="black", fg="white")
lbl.grid(column=0, row=0)
lbl1 = Label(window, text="Убедитесь, что вы запускаете скрипт через sudo",bg="black", fg="white")
lbl1.grid(column=0, row=1)
btn = Button(window, text="Продолжить!", bg="purple", fg="white", command=starter)
btn.grid(column=0, row=2)
btn1 = Button(window, text="Перезапуск через sudo", bg="purple", fg="white", command=restarter)
btn1.grid(column=0, row=3)
window.mainloop()