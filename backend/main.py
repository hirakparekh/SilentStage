from fastapi import FastAPI

app = FastAPI(title="Silent Stage API")

@app.get("/")
async def root():
    return {"message": "Welcome to the Silent Stage API", "status": "active"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
