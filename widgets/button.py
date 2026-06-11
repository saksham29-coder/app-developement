import tkinter as tk

window = tk.Tk()
window.title("hello,NIET")


def Button_clicked():
    print("Button-clicked")


button = tk.Button(window, text="Hello,student click me", command=Button_clicked)
button.pack(padx=20, pady=20)
window.mainloop()
