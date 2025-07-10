from django.shortcuts import render
from integration_utils import *

def index (request):
    context = {"user": request.user }
    return render (request, "GavlanDealApp/index.html", context)
