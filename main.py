from pickle import TRUE
import pyautogui as pag
import random
import time
while TRUE:
    x = random.randint(600,700)
    y = random.randint(200,600)
    pag.moveTo(x,y,0.5)
    time.sleep(2)

    