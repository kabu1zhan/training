import pyautogui as pg

def dota():
    pg.hotkey("ctrl", "esc")
    pg.sleep(1)
    pg.typewrite('Steam', 0.5)
    pg.press("Enter")
    pg.sleep(2)
    pg.click(x=1048, y=479, duration=0.5)
    pg.sleep(0.5)
    pg.press('backspace', presses=20)
    pg.sleep(0.5)
    pg.typewrite('22_fantom_2', 0.5)
    pg.sleep(0.5)
    pg.click(x=1095, y=509, duration=0.5)
    pg.sleep(0.5)
    pg.typewrite('VedmaK92943349561M', 0.3)
    pg.press('enter')
    pg.sleep(8)
    pg.hotkey("win", "d")
    pg.sleep(1)
    pg.doubleClick(x=1715, y=51, duration=0.5)
    pg.sleep(2)
    pg.typewrite('88848', 0.5)
    pg.sleep(0.5)
    pg.press("Enter")
    pg.sleep(1)
    pg.doubleClick(x=1069, y=422, duration=0.5)
    pg.sleep(1)
    pg.hotkey("win", "d")
    pg.hotkey("ctrl", "esc")
    pg.sleep(1)
    pg.typewrite('Steam', 0.5)
    pg.press("Enter")
    pg.sleep(1)
    pg.click(x=1020, y=606, duration=0.5)
    pg.rightClick(x=1020, y=606, duration = 2)
    pg.press('down', presses=3)
    pg.sleep(1)
    pg.press("Enter")
a = dota()
print(a)
