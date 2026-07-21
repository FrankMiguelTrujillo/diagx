from fastapi import FastAPI

app = FastAPI()

businesses_db = {}

@app.get("/")
def root():
    return {"status": "Diagx API running"}