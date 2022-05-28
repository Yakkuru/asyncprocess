from abc import ABC, abstractmethod

class AsyncTask(ABC):
    @abstractmethod
    async def run_async(self) -> None:
        pass