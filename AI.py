import time
import pyautogui

def simulate_typing(text,delay=0.1):
    for char in text:
        pyautogui.typewrite(char)
        time.sleep(delay)
  
simulate_typing("Hlo this is ishant,  i want to say someting",delay=0.1)