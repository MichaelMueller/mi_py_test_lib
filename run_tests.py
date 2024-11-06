# built-ing
import os
import sys
import asyncio
# local
from mi_py_test.SelfTest import SelfTest

async def main():
    await SelfTest().exec()
        
if __name__ == "__main__":
    asyncio.run(main())