import pyautogui
import time
import random

def minimize_maximize():

    # Minimize Teams
    pyautogui.hotkey('winleft', 'down')
    time.sleep(3) 
    
    # Maximize Teams
    pyautogui.hotkey('winleft', 'up')
    time.sleep(3)  
    
def move_cursor():
    # Get the screen size
    screen_width, screen_height = pyautogui.size()

    # Move the cursor to a random position within the screen
    pyautogui.moveTo(
        x=random.randint(0, screen_width),
        y=random.randint(0, screen_height),
        duration=0.25  # You can adjust the duration of the movement
    )

if __name__ == "__main__":
    while True:
        minimize_maximize()
        move_cursor()
        time.sleep(5)  