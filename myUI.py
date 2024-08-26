# importing tkinter and a messagebox
import tkinter as tk
from tkinter import messagebox

# tk opens the main window

root = tk.Tk()
root.title("UI Interface")

# creates message box
messagebox.showinfo(
    title="UI Interface",
    message="TEST UI interface has been opened."
)

# keeps window open until closed by user
root.mainloop()
