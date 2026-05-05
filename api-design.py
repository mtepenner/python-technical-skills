# api_design.py
# Example: RESTful API for a Drone Mesh Network using FastAPI
# Run with: uvicorn api_design:app --reload

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Pydantic model for data validation
class Drone(BaseModel):
    id: int
    status: str
    battery_level: float

# In-memory storage for demonstration
mesh_network: List[Drone] = []

@app.post("/drones/", status_code=201)
def register_drone(drone: Drone):
    """Adds a new drone to the network (POST request)."""
    mesh_network.append(drone)
    return {"message": "Drone successfully integrated into the mesh network"}

@app.get("/drones/{drone_id}", response_model=Drone)
def get_drone_status(drone_id: int):
    """Retrieves specific drone telemetry (GET request)."""
    for d in mesh_network:
        if d.id == drone_id:
            return d
    # Proper error handling with standard HTTP status codes
    raise HTTPException(status_code=404, detail="Drone not found in network")
