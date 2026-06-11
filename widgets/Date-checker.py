import tkinter as tk
from tkcalendar import DateEntry

root = tk.Tk()
root.title("Date Picker")
root.geometry("400x200")
date_entry = DateEntry(root)
date_entry.pack()
root.mainloop()
