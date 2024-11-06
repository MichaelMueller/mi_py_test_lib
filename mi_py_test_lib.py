import asyncio
from mi_py_test_lib.tests.SelfTest import SelfTest

async def main():
    await SelfTest().exec()
        
if __name__ == "__main__":
    asyncio.run(main())