import tkinter as tk
from tkinter import ttk  # Required for the Notebook widget

# Import your modified module files
# (Assuming you have turned them into classes that inherit from tk.Frame)
import log_in
import my_button  # renamed from button.py to avoid conflicts
import my_combobox

# 1. Create the Main Window
root = tk.Tk()
root.title("My Combined Tkinter App")
root.geometry("600x400")

# 2. Create the Notebook (Tab Control)
notebook = ttk.Notebook(root)
notebook.pack(pady=10, expand=True, fill="both")

# 3. Create the Frames for each tab
# We pass the 'notebook' as the parent container
tab1 = tk.Frame(notebook)
tab2 = tk.Frame(notebook)
tab3 = tk.Frame(notebook)

# 4. Add the frames to the Notebook with tab titles
notebook.add(tab1, text="Admission Page")
notebook.add(tab2, text="Submit")
notebook.add(tab3, text="Course options")

# 5. Insert your custom widgets into the respective tabs
# Tab 1: Login feature
login_widget = log_in.LoginFrame(tab1)
login_widget.pack(pady=20)

# Tab 2: Button feature (Assuming you wrapped it in a class called ButtonFrame)
button_widget = my_button.ButtonFrame(tab2)
button_widget.pack(pady=20)

# Tab 3: Combobox feature (Assuming you wrapped it in a class called ComboboxFrame)
combo_widget = my_combobox.ComboboxFrame(tab3)
combo_widget.pack(pady=20)

# Start the main loop
root.mainloop()
