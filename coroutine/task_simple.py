import asyncio
import time
 
now = lambda : time.time()
 
async def do_some_work(x):
    print('Waiting: ', x)
    return 'Done after {}s'.format(x)

def callback(future):
    print('Callback: ', future.result())
 
start = now()
 
coroutine = do_some_work(2)
loop = asyncio.get_event_loop()
# task is subclass of the asyncio.Future()
# blow code is the same
# task = asyncio.ensure_future(coroutine)
task = loop.create_task(coroutine)
task.add_done_callback(callback)
print(task)
loop.run_until_complete(task)
print(task)
print('TIME: ', now() - start)

#SEE func do_some_work() return
print('Task ret: {}'.format(task.result()))
loop.close()