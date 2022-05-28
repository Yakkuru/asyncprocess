import asyncio
from async_task import AsyncTask
from startup_async_task import StartupAsyncTask

class AsyncProcess:
    def __init__(self, debug: bool = False):
        self._debug = debug
        self._startup_async_coros = []
        self._async_coros = []

    def register(self, at: AsyncTask) -> None:
        if isinstance(at, StartupAsyncTask):
            self._startup_async_coros.append(at.initialize_async())
        self._async_coros.append(at.run_async())
    
    def run(self) -> None:
        try:
            asyncio.run(self._initialize_async())
            asyncio.run(self._run_async())
        except KeyboardInterrupt:
            print('\n\nKeyboardInterrupt')

    async def _initialize_async(self):
        await asyncio.gather(*self._startup_async_coros)

    async def _run_async(self):
        if self._debug:
            asyncio.get_event_loop().set_debug(self._debug)
        await asyncio.gather(*self._async_coros)