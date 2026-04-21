# IVP - Installation Verification Procedure
import asyncio
import os
from ib_async import IB

# Load environment variables
from dotenv import load_dotenv
load_dotenv(".env")

ib_host = os.environ.get("IB_HOST", "127.0.0.1")
ib_port = os.environ.get("IB_PORT", 4002)
ib_client_id = os.environ.get("IB_CLIENT_ID", 1)

async def test():
    ib = IB()
    try:
        await ib.connectAsync(ib_host, ib_port, clientId=ib_client_id)
        print("✓ Connected successfully!")
        print(f"Accounts: {ib.managedAccounts()}")
        ib.disconnect()
    except Exception as e:
        print(f"✗ Connection failed: {e}")

asyncio.run(test())
