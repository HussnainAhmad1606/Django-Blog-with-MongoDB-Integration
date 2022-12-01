from django.shortcuts import render
from django.http import HttpResponse
import pymongo
from decouple import config

# Create your views here.
def index(request):

    client = pymongo.MongoClient(config('HOST'))

        #Define Db Name
    dbname = client['Blog_DB']

    #Define Collection
    collection = dbname['news']
    data = {
        "name": "Psycho Coder",
        "Role": "CTO"
    }
    collection.insert_one(data)

    return HttpResponse("Connection DONE!")