from abc import abstractmethod
from async_task import AsyncTask

class StartupAsyncTask(AsyncTask):
    @abstractmethod
    async def initialize_async(self) -> None:
        pass