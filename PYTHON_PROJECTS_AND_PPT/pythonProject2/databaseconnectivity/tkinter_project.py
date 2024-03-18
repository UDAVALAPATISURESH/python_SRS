import tkinter as tk
def say_Hello():
    print("Hello, Tkinter!")
window = tk.Tk()
window.geometry("500x600+10+20")
button = tk.Button(window,text="say Hello", command= say_Hello())
button.pack()
window.mainloop()