import pyautogui as pt 
from time import sleep 

class GuiCommands:
    def __init__(self, x, y):
        self.x = x 
        self.y = y 
    
    def navigate_to_heart(self, speed):
        position = pt.locateOnScreen("bookmark.png", confidence = .8)
        self.x = position[0] - 550
        self.y = position[1] + 10 
        pt.moveTo(self.x, self.y, duration = spped) 
        print("Navigating to heart!")
        sleep(.3)

commands = GuiCommands(0, 0)

for i in range(5):
    try:
        commands.navigate_to_heart(1)
        if pt.pixelMatchesColor(pt.position().x, pt.position().y, (237,73,86), tolerance = 10):
            pt.scroll(5000)
            sleep(.3)
        else:
            pt.click()
            sleep(.3)
    except Exception as e:
        print(e)
        pt.scroll(5000)
        sleep(.3)