from ..interfaces.Test import Test

class AbstractTest (Test):
    
    async def exec(self) -> None:        
        await self._exec()
    
    async def _exec(self):
        raise NotImplementedError()
    
    