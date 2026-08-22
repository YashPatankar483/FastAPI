from fastapi import FastAPI
import json

app = FastAPI()

@app.get("/")
def doctor():
    return {"message" : "Welcome to my Clinic :)"}

@app.get("/about")
def about():
    return {"message" : "Doctor's clinic helps you cure from the fever, cold or any health issues you are dealing with! The Doctor is a Mech Engineer."}

@app.get("/view")
def case_papers():

    with open("data.json", "r") as f:
        data = json.load(f)

    return data