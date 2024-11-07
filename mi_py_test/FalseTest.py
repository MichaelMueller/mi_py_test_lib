from typing import Any, Coroutine
from .AbstractTest import AbstractTest

class FalseTest(AbstractTest):
    
    async def exec(self) -> bool:
        return False