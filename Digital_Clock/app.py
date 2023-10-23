import tkinter as tk
from time import strftime

def time():
    string = strftime("%H:%M:%S %p")
    label.config(text=string)
    label.after(1000, time)
def on_resize(event):
    label.config(font=('Helvetica',max(20, event.width // 15)))

root = tk.Tk()
root.title("Digital Clock")
root.geometry("400x200")

label = tk.Label(root, font=('Helvetica', 30), background='black', foreground='white')
label.pack(fill='both', expand=True)

time()

root.bind("<Configure>", on_resize)

root.mainloop()
