import tkinter as tk

root = tk.Tk()
root.title("Text Box Example")
root.geometry("300x200")

def display_text():
    entered_text = entry.get()
    label.config(text=f"var entered: {entered_text}")

entry = tk.Entry(root, width=25)
entry.pack(pady=10)

submit_button = tk.Button(root, text="submit", command=display_text)
submit_button.pack(pady=5)

label = tk.Label(root, text="", fg="blue", font=("Arial", 12))
label.pack(pady=10)

root.mainloop()