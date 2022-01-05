import pyautogui
import time

region = (550, 0, 550, 600)
center = (region[0] + region[2] / 2, region[1] + 375 / 2 )
waitTime = 2.2
queueNum = '2'
nextQueue = '3'
newMapTimer = 120
RepositionTimer = 180
ResetTimer = 3000

try:
    while True:
        isError = False
        time.sleep(15)

        while open('Queue.txt', 'r').read() != queueNum:
            time.sleep(1.7)
            continue

        print("In Loop")

        while True:
            time.sleep(15)
            connectButton = pyautogui.locateCenterOnScreen('Image50/Connect50.png', region = region, confidence = 0.7)
            if connectButton == None:
                pyautogui.moveTo(center)
                time.sleep(1)
                pyautogui.click(center)
                time.sleep(1)
                pyautogui.click(center)
                time.sleep(1)
                pyautogui.hotkey('ctrl', 'shift', 'r')
                print('Connect Not Found -- Reloading')
                continue
            pyautogui.moveTo(connectButton[0], connectButton[1])
            pyautogui.click(connectButton[0], connectButton[1])
            time.sleep(1)
            pyautogui.click(connectButton[0], connectButton[1])
            time.sleep(1)
            print('Connecting Wallet...')
            break
        time.sleep(10)

        while True:
            signButton = pyautogui.locateCenterOnScreen('Image50/Sign50.png', region = region, confidence = 0.7)
            if signButton == None:
                pyautogui.moveTo(center)
                time.sleep(1)
                pyautogui.click(center)
                time.sleep(1)
                pyautogui.hotkey('ctrl', 'shift', 'r')
                print('MetaMask Not Found -- Reloading')
                break
            pyautogui.moveTo(signButton[0], signButton[1])
            pyautogui.click(signButton[0], signButton[1])
            time.sleep(1)
            pyautogui.click(signButton[0], signButton[1])
            time.sleep(1)
            print('Loading...')
            break
        open('Queue.txt', 'w').write(nextQueue)
        time.sleep(15)

        while isError == False:
            connectButton = None
            mmButton = None
            signButton = None
            selectHero = None
            homeButton = None
            workButton = None
            closeHero = None
            error = None
            errorIdle = None
            backButton = None
            timeResetCount = 0
            timeRestartCount = 0
            timeCheck = 0
            isError = False

            while open('Queue.txt', 'r').read() != queueNum:
                time.sleep(1.7)
                continue

            selectHero = pyautogui.locateCenterOnScreen('Image50/Hero50.png', region = region, confidence = 0.7)
            error = pyautogui.locateCenterOnScreen('Image50/Error50.png', region = region, confidence = 0.7)
            errorIdle = pyautogui.locateCenterOnScreen('Image50/ErrorIdle50.png', region = region, confidence = 0.7)

            if error != None:
                pyautogui.moveTo(error[0], error[1])
                time.sleep(1)
                pyautogui.click(error[0], error[1])
                time.sleep(1)
                pyautogui.hotkey('ctrl', 'r')
                print('Error -- Reloading')
                isError = True
                time.sleep(5)
                open('Queue.txt', 'w').write(nextQueue)
                break
            if errorIdle != None:
                pyautogui.moveTo(errorIdle[0], errorIdle[1])
                time.sleep(1)
                pyautogui.click(errorIdle[0], errorIdle[1])
                time.sleep(1)
                pyautogui.hotkey('ctrl', 'r')
                print('Idle -- Reloading')
                isError = True
                time.sleep(5)
                open('Queue.txt', 'w').write(nextQueue)
                break
            if selectHero == None :
                pyautogui.moveTo(center)
                time.sleep(0.5)
                pyautogui.click(center)
                time.sleep(0.5)
                pyautogui.hotkey('ctrl', 'shift,' 'r')
                print('Cant Load Game -- Reload')
                open('Queue.txt', 'w').write(nextQueue)
                break
            pyautogui.moveTo(selectHero[0], selectHero[1])
            time.sleep(1)
            pyautogui.click(selectHero[0], selectHero[1])
            time.sleep(1)
            pyautogui.click(selectHero[0], selectHero[1])
            print('Open Heroes Screen...')
            time.sleep(1)

            while isError == False:
                homeButton = pyautogui.locateCenterOnScreen('Image50/Home50.png', region = region, confidence = 0.7)
                error = pyautogui.locateCenterOnScreen('Image50/Error50.png', region = region, confidence = 0.7)
                errorIdle = pyautogui.locateCenterOnScreen('Image50/ErrorIdle50.png', region = region, confidence = 0.7)
                
                if error != None:
                    pyautogui.moveTo(error[0], error[1])
                    time.sleep(1)
                    pyautogui.click(error[0], error[1])
                    time.sleep(1)
                    pyautogui.hotkey('ctrl', 'r')
                    print('Error -- Reloading')
                    isError = True
                    time.sleep(5)
                    open('Queue.txt', 'w').write(nextQueue)
                    break
                if errorIdle != None:
                    pyautogui.moveTo(errorIdle[0], errorIdle[1])
                    time.sleep(1)
                    pyautogui.click(errorIdle[0], errorIdle[1])
                    time.sleep(1)
                    pyautogui.hotkey('ctrl', 'r')
                    print('Idle -- Reloading')
                    isError = True
                    time.sleep(5)
                    open('Queue.txt', 'w').write(nextQueue)
                    break
                if homeButton == None:
                    continue
                pyautogui.moveTo(homeButton[0], homeButton[1])
                print('Scrolling Down...')
                for s in range(60):
                    pyautogui.moveTo(homeButton[0], homeButton[1])
                    pyautogui.click(homeButton[0], homeButton[1])
                    pyautogui.scroll(-1)
                    time.sleep(0.05)
                time.sleep(1)
                break
            heroCount = 0
            if isError == False:
                error = None
                print('Bring Hero To Work...')
                while True:
                    workButton = pyautogui.locateCenterOnScreen('Image50/Work50.png', region = region, confidence = 0.95)
                    error = pyautogui.locateCenterOnScreen('Image50/Error50.png', region = region, confidence = 0.7)
                    errorIdle = pyautogui.locateCenterOnScreen('Image50/ErrorIdle50.png', region = region, confidence = 0.7)
                    workError = pyautogui.locateCenterOnScreen('Image50/WorkError50.png', region = region, confidence = 0.7)
                    if error != None:
                        pyautogui.moveTo(error[0], error[1])
                        time.sleep(1)
                        pyautogui.click(error[0], error[1])
                        time.sleep(1)
                        pyautogui.hotkey('ctrl', 'r')
                        print('Error -- Reloading')
                        isError = True
                        time.sleep(5)
                        open('Queue.txt', 'w').write(nextQueue)
                        break
                    if errorIdle != None:
                        pyautogui.moveTo(errorIdle[0], errorIdle[1])
                        time.sleep(1)
                        pyautogui.click(errorIdle[0], errorIdle[1])
                        time.sleep(1)
                        pyautogui.hotkey('ctrl', 'r')
                        print('Idle -- Reloading')
                        isError = True
                        time.sleep(5)
                        open('Queue.txt', 'w').write(nextQueue)
                        break
                    if workError != None:
                        pyautogui.moveTo(workError[0], workError[1])
                        time.sleep(1)
                        pyautogui.click(workError[0], workError[1])
                        time.sleep(1)
                        pyautogui.hotkey('ctrl', 'shift', 'r')
                        print('Error -- Reloading')
                        isError = True
                        time.sleep(5)
                        open('Queue.txt', 'w').write(nextQueue)
                        break
                    if workButton != None:
                        pyautogui.click(workButton[0], workButton[1])
                        heroCount += 1
                        print('Hero: ', heroCount)
                        time.sleep(1)
                        continue
                    break

            while isError == False:
                closeHero = pyautogui.locateCenterOnScreen('Image50/CloseHero50.png', region = region, confidence = 0.7)
                error = pyautogui.locateCenterOnScreen('Image50/Error50.png', region = region, confidence = 0.7)
                errorIdle = pyautogui.locateCenterOnScreen('Image50/ErrorIdle50.png', region = region, confidence = 0.7)
                
                if error != None:
                    pyautogui.moveTo(error[0], error[1])
                    time.sleep(1)
                    pyautogui.click(error[0], error[1])
                    time.sleep(1)
                    pyautogui.hotkey('ctrl', 'shift', 'r')
                    isError = True
                    print('Error -- Reloading')
                    time.sleep(5)
                    open('Queue.txt', 'w').write(nextQueue)
                    break
                if errorIdle != None:
                    pyautogui.moveTo(errorIdle[0], errorIdle[1])
                    time.sleep(1)
                    pyautogui.click(errorIdle[0], errorIdle[1])
                    time.sleep(1)
                    pyautogui.hotkey('ctrl', 'r')
                    print('Idle -- Reloading')
                    isError = True
                    time.sleep(5)
                    open('Queue.txt', 'w').write(nextQueue)
                    break
                if closeHero == None:
                    continue
                pyautogui.moveTo(closeHero[0], closeHero[1])
                time.sleep(1)
                pyautogui.click(closeHero[0], closeHero[1])
                time.sleep(0.5)
                pyautogui.click(closeHero[0], closeHero[1])
                break
                
            while isError == False:
                error = None
                hunt = pyautogui.locateCenterOnScreen('Image50/Hunt50.png', region = region, confidence = 0.7)
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
                    open('Queue.txt', 'w').write(nextQueue)
                    continue
                if errorIdle != None:
                    pyautogui.moveTo(errorIdle[0], errorIdle[1])
                    time.sleep(1)
                    pyautogui.click(errorIdle[0], errorIdle[1])
                    time.sleep(1)
                    pyautogui.hotkey('ctrl', 'r')
                    print('Idle -- Reloading')
                    isError = True
                    time.sleep(5)
                    open('Queue.txt', 'w').write(nextQueue)
                    break
                if(hunt == None):
                    continue
                pyautogui.moveTo(hunt[0], hunt[1])
                time.sleep(1)
                pyautogui.click(hunt[0], hunt[1])
                time.sleep(0.5)
                pyautogui.click(hunt[0], hunt[1])
                print('Start...')
                open('Queue.txt', 'w').write(nextQueue)
                break
            
            resetCount = 0

            while isError == False:
                timeResetCount += 60
                timeRestartCount += 60
                timeCheck += 60

                while open('Queue.txt', 'r').read() != queueNum:
                    time.sleep(1.7)
                    continue

                error = None
                errorIdle = None
                error = pyautogui.locateCenterOnScreen('Image50/Error50.png', region = region, confidence = 0.7)
                errorIdle = pyautogui.locateCenterOnScreen('Image50/ErrorIdle50.png', region = region, confidence = 0.7)
                if timeCheck >= newMapTimer:
                    newMap = pyautogui.locateCenterOnScreen('Image50/NewMap50.png', region = region, confidence = 0.7)
                    if error != None:
                        pyautogui.moveTo(error[0], error[1])
                        time.sleep(1)
                        pyautogui.click(error[0], error[1])
                        time.sleep(1)
                        pyautogui.hotkey('ctrl', 'r')
                        isError = True
                        print('Error -- Reloading')
                        time.sleep(5)
                        break
                    if errorIdle != None:
                        pyautogui.moveTo(errorIdle[0], errorIdle[1])
                        time.sleep(1)
                        pyautogui.click(errorIdle[0], errorIdle[1])
                        time.sleep(1)
                        pyautogui.hotkey('ctrl', 'r')
                        print('Idle -- Reloading')
                        isError = True
                        time.sleep(5)
                        break
                    if newMap != None:
                        pyautogui.moveTo(newMap[0], newMap[1])
                        time.sleep(1)
                        pyautogui.click(newMap[0], newMap[1])
                        print('Change Map...')
                        open('Queue.txt', 'w').write(nextQueue)
                    
                    timeCheck = 0

                if timeResetCount >= RepositionTimer and isError == False:
                    if error != None:
                        pyautogui.moveTo(error[0], error[1])
                        time.sleep(1)
                        pyautogui.click(error[0], error[1])
                        time.sleep(1)
                        pyautogui.hotkey('ctrl', 'r')
                        isError = True
                        print('Error -- Reloading')
                        time.sleep(5)
                        break
                    if errorIdle != None:
                        pyautogui.moveTo(errorIdle[0], errorIdle[1])
                        time.sleep(1)
                        pyautogui.click(errorIdle[0], errorIdle[1])
                        time.sleep(1)
                        pyautogui.hotkey('ctrl', 'r')
                        print('Idle -- Reloading')
                        isError = True
                        time.sleep(5)
                        break
                    backButton = pyautogui.locateCenterOnScreen('Image50/Back50.png', region = region, confidence = 0.7)
                    if backButton == None:
                        continue
                    elif backButton != None:
                        pyautogui.moveTo(backButton[0], backButton[1])
                        time.sleep(1)
                        pyautogui.click(backButton[0], backButton[1])
                    resetCount += 1
                    print('Reseting Position - ', resetCount)
                    time.sleep(2)
                    pyautogui.moveTo(hunt[0], hunt[1])
                    time.sleep(1)
                    pyautogui.click(hunt[0], hunt[1])
                    timeResetCount = 0
                
                if timeRestartCount >= ResetTimer and isError == False:
                    if error != None:
                        pyautogui.moveTo(error[0], error[1])
                        time.sleep(1)
                        pyautogui.click(error[0], error[1])
                        time.sleep(1)
                        pyautogui.hotkey('ctrl', 'r')
                        isError = True
                        print('Error -- Reloading')
                        time.sleep(5)
                        break
                    if errorIdle != None:
                        pyautogui.moveTo(errorIdle[0], errorIdle[1])
                        time.sleep(1)
                        pyautogui.click(errorIdle[0], errorIdle[1])
                        time.sleep(1)
                        pyautogui.hotkey('ctrl', 'r')
                        print('Idle -- Reloading')
                        isError = True
                        time.sleep(5)
                        break
                    backButton = pyautogui.locateCenterOnScreen('Image50/Back50.png', region = region, confidence = 0.7)
                    if backButton != None:
                        pyautogui.moveTo(backButton[0], backButton[1])
                        time.sleep(1)
                        pyautogui.click(backButton[0], backButton[1])
                        time.sleep(0.5)
                        pyautogui.click(backButton[0], backButton[1])
                    time.sleep(0.5)
                    pyautogui.click(backButton[0], backButton[1])
                    time.sleep(5)
                    isError = False
                    f = open('MouseUsed.txt', 'w')
                    f.write('F')
                    f.close()
                    print('Restarting Flow...')
                    break
                open('Queue.txt', 'w').write(nextQueue)
                time.sleep(60)
            
            if isError == True:
                open('Queue.txt', 'w').write(nextQueue)
                break
            else:
                open('Queue.txt', 'w').write(nextQueue)
                continue

        continue
except KeyboardInterrupt:
    print('\n')