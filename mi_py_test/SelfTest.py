from typing import Any, Coroutine
from .AbstractTest import AbstractTest

class SelfTest(AbstractTest):
    
    async def exec(self) -> bool:
        await super().exec()
        return True # always return true
        
    async def _exec(self) -> None:
        self._print( "Demo Message")
        
        self._check( 1==1, "1==1")
        self._check( 1==2, "1==2")
        
        def raise_not_implemented_error():
            raise NotImplementedError()
        
        self._expect_exception( raise_not_implemented_error, raise_not_implemented_error.__name__, NotImplementedError )
        
        self._assert( 1==1, "1==1")
        self._assert( 1==2, "1==2")