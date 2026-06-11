import tkinter as tk

window = tk.Tk()
window.title("Slider")
window.geometry("400x200")
scale = tk.Scale(window, from_=0, to=100, orient=tk.HORIZONTAL)
scale.pack()
window.mainloop()
