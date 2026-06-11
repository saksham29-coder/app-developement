import tkinter as tk

window = tk.Tk()
window.title("Spinbox")
window.geometry("400x200")
spinbox = tk.Spinbox(window, from_=0, to=100)
spinbox.pack()
window.mainloop()
