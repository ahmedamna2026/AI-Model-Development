from fastapi import FastAPI

app = FastAPI()


# GET fits because the endpoint returns a calculation without saving data.
@app.get("/add")
def add(a, b):
    # FastAPI converts both required inputs to integers before adding.
    return {"sum": int(a) + int(b)}
