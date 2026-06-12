import tkinter as tk
from tkinter import ttk  # Required to use the Combobox widget


class ComboboxFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # 1. Create the combobox and give it a list of values
        self.my_combo = ttk.Combobox(self, values=["B.tech", "M.tech", "BCA"])
        self.my_combo.pack(pady=20)

        # 2. Bind the event so choosing an item triggers your function below
        self.my_combo.bind("<<ComboboxSelected>>", self.combobox_selected)

        # 3. Create a basic label so we can see the output change
        self.result_label = tk.Label(self, text="Please select a course.")
        self.result_label.pack(pady=10)

    def combobox_selected(self, event):
        # Grab the value and update the label
        selected_value = self.my_combo.get()
        self.result_label.config(text=f"Selected: {selected_value}")
