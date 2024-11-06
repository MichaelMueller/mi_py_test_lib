from .AbstractTest import AbstractTest

class SelfTest(AbstractTest):
    
    async def _exec(self) -> None:
        print("Worx!")