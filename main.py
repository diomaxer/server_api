from fastapi import FastAPI
import asyncio

futures = [...]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(futures))

app = FastAPI()


@app.get("/")
async def main_page():
    return {'team': 'Ivan Ivanov'}
