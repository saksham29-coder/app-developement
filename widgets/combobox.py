import tkinter as tk
from tkinter import ttk  # Required to use the Combobox widget

window = tk.Tk()
window.title("Combo_box")
window.geometry("400x200")


def combobox_selected(event):
    # Completing your line to grab the value
    selected_value = my_combo.get()

    # Updating a label to show the choice

    result_label.config(text=f"Selected: {selected_value}")


# --- Setup the Combobox ---

# 1. Create the combobox and give it a list of values
my_combo = ttk.Combobox(window, values=["Red", "Green", "Blue"])
my_combo.pack(pady=20)

# 2. Bind the event so choosing an item triggers your function above
my_combo.bind("<<ComboboxSelected>>", combobox_selected)

# --- Setup the Display Label ---

# 3. Create a basic label so we can see the output change
result_label = tk.Label(window, text="Please select a color.")
result_label.pack(pady=10)

# Start the window
window.mainloop()
