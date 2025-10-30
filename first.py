

from fastapi import FastAPI

app = FastAPI()

@app.get("/get-message")
def hello(name: str):
    return {'Message': "Hi " + name + ', how are you?'}
#async def read_root():
#    return {"Message": "Trying out this API!"}