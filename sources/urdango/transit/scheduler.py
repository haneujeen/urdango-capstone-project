# scheduler.py
from apscheduler.schedulers.asyncio import AsyncIOScheduler
#from .tasks import update_target_bus


scheduler = AsyncIOScheduler()

"""
def start_tracking(uuid, veh_id, bus_route_id):
    # Schedule the `update_target_bus` function to be called every 60 seconds
    scheduler.add_job(
        func=update_target_bus,
        trigger="interval",
        seconds=60,
        args=[veh_id, bus_route_id],
        id=f'bus_{uuid}_{veh_id}_{bus_route_id}',
        replace_existing=True
    )

    if not scheduler.running:
        scheduler.start()


def stop_tracking(uuid, veh_id, bus_route_id):
    # Remove the job with the specified ID
    scheduler.remove_job(f'bus_{uuid}_{veh_id}_{bus_route_id}')
"""
