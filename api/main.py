from fastapi import FastAPI
from api.routers import solver
from fastapi.middleware.cors import CORSMiddleware


origins = ["http://localhost:5173"]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(solver.router)

@app.get("/")
async def root():
    return {"message": "Api Online"}
