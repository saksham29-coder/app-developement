import tkinter as tk

window = tk.Tk()
window.title("List_box")
window.geometry("400x200")
listbox = tk.Listbox(window)
listbox.insert(1, "B.tech")
listbox.insert(2, "M.tech")
listbox.insert(3, "BCA")
listbox.pack()
window.mainloop()
