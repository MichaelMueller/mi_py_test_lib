import logging
from mi_py_test_lib.Test import Test

class AbstractTest (Test):
    def __init__(self) -> None:
        super().__init__()
        
    async def exec(self) -> None:        
        await self._exec()
    
    async def _exec(self):
        raise NotImplementedError()
    
    def _assert( self, condition:bool, assertion_description:str ):
        if not condition:
            raise AssertionError( f'{self.__class__.__name__} - Assertion FAILED: {assertion_description}' )
    
    def _check( self, condition:bool, assertion_description:str ):
        if not condition:
            logging.warning( f'{self.__class__.__name__} - Check FAILED: {assertion_description}' )
        