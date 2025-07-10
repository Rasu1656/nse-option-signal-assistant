from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "NSE Data API for GPT Actions is live."}
