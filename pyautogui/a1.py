#import the relevant modules
import pyautogui
import time
#give the python file some time before continuing
time.sleep(3)
#mouse functions
#prints the resolution of your screen
#print(pyautogui.size()) 
#prints the current position of the mouse
#print(pyautogui.position())
#moves the mouse over time(3 seconds)
#pyautogui.moveTo(100,100,3)#(x,y,time)
#move the mouse relative to its current position
#(current position sey x axis me itna or y axix me itna move kerega)
#pyautogui.moveRel(100,100,3)#(x,y,time)
#click
#pyautogui.click(500,500,3,3,button="left")#(x,y,no. of click,time)
"""pyautogui.rightClick()
pyautogui.leftClick()
pyautogui.doubleClick()
pyautogui.tripleClick()"""
#Scroll function
#Scroll up 500
#pyautogui.scroll(500)
#scroll down 500
#pyautogui.scroll(-500)
#mouse up and down
#pyautogui.mouseUp(100,100,button="left")
#pyautogui.mouseDown(100,100,button="left")

#example of mouse up and down
pyautogui.mouseDown(300,400,button="left")
pyautogui.moveTo(800,400,3)
pyautogui.mouseUp()
pyautogui.moveTo(1000,400,3)
#tiktok liker -example
for i in range(10):#(no. of posts)
    pyautogui.moveTo(450,500)
    time.sleep(1)
    pyautogui.doubleClick()
    time.sleep(1)
    pyautogui.moveTo(854,515)
    time.sleep(1)
    pyautogui.leftClick() 
    #keyword function
    pyautogui.write("hello")
    pyautogui.press("enter")
    pyautogui.press("space")
    #dinogame-chrome
    time.sleep(3)
    for i in range(20):
        pyautogui.press("space")
        time.sleep(0.5)
        #screenshot in pyautogui
        pyautogui.screenshot("screenshot.png")