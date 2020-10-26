from celery.schedules import crontab
from celery.task import periodic_task

@periodic_task(run_every=crontab(hour=21, minute=20, day_of_week="fri"))
def every_monday_morning():
    print("This is run every Monday morning at 7:30")