from fastapi import FastAPI, Path, HTTPException, Query
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


@app.get("/patient/{patient_id}")
def patient_info(patient_id : str = Path(..., description="This path param identifies a patient using its patient id", example="PT-1003")):

    with open("data.json", "r") as f:
            data = json.load(f)

            for patient in data["patients"]:
                 if patient["patient_id"] == patient_id:
                    patient_info = patient
                    # print(patient_info)
                    return patient_info

            else:
                 raise HTTPException(status_code=404, detail="Patient not found")



@app.get("/sort")
def sorted_list(sort_by: str = Query(..., description="height_cm, weight_kg, bmi, heart_rate_bpm"), order: str = Query("asc", description="asc or desc")):

     valid_fields = ["height_cm", "weight_kg", "bmi", "heart_rate_bpm"]

     if sort_by not in valid_fields:
          raise HTTPException(status_code=400, detail=f"Invalid field, select from {valid_fields}")

     if order not in ["asc", "desc"]:
          raise HTTPException(status_code=400, detail=f"Invalid field, select from {["asc", "desc"]}")

     with open("data.json", "r") as f:
          data = json.load(f)

          patients = data["patients"]            # list of patients

          sort_order = True if order=="desc" else False

          sorted_data = sorted(patients, key = lambda x: x["vitals"][sort_by], reverse=sort_order)

          return sorted_data