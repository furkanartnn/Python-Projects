import pyautogui as pt 
from time import sleep
import pyperclip
import random 

sleep(3)

position1 = pt.locateOnScreen("whatsapp/smiley_paperclip.png", confidence = .6)
x = position1[0]
y = position1[1]


def get_message():
    global x, y 

    position = pt.locateOnScreen("whatsapp/smiley_paperclip.png", confidence = .6)
    x = position[0]
    y = position[1]
    pt.moveTo(x, y, duration=.05)
    pt.moveTo(x+ 70, y - 40, duration=.5)
    pt.tripleClick()
    pt.rightClick()
    pt.moveRel(12,15)
    pt.click()
    whatsapp_message = pyperclip.paste()
    pt.click()
    print("Message received: " + whatsapp_message)

    return whatsapp_message 


def post_response(message):
    global x,y 
    
    position = pt.locateOnScreen("whatsapp/smiley_paperclip.png", confidence = .6)
    x = position[0]
    y = position[1]
    pt.moveTo(x + 200, y +28, duration=.5)
    pt.click()
    pt.typewrite(message, interval = .01)

    #pt.typewrite("\n", interval =.01)

def process_response(message):
    random_no = random.randrange(3)

    if "?" in str(message).lower():
        return "Don't ask me any questions!"
    
    else:
        if random_no ==0:
            return "That's cool!"
        elif random_no == 1:
            return "Remember to make dishes"
        else: 
            return "I want to eat something."


def check_for_new_messages():
    pt.moveTo(x+50, y-35, duration=.5)

    while True:
        try:
            position = pt.locateOnScreen("whatsapp/green_circle.png", confidence=.7)

            if position is not None:
                pt.moveTo(position)
                pt.moveRel(-100,0)
                pt.click()
                sleep(.5)
        except(Exception):
            print("No new other users with new messages located")
        
        if pt.pixelMatchesColor(int(x),int(y), (255,255,255), tolerance = 10):
            print("is_white")
            processed_message = prcess_response(get_message())
            post_response(processed_message)
        
        else:
            print("No new messages yet...")
        sleep(5)
        





#processed_message = process_response(get_message())

#post_response(processed_message)



