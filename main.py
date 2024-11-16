from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from starlette.staticfiles import StaticFiles

from config import config
from routes.registration import registration_router
from routes.auth import auth_router
from routes.user import user_router
from routes.company import company_router
from routes.candidate import candidate_router
from routes.employee import employee_router
from routes.team import team_router
from routes.vacancy import vacancy_router
from routes.frontend import frontend_router
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
app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(registration_router, prefix='/registration', tags=['registration'])
app.include_router(auth_router, prefix='/auth', tags=['auth'])
app.include_router(user_router, prefix='/user', tags=['user'])
app.include_router(company_router, prefix='/company', tags=['company'])
app.include_router(candidate_router, prefix='/candidate', tags=['candidate'])
app.include_router(employee_router, prefix='/employee', tags=['employee'])
app.include_router(team_router, prefix='/team', tags=['team'])
app.include_router(vacancy_router, prefix='/vacancy', tags=['vacancy'])
app.include_router(frontend_router, prefix='/frontend', tags=['frontend'])


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True, timeout_keep_alive=60, port=8001)
