from fastapi import FastAPI

app = FastAPI()

@app.get("/blame?name=Nikita")
def blame(name: str):
    return {"message": f"Hello {name}, YR loshara!"}
