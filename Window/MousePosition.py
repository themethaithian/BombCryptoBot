from sys import breakpointhook
import pyautogui
import time

region = (0, 0, 550, 600)

error = None
errorIdle = None
error = pyautogui.locateCenterOnScreen('Image50/Error50.png', region = region, confidence = 0.7)
errorIdle = pyautogui.locateCenterOnScreen('Image50/ErrorIdle50.png', region = region, confidence = 0.7)

if error != None:
    pyautogui.moveTo(error[0], error[1])
    time.sleep(1)
    pyautogui.click(error[0], error[1])
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'r')
    isError = True
    print('Error -- Reloading')
    time.sleep(5)
if errorIdle != None:
    pyautogui.moveTo(errorIdle[0], errorIdle[1])
    time.sleep(1)
    pyautogui.click(errorIdle[0], errorIdle[1])
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'r')
    print('Idle -- Reloading')
    isError = True
    time.sleep(5)
backButton = pyautogui.locateCenterOnScreen('Image50/Back50.png', region = region, confidence = 0.7)
if backButton != None:
    pyautogui.moveTo(backButton[0], backButton[1])
    time.sleep(1)
    pyautogui.click(backButton[0], backButton[1])

# pyautogui.displayMousePosition()

# backButton = pyautogui.locateCenterOnScreen('Image/Back67.png', region = (0, 0, 750, 600), confidence = 0.7)
# if backButton != None:
#     pyautogui.click(backButton[0], backButton[1])

# X 0 Y 0 W 750 H 600
# X 0 Y 600 W 750 H 600
# X 750 Y 0 W 750 H 600
# X 750 Y 600 W 750 H 600

# (0, 0, 550, 600)
# (0, 450, 550, 600)
# (550, 0, 550, 600)
# (550, 450, 550, 600)
# (1100, 0, 550, 600)
# (1100, 450, 550, 600)

# (0, 0, 550, 600)
# (550, 0, 550, 600)
# (1100, 0, 550, 600)
# (0, 375, 550, 600)
# (550, 375, 550, 600)
# (1100, 375, 550, 600)
# (0, 700, 550, 350)
# (550, 700, 550, 350)
# (1100, 700, 550, 350)