import pyautogui
import time

region = (550, 700, 550, 350)
center = (region[0] + region[2] / 2, region[1] + 350 / 2 )
waitTime = 8.2
queueNum = '8'
nextQueue = '9'

try:
    while True:
        time.sleep(15)

        while open('Queue.txt', 'r').read() != queueNum:
            time.sleep(1.7)
            if open('Queue.txt', 'r').read() == '0':
                open('Queue.txt', 'w').write(queueNum)
            continue

        while open('MouseUsed.txt', 'r').read() == 'T':
            time.sleep(waitTime)
            continue
        print("In Loop")
        f = open('MouseUsed.txt', 'w')
        f.write('T')
        f.close()
        while True:
            time.sleep(15)
            connectButton = pyautogui.locateCenterOnScreen('Image50/Connect50.png', region = region, confidence = 0.7)
            if connectButton == None:
                pyautogui.moveTo(center)
                time.sleep(1)
                pyautogui.click(center)
                time.sleep(1)
                pyautogui.hotkey('ctrl', 'shift', 'r')
                print('Connect Not Found -- Reloading')
                f = open('MouseUsed.txt', 'w')
                f.write('F')
                f.close()
                continue
            pyautogui.moveTo(connectButton[0], connectButton[1])
            pyautogui.click(connectButton[0], connectButton[1])
            print('Connecting Wallet...')
            break
        time.sleep(5)

        # mmButton = pyautogui.locateCenterOnScreen('Image50/Meta50.png', region = region, confidence = 0.7)
        # if mmButton == None:
        #     pyautogui.moveTo(center)
        #     time.sleep(0.5)
        #     pyautogui.click(center)
        #     time.sleep(0.5)
        #     pyautogui.hotkey('ctrl', 'shift', 'r')
        #     print('MetaMask Not Found -- Reloading')
        #     f = open('MouseUsed.txt', 'w')
        #     f.write('F')
        #     f.close()
        #     continue
        # pyautogui.moveTo(mmButton[0], mmButton[1])
        # pyautogui.click(mmButton[0], mmButton[1])
        # print('Signing MetaMask...')
        # time.sleep(5)

        while True:
            signButton = pyautogui.locateCenterOnScreen('Image50/Sign50.png', region = region, confidence = 0.7)
            if signButton == None:
                pyautogui.moveTo(center)
                time.sleep(1)
                pyautogui.click(center)
                time.sleep(1)
                pyautogui.hotkey('ctrl', 'shift', 'r')
                print('MetaMask Not Found -- Reloading')
                f = open('MouseUsed.txt', 'w')
                f.write('F')
                f.close()
                break
            pyautogui.moveTo(signButton[0], signButton[1])
            pyautogui.click(signButton[0], signButton[1])
            print('Loading...')
            break
        f = open('MouseUsed.txt', 'w')
        f.write('F')
        f.close()
        open('Queue.txt', 'w').write(nextQueue)
        time.sleep(15)

        while True:
            connectButton = None
            mmButton = None
            signButton = None
            selectHero = None
            homeButton = None
            workButton = None
            closeHero = None
            error = None
            timeResetCount = 0
            timeRestartCount = 0
            timeCheck = 0
            isError = False

            while open('Queue.txt', 'r').read() != queueNum:
                time.sleep(1.7)
                if open('Queue.txt', 'r').read() == '0':
                    open('Queue.txt', 'w').write(queueNum)
                continue

            while open('MouseUsed.txt', 'r').read() == 'T':
                time.sleep(waitTime)
                continue
            f = open('MouseUsed.txt', 'w')
            f.write('T')
            f.close()

            selectHero = pyautogui.locateCenterOnScreen('Image50/Hero50.png', region = region, confidence = 0.7)
            error = pyautogui.locateCenterOnScreen('Image50/Error50.png', region = region, confidence = 0.7)

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
                open('Queue.txt', 'w').write(nextQueue)
                break
            if selectHero == None :
                pyautogui.moveTo(center)
                time.sleep(0.5)
                pyautogui.click(center)
                time.sleep(0.5)
                pyautogui.hotkey('ctrl', 'shift,' 'r')
                print('Cant Load Game -- Reload')
                f = open('MouseUsed.txt', 'w')
                f.write('F')
                f.close()
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
                    f = open('Queue.txt', 'w')
                    f.write('0')
                    f.close
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
                time.sleep(1)
                break
            heroCount = 0
            if isError == False:
                error = None
                print('Bring Hero To Work...')
                while True:
                    workButton = pyautogui.locateCenterOnScreen('Image50/Work50.png', region = region, confidence = 0.95)
                    error = pyautogui.locateCenterOnScreen('Image50/Error50.png', region = region, confidence = 0.7)
                    workError = pyautogui.locateCenterOnScreen('Image50/WorkError50.png', region = region, confidence = 0.7)
                    if error != None:
                        pyautogui.moveTo(error[0], error[1])
                        time.sleep(1)
                        pyautogui.click(error[0], error[1])
                        time.sleep(1)
                        pyautogui.hotkey('ctrl', 'shift', 'r')
                        print('Error -- Reloading')
                        isError = True
                        time.sleep(5)
                        f = open('MouseUsed.txt', 'w')
                        f.write('F')
                        f.close()
                        f = open('Queue.txt', 'w')
                        f.write('0')
                        f.close
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
                        f = open('MouseUsed.txt', 'w')
                        f.write('F')
                        f.close()
                        f = open('Queue.txt', 'w')
                        f.write('0')
                        f.close
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
                
                if error != None:
                    pyautogui.moveTo(error[0], error[1])
                    time.sleep(1)
                    pyautogui.click(error[0], error[1])
                    time.sleep(1)
                    pyautogui.hotkey('ctrl', 'shift', 'r')
                    isError = True
                    print('Error -- Reloading')
                    time.sleep(5)
                    f = open('MouseUsed.txt', 'w')
                    f.write('F')
                    f.close()
                    f = open('Queue.txt', 'w')
                    f.write('0')
                    f.close
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
                if error != None:
                    pyautogui.moveTo(error[0], error[1])
                    time.sleep(1)
                    pyautogui.click(error[0], error[1])
                    time.sleep(1)
                    pyautogui.hotkey('ctrl', 'shift', 'r')
                    isError = True
                    print('Error -- Reloading')
                    time.sleep(5)
                    f = open('MouseUsed.txt', 'w')
                    f.write('F')
                    f.close()
                    f = open('Queue.txt', 'w')
                    f.write('0')
                    f.close
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
                open('Queue.txt', 'w').write(nextQueue)
                break
            
            resetCount = 0

            while isError == False:
                timeResetCount += 60
                timeRestartCount += 60
                timeCheck += 60

                while open('Queue.txt', 'r').read() != queueNum:
                    time.sleep(1.7)
                    if open('Queue.txt', 'r').read() == '0':
                        open('Queue.txt', 'w').write(queueNum)
                    continue

                while open('MouseUsed.txt', 'r').read() == 'T':
                    time.sleep(waitTime)
                    continue
                f = open('MouseUsed.txt', 'w')
                f.write('T')
                f.close()
                error = None
                error = pyautogui.locateCenterOnScreen('Image50/Error50.png', region = region, confidence = 0.7)
                if timeCheck >= 120:
                    newMap = pyautogui.locateCenterOnScreen('Image50/NewMap50.png', region = region, confidence = 0.7)
                    if error != None:
                        pyautogui.moveTo(error[0], error[1])
                        time.sleep(1)
                        pyautogui.click(error[0], error[1])
                        time.sleep(1)
                        pyautogui.hotkey('ctrl', 'shift', 'r')
                        isError = True
                        print('Error -- Reloading')
                        time.sleep(5)
                        f = open('MouseUsed.txt', 'w')
                        f.write('F')
                        f.close()
                        f = open('Queue.txt', 'w')
                        f.write('0')
                        f.close
                        break
                    if newMap != None:
                        pyautogui.moveTo(newMap[0], newMap[1])
                        time.sleep(1)
                        pyautogui.click(newMap[0], newMap[1])
                        print('Change Map...')
                        f = open('MouseUsed.txt', 'w')
                        f.write('F')
                        f.close()
                        f = open('Queue.txt', 'w')
                        f.write('0')
                        f.close
                    
                    timeCheck = 0

                if timeResetCount >= 180:
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
                        f = open('Queue.txt', 'w')
                        f.write('0')
                        f.close
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
                
                if timeRestartCount >= 1800:
                    if error != None:
                        pyautogui.moveTo(error[0], error[1])
                        time.sleep(1)
                        pyautogui.click(error[0], error[1])
                        time.sleep(1)
                        pyautogui.hotkey('ctrl', 'shift', 'r')
                        isError = True
                        print('Error -- Reloading')
                        time.sleep(5)
                        f = open('MouseUsed.txt', 'w')
                        f.write('F')
                        f.close()
                        f = open('Queue.txt', 'w')
                        f.write('0')
                        f.close
                        break
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
                f = open('MouseUsed.txt', 'w')
                f.write('F')
                f.close()
                open('Queue.txt', 'w').write(nextQueue)
                time.sleep(60)
            
            if isError == True:
                f = open('MouseUsed.txt', 'w')
                f.write('F')
                f.close()
                open('Queue.txt', 'w').write(nextQueue)
                break
            else:
                f = open('MouseUsed.txt', 'w')
                f.write('F')
                f.close()
                open('Queue.txt', 'w').write(nextQueue)
                continue

        continue
except KeyboardInterrupt:
    print('\n')