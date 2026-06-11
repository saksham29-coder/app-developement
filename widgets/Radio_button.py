import tkinter as tk

window = tk.Tk()
window.title("Radio_button")
window.geometry("400x200")
radio_var = tk.StringVar()
radiobutton1 = tk.Radiobutton(
    window, font=("Arial Black", 70), text="Male", variable=radio_var, indicatoron=0
)
radiobutton1.pack(padx=40, pady=40)
window.mainloop()
