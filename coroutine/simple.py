import time
import asyncio
 
now = lambda : time.time()
 
async def do_some_work(x):
    print('Waiting: ', x)
 
start = now()
 
coroutine = do_some_work(2)
 
# a loop to handle async coroutine
loop = asyncio.get_event_loop()

#another run function is run_forever()
loop.run_until_complete(coroutine)
 
print('TIME: ', now() - start)