# hello this is my automation project
import pyautogui as pag
import random
import time

while True:
    a =random.randint(700,800)
    b =random.randint(300,700)
    pag.move(a,b,0.15)
    time.sleep(6)
