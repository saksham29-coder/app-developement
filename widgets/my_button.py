import tkinter as tk


class ButtonFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Attach the button to 'self' and point the command to 'self.button_clicked'
        self.button = tk.Button(
            self, text="Hello, student click me", command=self.button_clicked
        )
        self.button.pack(padx=20, pady=20)

    def button_clicked(self):
        print("Button-clicked")
