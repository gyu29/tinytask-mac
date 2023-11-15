# Import necessary libraries
import pyautogui
import keyboard
import time

# Variables for automation state and recorded events
automation_running = False
events = []

# Function to start and stop automation
def toggle_automation():
    global automation_running
    if not automation_running:
        automation_running = True
        print("Automation started.")
        pyautogui.PAUSE = 0.01  # Set the desired pause between events
        while automation_running:
            events.append((time.time(), pyautogui.position()))
            time.sleep(0.01)
            if keyboard.is_pressed("i"):
                toggle_automation()
                break
    else:
        automation_running = False
        print("Automation stopped.")

# Example usage
if __name__ == "__main__":
    while True:
        if keyboard.is_pressed("i"):
            toggle_automation()
            time.sleep(0.1)  # Avoid capturing the initial "i" press
