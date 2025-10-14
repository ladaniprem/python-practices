# Tkinter is Python's standard GUI library for creating desktop applications
# - tk.Label(): Creates a label widget to display text
# - tk.Entry(): Creates a single-line text input field
# - tk.Button(): Creates a clickable button
# - pack(): Geometry manager that organizes widgets in blocks
# - pady: Adds vertical padding (space) around widgets
# - command: Links button click to a function
# - get(): Retrieves text from Entry widget
# - config(): Updates widget properties dynamically

# import tkinter as tk

# root = tk.Tk()
# root.title("Text Box Example")
# root.geometry("300x200")

# def display_text():
#     entered_text = entry.get()
#     label.config(text=f"var entered: {entered_text}")

# entry = tk.Entry(root, width=25)
# entry.pack(pady=10)
# # Add descriptive text label above entry
# theory_label = tk.Label(root, text="Enter text below:", fg="black", font=("Arial", 10))
# theory_label.pack(pady=5)

# submit_button = tk.Button(root, text="submit", command=display_text)
# submit_button.pack(pady=5)

# label = tk.Label(root, text="", fg="blue", font=("Arial", 12))
# label.pack(pady=10)

# root.mainloop()

# import tkinter as tk
# from tkinter import ttk

# root = tk.Tk()
# root.title("Widgets Example")
# root.geometry("400x400")

# # Label
# label = tk.Label(root, text="Enter your name:")
# label.pack()

# # Textbox
# entry = tk.Entry(root)
# entry.pack()

# # Button
# btn = tk.Button(root, text="Click Me", command=lambda: print("Hello", entry.get()))
# btn.pack()

# # Combobox
# combo = ttk.Combobox(root, values=["Python", "Java", "C++"])
# combo.pack()

# # Dropdown List
# var = tk.StringVar(root)
# var.set("Select Option")
# drop = tk.OptionMenu(root, var, "Option1", "Option2", "Option3")
# drop.pack()

# # Progress bar
# progress = ttk.Progressbar(root, length=200, mode="determinate")
# progress['value'] = 60
# progress.pack()

# root.mainloop()

# import tkinter as tk
# from PIL import Image, ImageTk  # install pillow library

# root = tk.Tk()
# root.title("Image Example")

# img = Image.open("closures.jpg")   # use your own image
# photo = ImageTk.PhotoImage(img)

# label = tk.Label(root, image=photo)
# label.pack()

# root.mainloop()

# import tkinter as tk

# def click(event):
#     text = event.widget.cget("text")
#     if text == "=":
#         try:
#             result = eval(str(entry.get()))
#             entry.set(result)
#         except Exception as e:
#             entry.set("Error")
#     elif text == "C":
#         entry.set("")
#     else:
#         entry.set(entry.get() + text)

# root = tk.Tk()
# root.title("Calculator")

# entry = tk.StringVar()
# screen = tk.Entry(root, textvar=entry, font="lucida 20 bold")
# screen.pack(fill="x", ipadx=8, pady=10, padx=10)

# buttons = [
#     ["7","8","9","/"],
#     ["4","5","6","*"],
#     ["1","2","3","-"],
#     ["0",".","=","+"],
#     ["C"]
# ]

# for row in buttons:
#     f = tk.Frame(root)
#     f.pack()
#     for b in row:
#         button = tk.Button(f, text=b, padx=20, pady=20, font="lucida 15 bold")
#         button.pack(side="left", padx=5, pady=5)
#         button.bind("<Button-1>", click)

# root.mainloop()