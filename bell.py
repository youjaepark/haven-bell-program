


#----------- 이줄 위에는 환호 --------------





#------------- 이줄 위에는 주환 -------------

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





#------------- 이줄 위에는 유재 -------------
