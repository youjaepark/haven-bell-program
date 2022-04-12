

from cgitb import text
from tkinter import *
window = Tk()
window.title("School Bell")
window.geometry('800x600')


btn1 = Button(window, text="평일 벨소리", width=20, height=15)
btn1.pack(side="left", padx=100)

btn2 = Button(window, text="시험 벨소리", width=20, height=15)
btn2.pack(side="right", padx=100)


window.mainloop()

#----------- 이줄 위에는 환호 --------------

import schedule
import time
 
def job():
    print("I'm working...")
schedule.every().monday.at("13:44").do(job)
schedule.every().tuesday.at("13:449","13:49").do(job)
schedule.every().wednesday.at("13:44").do(job)
schedule.every().thursday.at("13:44").do(job)
schedule.every().friday.at("13:44").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)





#------------- 이줄 위에는 주환 -------------



print("코딩 연습")
print("hello")
#------------- 이줄 위에는 유재 ------------
