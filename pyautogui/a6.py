import pyautogui as pg
import time
import random

time.sleep(8)
# print(pg.position())


pg.leftClick(1139,1038, 1, 1)
time.sleep(10)
#pg.click(1549,111)
#time.sleep(5)
#pg.leftClick(1800, 79)
#time.sleep(2)
pg.leftClick(1692, 414)
time.sleep(5)

list=[
    "python",
    "AI",
    "crypto",
    "blockchain",
    "NFT",
    "vaccine",
    "metaverse",
    "sustainability",
    "space",
    "innovation",
    "climate",
    "AR",
    "health",
    "smartphones",
    "robotics",
    "automation",
    "privacy",
    "data",
    "cybersecurity",
    "renewable"
]


for i in range(20):
    pg.leftClick(360, 90, 1, 0.5)
    msg=random.choice(list)
    pg.typewrite(msg)
    pg.press("enter")
    time.sleep(1)
    pg.leftClick(53, 80, 1, 0.5)