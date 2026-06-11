# window.mainloop()


import tkinter as tk

window = tk.Tk()
window.title("Login Example")


def submit_clicked():
    result_label.config(text="Good Job")


# Username
username_label = tk.Label(window, text="Username")
username_label.grid(row=0, column=0, padx=10, pady=5)

username_entry = tk.Entry(window)
username_entry.grid(row=0, column=1, padx=10, pady=5)

# Password
password_label = tk.Label(window, text="Password")
password_label.grid(row=1, column=0, padx=10, pady=5)

password_entry = tk.Entry(window, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=5)

# Submit Button
submit_button = tk.Button(window, text="Login", command=submit_clicked)
submit_button.grid(row=2, column=0, columnspan=2, pady=10)

# Result Label
result_label = tk.Label(window, text="")
result_label.grid(row=3, column=0, columnspan=2)

window.mainloop()
