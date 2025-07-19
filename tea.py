import pyautogui
import keyboard
import time
import threading



print(pyautogui.position())

print("Auto Clicker Mouse and Keyboard Ready")
print("Press 'S' to start and 'q' to stop")

position= None

running = False
stoped = False

def stop():
    global stoped
    while not stoped :
        if keyboard.is_pressed('q'):
            print("Stopped")
            stoped = True
            break

def autoclicker():
    global running, stoped
    print("Ready in 3 second")
    time.sleep(3)
    running = True
    print("started")
    while not stoped:
        pyautogui.click(1613, 874)
        time.sleep(2)
        pyautogui.click(1505, 510)
        time.sleep(1)
        pyautogui.click(1529, 575)
        time.sleep(1)
        pyautogui.click(1731, 880)
        time.sleep(8)
        pyautogui.click(1795, 708)
        time.sleep(15)
        pyautogui.click(1613, 874)
        time.sleep(1)

keyboard.wait('s')

stop_thread = threading.Thread(target=stop)
stop_thread.start()

autoclicker()