import logging
from .Test import Test

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
        else:
            print(f'{self.__class__.__name__} - Assertion PASSED: {assertion_description}')
    
    def _check( self, condition:bool, check_description:str ):
        if not condition:
            print( f'{self.__class__.__name__} - Check FAILED: {check_description}' )
        else:
            print(f'{self.__class__.__name__} - Check PASSED: {check_description}')
        