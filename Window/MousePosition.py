from sys import breakpointhook
import pyautogui
import time

region = (0, 0, 550, 600)

workAllButton = pyautogui.locateCenterOnScreen('Image50/WorkAll50.png', region = region, confidence = 0.7)
pyautogui.click(workAllButton[0], workAllButton[1])
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