from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
from fno import sendMsg

sched = BlockingScheduler()

# Schedule job_function to be called every two hours
sched.add_job(sendMsg, 'interval', seconds=10)

sched.start()