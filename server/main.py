import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sockets import sio_app

app = FastAPI()
app.mount('/', app=sio_app)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
async def home():
    return {'message': 'Hello👋 Developers💻'}


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
