import pyautogui as spam
import time

limit = input("500")
msg = input("Jij bent ongelukkig.. Pleeg zelfmoord!")

i = 0

time.sleep(5)

while i<int(limit):

    spam.typewrite(msg)
    spam.press('enter')

i += 1 
