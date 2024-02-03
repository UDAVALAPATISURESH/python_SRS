
#     file = open(r"C:\Users\lucky\PycharmProjects\pythonProject2\filehandling\hi.txt", "r")
#     content = file.read()
#     file.close()
#     return content
# cont = file_read()
# print(cont)


# def file_read():

# file = open(r"C:\Users\lucky\PycharmProjects\pythonProject2\filehandling\hi.txt", "a")
# content = file.write("\n iam  Suresh")
# content = file.write("\n iam  Suresh")
# print(content)



# with open("hi.txt","r") as file:
#     content = file.read()
#     print(content)

from Tools.scripts.which import msg
from fastapi import  FastAPI
from  pydantic import  BaseModel
# 1 . Define an API object
app = FastAPI()
# 2 .Define data type
class Msg(BaseModel):
    msg : str
# 3.map HTTP method and path to function
@app.get("/")
async def root():
    return {"message ": "Hello World . Welcome to the API home page"}
@app.get("/path")
async def function_demo_get(inp : msg):
    return {"message": "this is /path endpoint, use post required path " }
# uvicorn main:app --reload