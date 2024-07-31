import pyautogui
import time
 
time.sleep(5)
 
 
for i in range(10):
    pyautogui.doubleClick()
    pyautogui.press('f1')
    pyautogui.press('y')
    time.sleep(2)
    pyautogui.press('f10')

    print(i)