from fastapi import FastAPI
from models.tweet import readJsonFile, getRelevantData

app = FastAPI()

data = readJsonFile()
tweets = getRelevantData(data)

@app.get('/dirty/tweets')
async def get_tweets():
    return tweets

@app.get("/")
async def root():
    return { "msg": "yo"}