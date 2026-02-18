<<<<<<< HEAD
from http.client import HTTPException

from fastapi import FastAPI, APIRouter, Request

from configurations import ping_collection, face_collection
from app.database.schemas import all_logs
from app.database.models import Ping, Faces

from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime


async def logging_middleware(request: Request, call_next):
    log_data = Ping(path=f"{request.url.path}", status="pending")
    log_data.created_at = datetime.now()
    log_data.updated_at = datetime.now()

    try:
        response = await call_next(request)
        log_data.status = response.status_code
    except Exception as e:
        log_data.status = 500
        log_data.updated_at = datetime.now()
        print(f"Error processing request: {e}")
        raise e
    finally:
        ping_collection.insert_one(dict(log_data))

    return response

app = FastAPI()
router = APIRouter()
app.middleware("http")(logging_middleware)
app.include_router(router)

@app.get("/")
async def get_all():
    data = ping_collection.find()
    return all_logs(data)


@app.post("/ping")
async def ping(new_ping: Ping):
    try:
        resp = ping_collection.insert_one(dict(new_ping))
        return {"status_code":200,"id": str(resp.inserted_id)}
    except Exception as e:
        return HTTPException(status_code=500, detail=f"error here{e}")


@app.post("/face")
async def face(facename):
    try:
        newface = Faces(name=facename)
        face_collection.insert_one(dict(newface))
    except Exception as e:
        return HTTPException(status_code=500, detail=f"error here{e}")

@app.get("/ping")
async def ping():
    return {"message": "Pong!"}
=======
from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "FastAPI is running!"}
>>>>>>> 78ff324b2d9bce681aae1b7c2aad269eece7b8bf
