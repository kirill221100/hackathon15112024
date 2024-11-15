from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from config import config
from routes.registration import registration_router
from routes.auth import auth_router
from routes.user import user_router
from db.db_setup import init_db
import uvicorn


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield

app = FastAPI(lifespan=lifespan, debug=config.DEBUG, title='tarot')
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
app.include_router(registration_router, prefix='/registration', tags=['registration'])
app.include_router(auth_router, prefix='/auth', tags=['auth'])
app.include_router(user_router, prefix='/user', tags=['user'])


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True, timeout_keep_alive=60, port=8001)
