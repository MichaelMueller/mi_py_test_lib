from mi_py_test_lib.AbstractTest import AbstractTest

class SelfTest(AbstractTest):
    
    async def _exec(self) -> None:
        print("Worx!")