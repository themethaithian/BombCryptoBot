from PIL.Image import new
import pyautogui
import pyscreeze
import cv2
import time
import sys

try:
    while True:
        time.sleep(5)
        while True:
            connectButton = pyautogui.locateCenterOnScreen('ConnectButton80.png', region = (0, 80, 850, 700), confidence = 0.7)
            if connectButton == None:
                continue
            pyautogui.click(connectButton[0], connectButton[1])
            print('Connecting Wallet...')
            break
        time.sleep(5)

        mmButton = pyautogui.locateCenterOnScreen('MetaMask80.png', region = (0, 80, 850, 700), confidence = 0.7)
        if mmButton == None:
            pyautogui.hotkey('command', 'shift', 'r')
            print('MetaMask Not Found -- Reloading')
            continue
        pyautogui.click(mmButton[0], mmButton[1])
        print('Signing MetaMask...')
        time.sleep(5)

        while True:
            signButton = pyautogui.locateCenterOnScreen('Sign80.png', region = (0, 80, 850, 700), confidence = 0.7)
            if signButton == None:
                pyautogui.hotkey('command', 'shift', 'r')
                print('MetaMask Not Found -- Reloading')
                continue
            pyautogui.click(signButton[0], signButton[1])
            print('Loading...')
            break
        time.sleep(15)

        while True:
            connectButton = None
            mmButton = None
            signButton = None
            selectHero = None
            homeButton = None
            workButton = None
            closeHero = None
            hunt = None
            newMap = None
            error = None
            backButton = None
            timeResetCount = 0
            timeRestartCount = 0
            timeCheck = 0
            isError = False

            selectHero = pyautogui.locateCenterOnScreen('Hero80.png', region = (0, 80, 850, 700), confidence = 0.7)
            error = pyautogui.locateCenterOnScreen('Error80.png', region = (0, 80, 850, 700), confidence = 0.7)
            if error != None:
                pyautogui.click(error[0], error[1])
                time.sleep(0.5)
                pyautogui.hotkey('command', 'shift', 'r')
                isError = True
                print('Error -- Reloading')
                time.sleep(5)
                break
            if selectHero == None :
                pyautogui.hotkey('command', 'r')
                print('Cant Load Game -- Reload')
                break
            pyautogui.click(selectHero[0], selectHero[1])
            print('Open Heroes Screen...')
            time.sleep(1)

            while isError == False:
                homeButton = pyautogui.locateCenterOnScreen('Home80.png', region = (0, 80, 850, 700), confidence = 0.7)
                error = pyautogui.locateCenterOnScreen('Error80.png', region = (0, 80, 850, 700), confidence = 0.7)
                if error != None:
                    pyautogui.click(error[0], error[1])
                    time.sleep(0.5)
                    pyautogui.hotkey('command', 'shift', 'r')
                    print('Error -- Reloading')
                    isError = True
                    time.sleep(5)
                    continue
                if homeButton == None:
                    continue
                pyautogui.moveTo(homeButton[0], homeButton[1])
                print('Scrolling Down...')
                for s in range(45):
                    pyautogui.scroll(-1)
                    time.sleep(0.05)
                break
            time.sleep(1)

            if isError == False:
                print('Bring Hero To Work...')
                while True:
                    workButton = pyautogui.locateCenterOnScreen('Work80.png', region = (0, 80, 850, 700), confidence = 0.95)
                    error = pyautogui.locateCenterOnScreen('Error80.png', region = (0, 80, 850, 700), confidence = 0.7)
                    if error != None:
                        pyautogui.click(error[0], error[1])
                        time.sleep(0.5)
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

            while isError == False:
                closeHero = pyautogui.locateCenterOnScreen('CloseHero80.png', region = (0, 80, 850, 700), confidence = 0.7)
                error = pyautogui.locateCenterOnScreen('Error80.png', region = (0, 80, 850, 700), confidence = 0.7)
                if error != None:
                    pyautogui.click(error[0], error[1])
                    time.sleep(0.5)
                    pyautogui.hotkey('command', 'shift', 'r')
                    isError = True
                    print('Error -- Reloading')
                    time.sleep(5)
                    break
                if closeHero == None:
                    continue
                pyautogui.click(closeHero[0], closeHero[1])
                break
                
            while isError == False:
                hunt = pyautogui.locateCenterOnScreen('Hunt80.png', region = (0, 80, 850, 700), confidence = 0.7)
                error = pyautogui.locateCenterOnScreen('Error80.png', region = (0, 80, 850, 700), confidence = 0.7)
                if error != None:
                    pyautogui.click(error[0], error[1])
                    time.sleep(0.5)
                    pyautogui.hotkey('command', 'shift', 'r')
                    isError = True
                    print('Error -- Reloading')
                    time.sleep(5)
                    continue
                if(hunt == None):
                    continue
                pyautogui.click(hunt[0], hunt[1])
                print('Start...')
                break

            while isError == False:
                timeResetCount += 60
                timeRestartCount += 60
                timeCheck += 60
                
                if timeCheck >= 120:
                    newMap = pyautogui.locateCenterOnScreen('NewMap80.png', region = (0, 80, 850, 700), confidence = 0.7)
                    error = pyautogui.locateCenterOnScreen('Error80.png', region = (0, 80, 850, 700), confidence = 0.7)
                    if error != None:
                        pyautogui.click(error[0], error[1])
                        time.sleep(0.5)
                        pyautogui.hotkey('command', 'shift', 'r')
                        isError = True
                        print('Error -- Reloading')
                        time.sleep(5)
                        break
                    elif newMap != None:
                        pyautogui.click(newMap[0], newMap[1])
                        time.sleep(0.5)
                        pyautogui.click(newMap[0], newMap[1])
                        print('Change Map...')
                    timeCheck = 0

                if timeResetCount >=300:
                    backButton = pyautogui.locateCenterOnScreen('Back80.png', region = (0, 80, 850, 700), confidence = 0.7)
                    pyautogui.click(backButton[0], backButton[1])
                    time.sleep(0.5)
                    pyautogui.click(backButton[0], backButton[1])
                    print('Reseting Position...')
                    time.sleep(5)
                    pyautogui.click(hunt[0], hunt[1])
                    timeResetCount = 0
                elif timeRestartCount >= 3600:
                    backButton = pyautogui.locateCenterOnScreen('Back80.png', region = (0, 80, 850, 700), confidence = 0.7)
                    pyautogui.click(backButton[0], backButton[1])
                    time.sleep(0.5)
                    pyautogui.click(backButton[0], backButton[1])
                    time.sleep(5)
                    print('Restarting Flow...')
                    break

                time.sleep(60)
            
            if isError == True:
                break
            else:
                continue

        continue
except KeyboardInterrupt:
    print('\n')