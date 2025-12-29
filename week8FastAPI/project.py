from fastapi import FastAPI
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
 

