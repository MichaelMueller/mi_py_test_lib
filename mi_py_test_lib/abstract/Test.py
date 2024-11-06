from ..interface.Test import Test as TestInterface

class Test (TestInterface):
    
    async def exec(self) -> None:        
        await self._exec()
    
    async def _exec(self):
        raise NotImplementedError()
    
    