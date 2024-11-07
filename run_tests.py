# built-ing
import os
import sys
import asyncio
# local
from mi_py_test.SelfTestSuite import SelfTestSuite

async def main():
    await SelfTestSuite().exec()
        
if __name__ == "__main__":
    asyncio.run(main())