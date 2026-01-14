from fastapi import FastAPI
from api.variables import router as variables_router
from api.signals import router as signals_router
from api.synoptic import router as synoptic_router

app = FastAPI(title="Dymola Simulation API")

app.include_router(variables_router)
app.include_router(signals_router)
app.include_router(synoptic_router)

@app.get("/hello")
def hello():
    return {"message": "Dymola API online"}
