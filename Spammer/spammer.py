import time
import pyautogui

def send():
    time.sleep(10)

    text = open('connectionterminated.txt')
    for each_line in text:
        pyautogui.typewrite(each_line)
        time.sleep(3)
        pyautogui.press('enter')


send()