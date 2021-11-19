import pyautogui

while open('MouseUsed.txt', 'r') == 'T':
    continue
print('out')


# pyautogui.displayMousePosition()

# backButton = pyautogui.locateCenterOnScreen('Image/Back67.png', region = (0, 0, 750, 600), confidence = 0.7)
# if backButton != None:
#     pyautogui.click(backButton[0], backButton[1])

# X 0 Y 0 W 750 H 600
# X 0 Y 600 W 750 H 600
# X 750 Y 0 W 750 H 600
# X 750 Y 600 W 750 H 600