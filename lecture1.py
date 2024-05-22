import tkinter as tk
def greet():
    name = entry.get()
    label.config(text=f"Hello, {name}!")
 # Create main window
root = tk.Tk()
root.title("Greeting App")
 # Create entry field
entry = tk.Entry(root)
entry.pack()
# Create button to trigger greeting
button = tk.Button(root, text="Greet", command=greet)
button.pack()
 # Create label for greeting message
label = tk.Label(root, text="")
label.pack()
 # Start the Tkinter event loop
root.mainloop()