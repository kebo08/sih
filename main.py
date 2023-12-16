from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse


app = FastAPI()
origins = [
    # "http://localhost.tiangolo.com",
    # "https://localhost.tiangolo.com",
    # "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


channel_data = {
    "Ernakulam": {"latitude": 9.9674, "longitude": 76.2422},
    "Mattancherry": {"latitude": 9.9542, "longitude": 76.2606}
}

ships = [
    {"name": "Ship1", "latitude": 9.970, "longitude": 76.250},
    {"name": "Ship2", "latitude": 9.960, "longitude": 76.255},
    {"name": "Ship3", "latitude": 9.955, "longitude": 76.245},
]

def change_ship_pos(ships):
    for i in ships:
        i["latitude"] += 0.001
        i["longitude"] += 0.001


@app.get("/initial_data", response_model=dict)
async def get_initial_data():
    change_ship_pos(ships)
    data = {"ships": ships, "channels": channel_data}
    return JSONResponse(content=data, status_code=200)
