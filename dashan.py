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
            time.sleep(1800)
            keyboard.press_and_release('f5')
            time.sleep(10) 
            pyautogui.click(778, 791)
            time.sleep(7)
            pyautogui.click(972, 635)
            time.sleep(5)
            pyautogui.click(821, 920)
   


print("Auto Clicker Mouse And Keyboard Ready")
print("Press 'S' to start and press 'q' to stop")

keyboard.wait('s')

stop_thread = threading.Thread(target=stop)
stop_thread.start()

autoclick()
print(pyautogui.position())