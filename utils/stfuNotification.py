import tkinter as tk
from tkinter import messagebox

def ShowFuckNotification(title, message):
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror(title, message)

