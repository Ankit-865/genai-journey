from fastapi import FastAPI
app = FastAPI()
@app.get ("/")
def home ():
 return { " message = Hello world"}

@app.get("/about")
def about ():
 return {"this is my first api and i am learning fast api"}
