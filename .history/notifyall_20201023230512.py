# print('Yes Rahul! I have notified all peoples')
import schedule
import time

def job():
    print("I'm working...")

schedule.every(10).seconds.do(job)
schedule.every().hour.do(job)
schedule.every().day.at("21:03").do(job)
schedule.every().monday.do(job)
schedule.every().wednesday.at("13:15").do(job)
print(time.localtime())

while True:
    schedule.run_pending()
    time.sleep(1)