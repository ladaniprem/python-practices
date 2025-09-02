# Tkinter is Python's standard GUI library for creating desktop applications
# - tk.Label(): Creates a label widget to display text
# - tk.Entry(): Creates a single-line text input field
# - tk.Button(): Creates a clickable button
# - pack(): Geometry manager that organizes widgets in blocks
# - pady: Adds vertical padding (space) around widgets
# - command: Links button click to a function
# - get(): Retrieves text from Entry widget
# - config(): Updates widget properties dynamically

import tkinter as tk

root = tk.Tk()
root.title("Text Box Example")
root.geometry("300x200")

def display_text():
    entered_text = entry.get()
    label.config(text=f"var entered: {entered_text}")

entry = tk.Entry(root, width=25)
entry.pack(pady=10)
# Add descriptive text label above entry
theory_label = tk.Label(root, text="Enter text below:", fg="black", font=("Arial", 10))
theory_label.pack(pady=5)

submit_button = tk.Button(root, text="submit", command=display_text)
submit_button.pack(pady=5)

label = tk.Label(root, text="", fg="blue", font=("Arial", 12))
label.pack(pady=10)

root.mainloop()