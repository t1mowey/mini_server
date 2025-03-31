from fastapi import FastAPI

app = FastAPI()

@app.get("/blame")
def blame(name: str):
    return {"message": f"Hello {name}, YR loshara!"}
