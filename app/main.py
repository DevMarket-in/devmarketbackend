from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}


# get
# api/v1/getproduct
 # api/v1/postProduct

# {
#     "name":"product name",
#     imageUrl:"",
#     decription:"",
#     livepreview:""
# }
# mongodb
# ODM  ---> mongodb
# cors --> 
# helmet
# health /api/v1/health status(200).json()
