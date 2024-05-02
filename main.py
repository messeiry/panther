# create a simple fast api app that returns a json response for default route.
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

# Run the app using uvicorn

# uvicorn main:app --reload
# --reload flag is used to reload the server whenever the code changes.

# Now, open the browser and go to http://
# localhost:8000/, you will see the response {"Hello": "World"}.    
# This is a simple FastAPI app that returns a JSON response for the default route.
