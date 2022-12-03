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
