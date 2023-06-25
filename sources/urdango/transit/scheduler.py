from apscheduler.schedulers.background import BackgroundScheduler
from .tasks import update_bus

def start():
    scheduler = BackgroundScheduler()

    update_bus(scheduler)

    scheduler.add_job(lambda: update_bus(scheduler), 'interval', seconds=5)

    print('Started scheduler')
    scheduler.start()


