import os
import sys
import asyncio

# Set the current file's parent directory in the system path
project_dir = os.path.dirname( os.path.dirname( os.path.abspath(__file__) ) )
if not project_dir in sys.path:
    sys.path.insert(0, project_dir)

from mi_py_test_lib.SelfTest import SelfTest

async def main():
    await SelfTest().exec()
        
if __name__ == "__main__":
    asyncio.run(main())