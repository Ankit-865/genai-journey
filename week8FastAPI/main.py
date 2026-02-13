from fastapi import FastAPI, Path , HTTPException , Query
import json
app = FastAPI()

def load_data():
    with open ('patient.json', 'r') as f:
      data= json.load (f)

    return data 

@app.get ("/")
def home ():
 return { " message = patient management API"}

@app.get("/about")
def about ():
 return {"api for managing patient records and appointments"}

@app.get("/view")
def view ():
    data = load_data()
   
    return data
 
@app.get("/patient/{patient_id}")
def view_patient(patient_id: int=  Path(..., description= "id of the patient in the DB", example= 1) ):
    data = load_data()   # list of patients

    # Loop to find the matching patient
    for patient in data:
        if patient["id"] == patient_id:
            return patient
        raise HTTPException (status_code= 404 , detail= "patient not found ")

@app.get('/sort')
def sort_patient(
    sort_by: str = Query(..., description="Sort by disease, gender or admitted"),
    order: str = Query('asc', description="Sort order: asc or desc")
):
    valid_fields = ['disease', 'gender', 'admitted']

    if sort_by not in valid_fields:
        raise HTTPException(
            status_code=400,
            detail=f'Invalid field. Select from {valid_fields}'
        )

    if order not in ['asc', 'desc']:
        raise HTTPException(
            status_code=400,
            detail='Invalid order. Select asc or desc'
        )

    data = load_data()

    reverse_order = True if order == 'desc' else False

    sorted_data = sorted(
        data,
        key=lambda x: x.get(sort_by),
        reverse=reverse_order
    )

    return sorted_data
