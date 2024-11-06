from mi_py_test_lib.Test import Test

class AbstractTest (Test):
    
    async def exec(self) -> None:        
        await self._exec()
    
    async def _exec(self):
        raise NotImplementedError()
    
    