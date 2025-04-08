import pyautogui
import keyboard
import time

print("Auto Clicker Mouse and Keyboard Ready")
print("Press 'S' to start and 'q' to stop")

custom_position = None

print(pyautogui.position())

running = False

while True:
    if not running and keyboard.is_pressed('s'):
        print("Ready in 3 second")
        time.sleep(3)  
        running = True
        print("Started!")

    if running:
        if keyboard.is_pressed('q'):
            print("Stopped")
            break
        if custom_position:
            pyautogui.click(custom_position)
        else:
            pyautogui.click(1023, 920)
            time.sleep(10)
            pyautogui.click(1023, 520)
            time.sleep(2)

  