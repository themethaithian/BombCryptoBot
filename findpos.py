import pyautogui
import time
# pyautogui.screenshot('Screenshot.png');
# pyautogui.displayMousePosition()
while True:
    workButton = pyautogui.locateCenterOnScreen('Work80.png', region = (0, 80, 850, 700), confidence = 0.95)
    error = pyautogui.locateCenterOnScreen('Error80.png', region = (0, 80, 850, 700), confidence = 0.7)
    if error != None:
        pyautogui.hotkey('command', 'shift', 'r')
        print('Error -- Reloading')
        isError = True
        time.sleep(5)
        break
    if workButton != None:
        pyautogui.click(workButton[0], workButton[1])
        time.sleep(1)
        continue
    break