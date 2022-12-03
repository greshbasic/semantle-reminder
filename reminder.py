'''
from datetime import datetime, timedelta
from threading import Timer

x=datetime.today()
y = x.replace(day=x.day, hour=1, minute=0, second=0, microsecond=0) + timedelta(days=1)
delta_t=y-x

secs=delta_t.total_seconds()

async def semantle_reminder():
    await ctx.send("@everyone time for semantle!")
    

t = Timer(secs, semantle_reminder)
t.start()
'''

'''
version 2
'''

from datetime import datetime
import threading

async def checkTime():
    threading.Timer(1, checkTime).start()

    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    print("Current time is: " + current_time)

    if(current_time == '06:00:00'):
        await ctx.send("@everyone its semantle time!")


checkTime()
