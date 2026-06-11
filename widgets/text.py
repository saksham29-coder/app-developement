import tkinter as tk

window = tk.Tk()  # Create Window
window.title("Login Page")  # Give title to window
window.geometry("400x200")  # Set size of window
label = tk.Label(
    window, text="Welcome", font=("Arial Bold", 40)
)  # Print text and set size
label.config(bg="white", fg="Blue")  # Give colour to font
label.pack(pady=50, ipady=50)  # Set margins and alignment
window.mainloop()
