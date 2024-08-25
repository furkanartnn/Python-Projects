import pyautogui as pt 
import time

while True:
    try:

        posXY = pt.position()
        print(posXY, pt.pixel(posXY[0], posXY[1]))
        time.sleep(1)
        if posXY[0]== 0:
            break 
    except Exception:
        pass  