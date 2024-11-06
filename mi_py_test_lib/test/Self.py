from ..abstract.Test import Test as AbstractTest

class Self(AbstractTest):
    
    async def _exec(self) -> None:
        print("Worx!")