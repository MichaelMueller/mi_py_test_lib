from ..abstract.Test import Test as AbstractTest

class SelfTest(AbstractTest):
    
    async def _exec(self) -> None:
        print("Worx!")