import sys
path = '/home/Desktop/lab1'
if path not in sys.path:
    sys.path.insert(0, path)

from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware
from fastapi.responses import HTMLResponse
from mangum import Mangum

# Создаем FastAPI приложение
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello from FastAPI on PythonAnywhere"}

# Для PythonAnywhere используем WSGIMiddleware
application = WSGIMiddleware(app)