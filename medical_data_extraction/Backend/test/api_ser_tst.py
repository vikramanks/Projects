from fastapi import FastAPI
import uvicorn

# creating fastapi instance

app = FastAPI()

# uvicorn api_ser_tst:app --reload


food_items = {
    "indian": ['Dosa', 'Pongal'],
    "american": ['Burger', 'Pizza'],
    "italian": ['Pasta', 'Soup']
}


@app.get("/get_items/{cuisine}")
async def get_items(cuisine):
    return food_items.get(cuisine)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
