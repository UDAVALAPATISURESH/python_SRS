from fastapi import FastAPI


app = FastAPI()

@app.get('/')
def home():
    return {'name':"suresh",
            'city':'Tirupati',
            'age':20}

@app.get("/name_details")
def suresh():
    return {'skils1':'python',
            'skils2':"c",
            'skils3':"c++",
            'skils':"html",
            'skils':'css'}

@app.get("/biks")
def bik():
    return {'car':["DUCK","HERO"],'KTM':'kdshfi'}

@app.get("/cars/{car_id}")
def car(car_id : int):
    return {'id':car_id,'cars':["motto",'RtC','Rose'],'mahi':'bus'}


#uvicorn app:app --reload