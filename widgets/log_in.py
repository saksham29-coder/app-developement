import tkinter as tk


class LoginFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Username
        self.username_label = tk.Label(self, text="Username")
        self.username_label.grid(row=0, column=0, padx=10, pady=5)

        self.username_entry = tk.Entry(self)
        self.username_entry.grid(row=0, column=1, padx=10, pady=5)

        # Mobile no
        self.password_label = tk.Label(self, text="Mobile no")
        self.password_label.grid(row=1, column=0, padx=10, pady=5)

        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.grid(row=1, column=1, padx=10, pady=5)

        # Submit Button
        self.submit_button = tk.Button(self, text="Submit", command=self.submit_clicked)
        self.submit_button.grid(row=2, column=0, columnspan=2, pady=10)

        # Result Label
        self.result_label = tk.Label(self, text="")
        self.result_label.grid(row=3, column=0, columnspan=2)

    def submit_clicked(self):
        self.result_label.config(text="Course Selected")
