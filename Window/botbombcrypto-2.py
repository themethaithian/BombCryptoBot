import pyautogui
import time

try:
    while True:
        time.sleep(15)
        f = open('MouseUsed.txt', 'r')
        while f.read() == 'T':
            continue
        f.close()
        f = open('MouseUsed.txt', 'w')
        f.write('T')
        f.close()
        while True:
            connectButton = pyautogui.locateCenterOnScreen('Image/Connect67.png', region = (0,  550, 750, 600), confidence = 0.7)
            if connectButton == None:
                pyautogui.hotkey('ctrl', 'shift', 'r')
                print('Connect Not Found -- Reloading')
                time.sleep(5)
                continue
            pyautogui.moveTo(connectButton[0], connectButton[1])
            pyautogui.click(connectButton[0], connectButton[1])
            print('Connecting Wallet...')
            break
        time.sleep(5)

        mmButton = pyautogui.locateCenterOnScreen('Image/Meta67.png', region = (0,  550, 750, 600), confidence = 0.7)
        if mmButton == None:
            pyautogui.hotkey('ctrl', 'shift', 'r')
            print('MetaMask Not Found -- Reloading')
            continue
        pyautogui.moveTo(mmButton[0], mmButton[1])
        pyautogui.click(mmButton[0], mmButton[1])
        print('Signing MetaMask...')
        time.sleep(5)

        while True:
            signButton = pyautogui.locateCenterOnScreen('Image/Sign67.png', region = (0,  550, 750, 600), confidence = 0.7)
            if signButton == None:
                pyautogui.hotkey('ctrl', 'shift', 'r')
                print('MetaMask Not Found -- Reloading')
                continue
            pyautogui.moveTo(signButton[0], signButton[1])
            pyautogui.click(signButton[0], signButton[1])
            print('Loading...')
            break
        time.sleep(15)
        f = open('MouseUsed.txt', 'w')
        f.write('F')
        f.close()

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

            selectHero = pyautogui.locateCenterOnScreen('Image/Hero67.png', region = (0,  550, 750, 600), confidence = 0.7)
            error = pyautogui.locateCenterOnScreen('Image/Error67.png', region = (0,  550, 750, 600), confidence = 0.7)
            
            f = open('MouseUsed.txt', 'r')
            while f.read() == 'T':
                continue
            f.close()
            f = open('MouseUsed.txt', 'w')
            f.write('T')
            f.close()

            if error != None:
                pyautogui.click(error[0], error[1])
                time.sleep(0.5)
                pyautogui.hotkey('ctrl', 'shift', 'r')
                isError = True
                print('Error -- Reloading')
                time.sleep(5)
                f = open('MouseUsed.txt', 'w')
                f.write('F')
                f.close()
                break
            if selectHero == None :
                pyautogui.hotkey('ctrl', 'shift,' 'r')
                print('Cant Load Game -- Reload')
                f = open('MouseUsed.txt', 'w')
                f.write('F')
                f.close()
                break
            pyautogui.moveTo(selectHero[0], selectHero[1])
            time.sleep(1)
            pyautogui.click(selectHero[0], selectHero[1])
            time.sleep(1)
            pyautogui.click(selectHero[0], selectHero[1])
            print('Open Heroes Screen...')
            f = open('MouseUsed.txt', 'w')
            f.write('F')
            f.close()
            time.sleep(1)

            while isError == False:
                homeButton = pyautogui.locateCenterOnScreen('Image/Home67.png', region = (0,  550, 750, 600), confidence = 0.7)
                error = pyautogui.locateCenterOnScreen('Image/Error67.png', region = (0,  550, 750, 600), confidence = 0.7)
                f = open('MouseUsed.txt', 'r')
                while f.read() == 'T':
                    continue
                f.close()
                f = open('MouseUsed.txt', 'w')
                f.write('T')
                f.close()
                if error != None:
                    pyautogui.click(error[0], error[1])
                    time.sleep(0.5)
                    pyautogui.hotkey('ctrl', 'shift', 'r')
                    print('Error -- Reloading')
                    isError = True
                    time.sleep(5)
                    f = open('MouseUsed.txt', 'w')
                    f.write('F')
                    f.close()
                    continue
                if homeButton == None:
                    continue
                pyautogui.moveTo(homeButton[0], homeButton[1])
                print('Scrolling Down...')
                for s in range(60):
                    pyautogui.moveTo(homeButton[0], homeButton[1])
                    pyautogui.click(homeButton[0], homeButton[1])
                    pyautogui.scroll(-1)
                    time.sleep(0.05)
                break
            f = open('MouseUsed.txt', 'w')
            f.write('F')
            f.close()
            time.sleep(1)

            if isError == False:
                print('Bring Hero To Work...')
                f = open('MouseUsed.txt', 'r')
                while f.read() == 'T':
                    continue
                f.close()
                f = open('MouseUsed.txt', 'w')
                f.write('T')
                f.close()
                while True:
                    workButton = pyautogui.locateCenterOnScreen('Image/Work67.png', region = (0,  550, 750, 600), confidence = 0.95)
                    error = pyautogui.locateCenterOnScreen('Image/Error67.png', region = (0,  550, 750, 600), confidence = 0.7)
                    if error != None:
                        pyautogui.click(error[0], error[1])
                        time.sleep(0.5)
                        pyautogui.hotkey('ctrl', 'shift', 'r')
                        print('Error -- Reloading')
                        isError = True
                        time.sleep(5)
                        f = open('MouseUsed.txt', 'w')
                        f.write('F')
                        f.close()
                        break
                    if workButton != None:
                        pyautogui.click(workButton[0], workButton[1])
                        time.sleep(1)
                        continue
                    f = open('MouseUsed.txt', 'w')
                    f.write('F')
                    f.close()
                    break

            while isError == False:
                closeHero = pyautogui.locateCenterOnScreen('Image/CloseHero67.png', region = (0,  550, 750, 600), confidence = 0.7)
                error = pyautogui.locateCenterOnScreen('Image/Error67.png', region = (0,  550, 750, 600), confidence = 0.7)
                f = open('MouseUsed.txt', 'r')
                while f.read() == 'T':
                    continue
                f.close()
                f = open('MouseUsed.txt', 'w')
                f.write('T')
                f.close()
                if error != None:
                    pyautogui.click(error[0], error[1])
                    time.sleep(0.5)
                    pyautogui.hotkey('ctrl', 'shift', 'r')
                    isError = True
                    print('Error -- Reloading')
                    time.sleep(5)
                    f = open('MouseUsed.txt', 'w')
                    f.write('F')
                    f.close()
                    break
                if closeHero == None:
                    continue
                pyautogui.moveTo(closeHero[0], closeHero[1])
                time.sleep(1)
                pyautogui.click(closeHero[0], closeHero[1])
                time.sleep(0.5)
                pyautogui.click(closeHero[0], closeHero[1])
                f = open('MouseUsed.txt', 'w')
                f.write('F')
                f.close()
                break
                
            while isError == False:
                hunt = pyautogui.locateCenterOnScreen('Image/Hunt67.png', region = (0,  550, 750, 600), confidence = 0.7)
                error = pyautogui.locateCenterOnScreen('Image/Error67.png', region = (0,  550, 750, 600), confidence = 0.7)
                f = open('MouseUsed.txt', 'r')
                while f.read() == 'T':
                    continue
                f.close()
                f = open('MouseUsed.txt', 'w')
                f.write('T')
                f.close()
                if error != None:
                    pyautogui.click(error[0], error[1])
                    time.sleep(0.5)
                    pyautogui.hotkey('ctrl', 'shift', 'r')
                    isError = True
                    print('Error -- Reloading')
                    time.sleep(5)
                    f = open('MouseUsed.txt', 'w')
                    f.write('F')
                    f.close()
                    continue
                if(hunt == None):
                    continue
                pyautogui.moveTo(hunt[0], hunt[1])
                time.sleep(1)
                pyautogui.click(hunt[0], hunt[1])
                time.sleep(0.5)
                pyautogui.click(hunt[0], hunt[1])
                print('Start...')
                f = open('MouseUsed.txt', 'w')
                f.write('F')
                f.close()
                break

            while isError == False:
                timeResetCount += 60
                timeRestartCount += 60
                timeCheck += 60
                
                if timeCheck >= 120:
                    newMap = pyautogui.locateCenterOnScreen('Image/NewMap67.png', region = (0,  550, 750, 600), confidence = 0.7)
                    error = pyautogui.locateCenterOnScreen('Image/Error67.png', region = (0,  550, 750, 600), confidence = 0.7)
                    f = open('MouseUsed.txt', 'r')
                    while f.read() == 'T':
                        continue
                    f.close()
                    f = open('MouseUsed.txt', 'w')
                    f.write('T')
                    f.close()
                    if error != None:
                        pyautogui.click(error[0], error[1])
                        time.sleep(1)
                        pyautogui.hotkey('ctrl', 'shift', 'r')
                        isError = True
                        print('Error -- Reloading')
                        time.sleep(5)
                        f = open('MouseUsed.txt', 'w')
                        f.write('F')
                        f.close()
                        break
                    if newMap != None:
                        pyautogui.moveTo(newMap[0], newMap[1])
                        time.sleep(1)
                        pyautogui.click(newMap[0], newMap[1])
                        time.sleep(1)
                        pyautogui.click(newMap[0], newMap[1])
                        time.sleep(1)
                        pyautogui.click(newMap[0], newMap[1])
                        time.sleep(1)
                        pyautogui.click(newMap[0], newMap[1])
                        print('Change Map...')
                        f = open('MouseUsed.txt', 'w')
                        f.write('F')
                        f.close()
                    timeCheck = 0

                if timeResetCount >= 180:
                    f = open('MouseUsed.txt', 'r')
                    while f.read() == 'T':
                        continue
                    f.close()
                    f = open('MouseUsed.txt', 'w')
                    f.write('T')
                    f.close()
                    if backButton == None:
                        backButton = pyautogui.locateCenterOnScreen('Image/Back67.png', region = (0,  550, 750, 600), confidence = 0.7)
                        pyautogui.moveTo(backButton[0], backButton[1])
                        time.sleep(1)
                        pyautogui.click(backButton[0], backButton[1])
                        time.sleep(1)
                        pyautogui.click(backButton[0], backButton[1])
                    elif backButton != None:
                        pyautogui.moveTo(backButton[0], backButton[1])
                        time.sleep(1)
                        pyautogui.click(backButton[0], backButton[1])
                        time.sleep(1)
                        pyautogui.click(backButton[0], backButton[1])
                    print('Reseting Position...')
                    time.sleep(2)
                    pyautogui.moveTo(hunt[0], hunt[1])
                    time.sleep(1)
                    pyautogui.click(hunt[0], hunt[1])
                    time.sleep(1)
                    pyautogui.click(hunt[0], hunt[1])
                    timeResetCount = 0
                    f = open('MouseUsed.txt', 'w')
                    f.write('F')
                    f.close()
                elif timeRestartCount >= 3000:
                    f = open('MouseUsed.txt', 'r')
                    while f.read() == 'T':
                        continue
                    f.close()
                    f = open('MouseUsed.txt', 'w')
                    f.write('T')
                    f.close()
                    if backButton != None:
                        pyautogui.moveTo(backButton[0], backButton[1])
                        time.sleep(1)
                        pyautogui.click(backButton[0], backButton[1])
                        time.sleep(0.5)
                        pyautogui.click(backButton[0], backButton[1])
                    time.sleep(0.5)
                    pyautogui.click(backButton[0], backButton[1])
                    time.sleep(5)
                    f = open('MouseUsed.txt', 'w')
                    f.write('F')
                    f.close()
                    print('Restarting Flow...')
                    break

                time.sleep(60)
            
            if isError == True:
                f = open('MouseUsed.txt', 'w')
                f.write('F')
                f.close()
                break
            else:
                f = open('MouseUsed.txt', 'w')
                f.write('F')
                f.close()
                continue

        continue
except KeyboardInterrupt:
    print('\n')