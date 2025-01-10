import tkinter as tk
from tkinter import filedialog

root = tk.Tk()

root.geometry("500x500")
label = tk.Label(root, text="hello shit", font=("Arial", 17))

label.pack()
root.title("buto")

button = tk.Button(root)
button.pack()

make = filedialog.askopenfilename()
#path = filedialog.askdirectory(title="select a file idiot")


root.mainloop()
