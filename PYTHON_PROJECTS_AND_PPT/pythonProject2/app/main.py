from fastapi import FastAPI

app = FastAPI()    # first install processpip      {       pip install "fastapi[all]"        }


@app.get('/item/item_id}')
def root(item_id):
    return {'id': item_id , "massage":["REDDYVARI MUNI PRASAD"],'sjhg':"shdgty"}    # excut this    {  uvicorn main:app --reload }

