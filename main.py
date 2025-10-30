from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, PlainTextResponse
from prometheus_client import Counter, Histogram, start_http_server, generate_latest, CONTENT_TYPE_LATEST
import time

app = FastAPI()

# ---------------- Metrics ----------------
REQUEST_COUNT = Counter(
    'http_requests_total', 
    'Total HTTP requests',
    ['method', 'endpoint', 'status']
)

REQUEST_LATENCY = Histogram(
    'http_request_latency_seconds', 
    'Request latency in seconds',
    ['endpoint']
)

ERROR_COUNT = Counter(
    'http_request_errors_total',
    'Total HTTP errors',
    ['endpoint', 'status']
)

# ---------------- App Routes ----------------
@app.get("/", response_class=HTMLResponse)
def home():
    start_time = time.time()
    status_code = 200
    try:
        html_content = """
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
        return HTMLResponse(content=html_content, status_code=status_code)
    except Exception as e:
        status_code = 500
        ERROR_COUNT.labels(endpoint="/", status=status_code).inc()
        raise e
    finally:
        REQUEST_COUNT.labels(method="GET", endpoint="/", status=status_code).inc()
        REQUEST_LATENCY.labels(endpoint="/").observe(time.time() - start_time)

# ---------------- Metrics Endpoint ----------------
@app.get("/metrics")
def metrics():
    return PlainTextResponse(generate_latest(), media_type=CONTENT_TYPE_LATEST)
