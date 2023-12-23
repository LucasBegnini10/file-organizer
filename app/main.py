from fastapi import FastAPI
from dotenv import load_dotenv
import os
from fastapi.middleware.cors import CORSMiddleware

from app.routers.file import FileRouter
from app.routers.user import UserRouter
from app.routers.auth import AuthRouter
from app.routers.folder import FolderRouter

from app.config.db import engine
from app.models.user import UserModel
from app.models.file import FileModel
from app.models.folder import FolderModel

UserModel.metadata.create_all(bind=engine)
FileModel.metadata.create_all(bind=engine)
FolderModel.metadata.create_all(bind=engine)

app = FastAPI()

load_dotenv()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(FileRouter.router, tags=['File'])
app.include_router(UserRouter.router, tags=['User'])
app.include_router(AuthRouter.router, tags=['Auth'])
app.include_router(FolderRouter.router, tags=['Folder'])

