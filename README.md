
# tinytask-mac

This Python script utilizes the pyautogui and keyboard libraries to facilitate automation. The program records mouse events while in automation mode and stops when the specified key ("i") is pressed. It serves as a foundation for creating custom automation scripts.

## Code

```
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
```

## Instructions:

Import the required libraries by running pip install pyautogui keyboard in your terminal.
Copy and paste the provided code into your Python environment or IDE.
Execute the script.
Press the "i" key to toggle automation on/off.
Customize the script to include specific automation tasks within the toggle_automation function.
Ensure your environment supports the use of pyautogui and keyboard libraries.
Explore pyautogui documentation (https://pyautogui.readthedocs.io/) for additional features and customization options.
Feel free to reach out if you have any questions or need further assistance.
