import tkinter as tk

root = tk.Tk()
root.title("Tkinter World")

# Set the window size
root.geometry("300x150")

# label = tk.Label(root, text="Hello, Studytonight!")  Step 1
label = tk.Label(
    text="Hello, Tkinter",
    foreground="white",  # Set the text color to white
    background="black"  # Set the background color to black
)
label.pack()

entry = tk.Entry(root)
entry.pack()

# button = tk.Button(root, text="Click Me!")  Step 1
button = tk.Button(
    text="Click me!",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
)
button.pack()

root.mainloop()