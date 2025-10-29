from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <head>
            <title>Hello Microservice</title>
        </head>
        <body style="font-family: Arial; text-align: center; margin-top: 100px;">
            <h1 style="color: #007bff;">Hello from FastAPI Microservice!</h1>
            <p>This is a simple microservice web app running on FastAPI </p>
        </body>
    </html>
    """