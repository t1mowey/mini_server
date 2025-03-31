from fastapi import FastAPI

app = FastAPI()

@app.get("/blame?name={name}")
def blame(name: str):
    return {"message": f"Hello {name}, YR loshara!"}
