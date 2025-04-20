import tkinter as tk
from tkinter import font, messagebox, END

def start_timer():
    try:
        total_time = int(entry.get())
    except ValueError:
        label.config(text="Enter seconds!")
        return

    countdown(total_time)

def press_enter(event):
    start_timer()

def clear_entry():
    entry.delete(0, END)

def countdown(seconds):
    mins, secs = divmod(seconds, 60)
    time_format = f"{mins:02d}:{secs:02d}"
    label.config(text=time_format)
    if seconds > 0:
        root.after(1000, countdown, seconds - 1)
    else:
        clear_entry()
        messagebox.showinfo("Time's up!", "⏰ " \
                            "Time is up!")

# --- GUI Setup ---
root = tk.Tk()
root.title("⏳ Countdown Timer")
root.geometry("300x250")
root.resizable(False, False)
# root.configure(bg="#2c3e50")
root.configure(bg="#90EE90")

# --- Fonts ---
time_font = font.Font(family='Helvetica', 
                      size=48, 
                      weight='bold')
entry_font = font.Font(family='Helvetica', 
                       size=18)

# --- Timer Display ---
label = tk.Label(root, 
                 text="00:00", 
                 font=time_font, 
                 fg="#000000", 
                 bg="#90EE90")
label.pack(pady=30)

# --- Input Box ---
entry = tk.Entry(root, 
                 font=entry_font, 
                 justify='center', 
                 width=10, 
                 bg="#ffffff", 
                 bd=0)
entry.pack(ipady=5)
entry.focus()

# --- Start Button ---
start_button = tk.Button(
    root,
    text="Start",
    font=entry_font,
    bg="#27ae60",
    fg="white",
    activebackground="#2ecc71",
    relief="flat",
    command=start_timer
)
start_button.pack(pady=20, ipadx=10, ipady=5)

# --- Bind Enter Key to Start Timer ---
entry.bind('<Return>', press_enter)

root.mainloop()
