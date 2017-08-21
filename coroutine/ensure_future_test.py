import asyncio

async def slow_operation(future):
    await asyncio.sleep(1)
    future.set_result('Future is done!')

loop = asyncio.get_event_loop()
future = asyncio.Future()
task = asyncio.ensure_future(slow_operation(future))
#this is the same
#loop.run_until_complete(future)
loop.run_until_complete(task)
print(future.result())
loop.close()