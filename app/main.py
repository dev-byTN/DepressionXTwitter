from fastapi import FastAPI
from models.tweet import *
from .test import *

app = FastAPI()

data = readJsonFile()
tweets = getRelevantData(data)

@app.get('/dirty/tweets')
async def get_all_tweets():
    return tweets

@app.get('/dirty/users')
async def get_users():
    return get_users_id()