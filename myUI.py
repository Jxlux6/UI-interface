# currently just a GUI box with Hello World at the top, and a small text box in the middle
# will add more later watching tutorial
# link: https://www.youtube.com/watch?v=ibf5cx221hk
import tkinter as tk

root = tk.Tk()

root.geometry("500x500")
root.title("my GUI")

label = tk.Label(root, text="Hello World", font=('Arial', 18))
label.pack(padx=20, pady=40)

textbox = tk.Text(root, height=3)
textbox.pack()




root.mainloop()

