# --- Asyncio ---
# Used for I/O bound tasks (like making network requests or database queries)
# to avoid blocking the main thread.
import asyncio

async def fetch_data(id):
    print(f"Fetching data {id}...")
    await asyncio.sleep(1) # Simulating a network request
    return f"Data {id}"

async def main():
    # Run multiple async functions concurrently
    results = await asyncio.gather(fetch_data(1), fetch_data(2))
    print(results)

# To run the async function:
# asyncio.run(main())
