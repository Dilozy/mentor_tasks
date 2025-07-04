import asyncio


class AsyncTimer:
    async def __aenter__(self):
        self.start_time = asyncio.get_event_loop().time()
        return self
    
    async def __aexit__(self, exc_type, exc_value, exc_tb):
        print(asyncio.get_event_loop().time() - self.start_time)
        return True
    

async def my_coro():
    async with AsyncTimer():
        await asyncio.sleep(2)


asyncio.run(my_coro())