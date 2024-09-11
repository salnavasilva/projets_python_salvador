# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 15:07:46 2024

@author: USNA0501
"""
import tkinter as tk
from tkinter import ttk
import time
from datetime import datetime, timedelta

def get_seconds_until_6pm():
    now = datetime.replace(hour=9, minute=0, second=0, microsecond=0)
    
    six_pm = now.replace(hour=18, minute=0, second=0, microsecond=0)
    if now > six_pm:
        # If it's already past 6 PM, calculate time until 6 PM the next day
        six_pm += timedelta(days=1)
    return (six_pm - now).total_seconds()

def update_progress_bar():
    elapsed = time.time() - start_time
    progress = elapsed / total_seconds * 100
    progress_var.set(progress)
    if elapsed < total_seconds:
        root.after(1000, update_progress_bar)
    else:
        root.destroy()

def create_progress_bar_window():
    global root, progress_var
    root = tk.Tk()
    root.title("Progress to 6 PM")
    root.geometry("300x100")
    
    progress_var = tk.DoubleVar()
    progress_bar = ttk.Progressbar(root, variable=progress_var, maximum=100)
    progress_bar.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)
    
    root.after(0, update_progress_bar)
    root.attributes('-topmost', False)  # Keeps the window in the background
    root.mainloop()

if __name__ == "__main__":
    total_seconds = get_seconds_until_6pm()
    start_time = time.time()
    create_progress_bar_window()

#%%