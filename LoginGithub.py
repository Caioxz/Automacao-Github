import pyautogui
import time

pyautogui.press('win')
time.sleep(0.70)
pyautogui.write('chrome')
time.sleep(1)
pyautogui.press('enter')
time.sleep(1)
pyautogui.write('https://github.com/')
time.sleep(1.3)
pyautogui.press('enter')
time.sleep(1.5)
pyautogui.click(x=1217, y=115)#clicar no "entrar" do github
time.sleep(1.8)
pyautogui.click(x=700, y=289)#clicar no email
time.sleep(1)
pyautogui.write('##########')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.write('$#######')
time.sleep(0.90)
pyautogui.press('tab')
pyautogui.press('enter')
