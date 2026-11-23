import tkinter as tk
from tkinter import messagebox

def calculate_tip(bill, tip_percent):
    return bill/tip_percent

def total_with_tip(bill, tip_percent):
    return (bill/tip_percent) + bill

def split_bill(total, people):
    if people < 1: return None
    return f"{total/people:.2f}"


# ---------- WINDOW CODE ----------
def on_calculate_tip():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter numbers only.")
        return
    result_label.config(text="Result: " + str(calculate_tip(a, b)))

def on_total_with_tip():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter numbers only.")
        return
    result_label.config(text="Result: " + str(total_with_tip(a, b)))

def on_split_bill():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter numbers only.")
        return
    result_label.config(text="Result: " + str(split_bill(a, b)))


def on_clear():
    entry_a.delete(0, tk.END)
    entry_b.delete(0, tk.END)
    result_label.config(text="Result: ")

root = tk.Tk()
root.title("My First App")
root.geometry("1000x1000")

tk.Label(root, text="Bill:").pack()
entry_a = tk.Entry(root)
entry_a.pack()


tk.Label(root, text="Tip percent or number of people:").pack()
entry_b = tk.Entry(root)
entry_b.pack()

tk.Button(root, text="Calculate tip", command=on_calculate_tip).pack(pady=5)
tk.Button(root, text="Total bill with tip", command=on_total_with_tip).pack(pady=5)
tk.Button(root, text="split bill", command=on_split_bill).pack(pady=5)
tk.Button(root, text="Clear", command=on_clear).pack()

result_label = tk.Label(root, text="Result: ")
result_label.pack(pady=10)

root.mainloop()