from typing import Any, Coroutine

from mi_py_test.Test import Test
from .AbstractTest import AbstractTest
from .SelfTest import SelfTest
from .FalseTest import FalseTest

class SelfTestSuite(AbstractTest):
    
    def dependent_tests(self) -> list[Test]:
        return [SelfTest(), FalseTest()]
    
    async def exec(self) -> bool:
        await super().exec()
        self._print("Expected Results in Self Test Suite. All Tests Passed!")
        return True # always return true
        
    async def _exec(self) -> None:
        pass