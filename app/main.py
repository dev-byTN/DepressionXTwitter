from fastapi import FastAPI
from models.tweet import *
from .test import *

app = FastAPI()

data = readJsonFile()
tweets = getRelevantData(data)

@app.get('/DepressionXTwitter/tweets/list_tweets')
async def get_all_tweets():
    return tweets

@app.get('/DepressionXTwitter/users/list_users')
async def get_users():
    return get_users_id()