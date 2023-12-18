from wikipedia import *
from Body import URL
from fastapi import *

app = FastAPI()


@app.get("/wiki/search_path/{title}")
def getPath(title:str):
    try:
        return {"result": wikipedia.search(title)}
    except PageError:
        raise HTTPException(status_code=404)



@app.get("/wiki/search_query/")
def getQuery(title: str, index: int):
    try:
        return {"result": wikipedia.page(title).images[index]}
    except PageError:
        raise HTTPException(status_code=404)



@app.post("/wiki/search_body")
def postBody(key: URL):
    try:
        return{"result": wikipedia.page(key.title).html()}
    except PageError:
        raise HTTPException(status_code=404)
