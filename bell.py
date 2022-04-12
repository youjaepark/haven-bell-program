

from cgitb import text
from tkinter import *
window = Tk()
window.title("School Bell")
window.geometry('800x600')

point = 1

def first(): 
    point = 1
    print(point)
    Label1 = Label(window, background='green')
    Label1.pack()

def second():
    point = 2
    print(point)
    btn1['bg'] = 'white'
    btn2['bg'] = 'green'

btn1 = Button(window, text="평일 벨소리", width=30, height=15, command=first)
btn1.pack(side="left", padx=50)

btn2 = Button(window, text="시험 벨소리", width=30, height=15, command= second)
btn2.pack(side="right", padx=50)

window.mainloop()


#----------- 이줄 위에는 환호 --------------


from datetime import datetime
import schedule
import time

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print(current_time)
 


def job():
    print("자연, 우리의 미래...")

# 매일 특정 HH:MM 및 다음 HH:MM:SS에 작업 실행
schedule.every().day.at("2:00").do(job)
schedule.every().day.at("2:00:42").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)




#------------- 이줄 위에는 주환 -------------



print("코딩 연습")
print("hello")
#------------- 이줄 위에는 유재 ------------
