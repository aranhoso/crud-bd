from fastapi import FastAPI, HTTPException, status

app = FastAPI(
    title="Simple API",
    description="A simple API that returns 200 OK",
    version="1.0.0"
)

@app.get("/", status_code=status.HTTP_200_OK)
def root():
    return {"status": "success", "message": "API is running with MySQL connection"}