import time, pyautogui, random

print('Please move browser with ucertify article to screen1')

while True:
    eop = pyautogui.locateOnScreen('eop.png')
    if eop == None:
        pyautogui.scroll(-40, x=955, y=415)
        time.sleep(random.randint(2,5))
    else:
        x,y = pyautogui.locateCenterOnScreen('nextBtn.png')
        time.sleep(5)
        pyautogui.click(x,y)
        time.sleep(5)
      
        

