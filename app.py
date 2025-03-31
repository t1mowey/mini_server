from fastapi import FastAPI

app = FastAPI()

@app.get("/blame/{name}")
def read_root(name: str):
    return {"message": f"Hello {name}, YR loshara!"}
