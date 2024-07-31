import pyautogui
import time
from pynput import keyboard

 # コードを中止か判断するためのフラグ
start_flag = False
break_flag = False

# コードを中止する文字'q'　`s`が入力されたか判定する関数
def on_press(key):
    global break_flag
    try:
        if key.char == 'q':
            break_flag = True
            return False
    except AttributeError:
        pass

    global start_flag
    try:
        if key.char == 's':
            start_flag = True
            return False
    except AttributeError:
        pass

listener = keyboard.Listener(on_press=on_press)
listener.start()

while start_flag==False and break_flag == False:#q, sが押されたら開始
    print('roop')

break_flag = False
listener = keyboard.Listener(on_press=on_press)
listener.start()

#stime.sleep(5)

for i in range(30):  # ここが消し込みの回数
    if break_flag: # 中止するかどうか判定
        break

    pyautogui.doubleClick()
    pyautogui.press('f1')
    pyautogui.press('y')
    time.sleep(2)  # yを押した後に少しまつ

    print(i)
    