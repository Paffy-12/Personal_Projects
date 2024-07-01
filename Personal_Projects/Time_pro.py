import pyautogui as pag
import random
import time

while True:
    x = random.randint(300, 500)
    y = random.randint(200, 700)
    pag.moveTo(x, y, 0.5)
    time.sleep(2)

