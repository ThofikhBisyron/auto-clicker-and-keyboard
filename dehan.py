import pyautogui
import keyboard
import time
import threading

print("Auto Clicker Mouse and Keyboard Ready")
print("Press 'S' to start and 'q' to stop")

custom_position = None

print(pyautogui.position())

running = False
stopped = False

def stop():
    global stopped
    while not stopped :
        if keyboard.is_pressed('q'):
            print("Stopped")
            stopped = True
            break



def autoclick():
    global running, stopped
    print("Ready in 3 second")
    time.sleep(3)  
    running = True
    print("Started!")

    while not stopped:
            pyautogui.click(971, 915)
            time.sleep(10)
            pyautogui.click(1785, 704)
            time.sleep(2)

print("Auto Clicker Mouse And Keyboard Ready")
print("Press 'S' to start and press 'q' to stop")

keyboard.wait('s')

stop_thread = threading.Thread(target=stop)
stop_thread.start()

autoclick()
print(pyautogui.position())